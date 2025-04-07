# ChatGPT to Markdown Converter

Don't particularly trust anything in this file. I didn't proofread what Claude
wrote. 

A tool to convert ChatGPT backup files (in JSON format) to Markdown files for easier reading and sharing.

## Features

- Converts ChatGPT conversations to readable Markdown files
- Maintains conversation structure and metadata
- Preserves timestamps (optional)
- Handles different message types (text, code, execution output)
- Copies DALL-E image files to the output directory

## Installation

### Option 1: Clone and use directly

```bash
git clone https://github.com/yourusername/chatgpt_to_markdown.git
cd chatgpt_to_markdown
python chatgpt_to_markdown.py /path/to/openai-export-dir
```

### Option 2: Install with pip

```bash
# Install from the cloned repository
git clone https://github.com/yourusername/chatgpt_to_markdown.git
cd chatgpt_to_markdown
pip install .

# Now you can use it from anywhere
chatgpt_to_markdown /path/to/openai-export-dir
```

## Usage

```bash
python chatgpt_to_markdown.py /path/to/openai-export-dir [output_dir]
```

- `/path/to/openai-export-dir`: Path to the directory containing the OpenAI data export (should contain a conversations.json file)
- `output_dir`: (Optional) Output directory for the Markdown files. If not specified, defaults to `tmp_md_<export-dir-name>`

## Example

```bash
python chatgpt_to_markdown.py ~/Downloads/openai-2025-04-06
```

This will create a directory called `tmp_md_openai-2025-04-06` containing all the conversations as Markdown files.

## Output Format

Each conversation is saved as a separate Markdown file with the following format:

```markdown
# Conversation Title

Created: 2025-04-06 14:30:45
Last Updated: 2025-04-06 15:20:12

### User - 2025-04-06 14:30:45

User message text here...

### Assistant - 2025-04-06 14:31:10

Assistant response here...

### Tool (python) - 2025-04-06 14:32:05

```python
print("Hello, world!")
```

### Tool (python) - 2025-04-06 14:32:10

```
Hello, world!
```
```

## Background

This tool was created to make ChatGPT conversation exports more accessible and easier to browse. The OpenAI export format can be difficult to navigate with its nested JSON structure, so this tool flattens each conversation into a readable Markdown file.

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT
