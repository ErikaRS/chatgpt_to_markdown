# ChatGPT to Markdown Converter

A tool to convert ChatGPT backup files (in JSON format) to Markdown files for easier reading and sharing.

## Features

- Converts ChatGPT conversations to readable Markdown files
- Maintains conversation structure and metadata
- Preserves timestamps (optional)
- Handles different message types (text, code, execution output)
- Copies DALL-E image files to the output directory

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

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT