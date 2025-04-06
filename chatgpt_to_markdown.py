#!/usr/bin/env python3

import json
import os
import sys
import re
import html
from datetime import datetime
import shutil

def clean_title(title):
    """Clean a title to make it suitable for a filename."""
    # Replace special characters with underscores
    return re.sub(r'[^\w\s-]', '_', title).strip().replace(' ', '_')

def format_time(timestamp):
    """Format a unix timestamp into a human-readable date."""
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def message_to_markdown(message, include_timestamps=True):
    """Convert a message to markdown format."""
    if not message or "author" not in message:
        return ""
    
    role = message["author"]["role"]
    
    # Skip system messages
    if role == "system":
        return ""
    
    if role == "user":
        prefix = "### User"
    elif role == "assistant":
        prefix = "### Assistant"
    elif role == "tool":
        tool_name = message["author"].get("name", "tool")
        prefix = f"### Tool ({tool_name})"
    else:
        prefix = f"### {role.capitalize()}"
    
    # Get timestamp if available and if requested
    timestamp_str = ""
    if include_timestamps and "create_time" in message and message["create_time"]:
        timestamp_str = f" - {format_time(message['create_time'])}"
    
    # Combine prefix and timestamp
    header = f"{prefix}{timestamp_str}\n\n"
    
    # Get content
    if "content" not in message:
        return header + "*[No content]*\n\n"
    
    content = message["content"]
    
    if content.get("content_type") == "text":
        # Handle text content
        text = "\n\n".join(content.get("parts", []))
        return header + text + "\n\n"
    elif content.get("content_type") == "code":
        # Handle code content
        language = content.get("language", "")
        text = content.get("text", "")
        return header + f"```{language}\n{text}\n```\n\n"
    elif content.get("content_type") == "execution_output":
        # Handle execution output
        text = content.get("text", "")
        return header + f"```\n{text}\n```\n\n"
    else:
        # Handle other content types
        return header + f"*[{content.get('content_type', 'unknown')} content]*\n\n"

def conversation_to_markdown(conversation, include_timestamps=True):
    """Convert a conversation to markdown format."""
    title = conversation.get("title", "Untitled Conversation")
    create_time = conversation.get("create_time")
    update_time = conversation.get("update_time")
    
    # Start with conversation metadata
    md = f"# {title}\n\n"
    
    if include_timestamps:
        if create_time:
            md += f"Created: {format_time(create_time)}\n"
        if update_time:
            md += f"Last Updated: {format_time(update_time)}\n"
        md += "\n"
    
    # Get message mapping and current node
    mapping = conversation.get("mapping", {})
    current_node = conversation.get("current_node")
    
    # Find the root node and traverse the conversation tree
    for node_id, node in mapping.items():
        if not node.get("parent"):
            # This is the root node
            root_id = node_id
            break
    else:
        return md + "*[Could not find conversation root]*\n"
    
    # Walk through the tree starting from root, following the primary child path
    current_id = root_id
    message_chain = []
    
    while current_id:
        node = mapping.get(current_id, {})
        message = node.get("message")
        
        if message:
            message_chain.append(message)
        
        # Move to the next node (first child)
        children = node.get("children", [])
        current_id = children[0] if children else None
    
    # Convert all messages to markdown
    for message in message_chain:
        md += message_to_markdown(message, include_timestamps)
    
    return md

def process_conversations(conversations_file, output_dir, include_timestamps=True):
    """Process all conversations from a JSON file and save as markdown files."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the conversations JSON
    with open(conversations_file, 'r', encoding='utf-8') as f:
        conversations = json.load(f)
    
    # Process each conversation
    for conversation in conversations:
        # Get title or use a default
        title = conversation.get("title", "Untitled Conversation")
        
        # Clean title for use as filename
        filename = clean_title(title)
        if not filename:
            filename = f"conversation_{conversation.get('id', 'unknown')}"
        
        # Ensure filename is unique
        counter = 1
        original_filename = filename
        while os.path.exists(os.path.join(output_dir, f"{filename}.md")):
            filename = f"{original_filename}_{counter}"
            counter += 1
        
        # Convert to markdown
        markdown_content = conversation_to_markdown(conversation, include_timestamps)
        
        # Save to file
        with open(os.path.join(output_dir, f"{filename}.md"), 'w', encoding='utf-8') as f:
            f.write(markdown_content)
    
    print(f"Processed {len(conversations)} conversations to {output_dir}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python chatgpt_to_markdown.py /path/to/openai-export-dir [output_dir]")
        sys.exit(1)
    
    # Get input directory
    input_dir = sys.argv[1]
    
    # Get output directory or create default
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        # Create a directory name based on the input directory
        dir_name = os.path.basename(os.path.normpath(input_dir))
        output_dir = f"tmp_md_{dir_name}"
    
    # Construct path to the conversations.json file
    conversations_file = os.path.join(input_dir, "conversations.json")
    
    if not os.path.exists(conversations_file):
        print(f"Error: Could not find conversations.json in {input_dir}")
        sys.exit(1)
    
    # Process the conversations
    process_conversations(conversations_file, output_dir, include_timestamps=True)
    
    # Copy over any image files from dalle-generations
    dalle_dir = os.path.join(input_dir, "dalle-generations")
    if os.path.exists(dalle_dir) and os.path.isdir(dalle_dir):
        output_dalle_dir = os.path.join(output_dir, "images")
        os.makedirs(output_dalle_dir, exist_ok=True)
        
        # Copy all files from dalle-generations to the output images directory
        for file in os.listdir(dalle_dir):
            src_path = os.path.join(dalle_dir, file)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, output_dalle_dir)
        
        print(f"Copied DALL-E images to {output_dalle_dir}")

if __name__ == "__main__":
    main()