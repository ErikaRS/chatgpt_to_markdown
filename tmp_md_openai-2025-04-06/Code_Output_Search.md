# Code Output Search

Created: 2023-08-27 11:54:23
Last Updated: 2023-08-27 11:54:46

### User - 2023-08-27 11:54:23

In obsidian, how do I search for text that occurs in the result of a code block rather than in the code for the block?

### Assistant - 2023-08-27 11:54:46

In Obsidian, as of my last update in September 2021, the default search functionality searches through the raw markdown content, including the content of code blocks. This means that if you search for a particular text, Obsidian will return notes that have that text in both the code and its output.

To search specifically for text that occurs in the result of a code block, and not in the code itself, you'd need a more sophisticated search or filtering mechanism. Obsidian doesn't natively differentiate between the content of a code block and its output in the search functionality.

However, here are a few workarounds you might consider:

1. **Unique Identifiers**: If the outputs of your code blocks have some unique patterns or identifiers that don't occur in the code itself, you can include those identifiers in your search query. 
2. **Use Comments**: For important results you want to search for later, you can add a comment next to the result. For example, if the result of a code block is `42`, you can write it as `42 <!--result-->`. Later, you can search for `42 <!--result-->` to find that specific result.
3. **External Tools**: If this is a frequent task, consider exporting your Obsidian vault and using external tools or scripts that can parse Markdown and differentiate between code and its output. This is more involved but can be tailored to your exact needs.

Remember that Obsidian's development is active and its capabilities might evolve. It's possible that more advanced search functionalities or plugins that offer this feature could be available in newer versions after 2021. Check Obsidian's official forums or documentation for the most up-to-date information.

