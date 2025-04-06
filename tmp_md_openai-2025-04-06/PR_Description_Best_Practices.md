# PR Description Best Practices

Created: 2024-09-18 12:26:24
Last Updated: 2024-09-18 16:03:10

### User - 2024-09-18 12:26:24

Summarize this into a preamble for a prompt for generating PR descriptions from diffs:
Introduction
A good change description is essential for effective code review and collaboration. The first line of the description plays a crucial role in providing a summary of the changes and facilitating understanding among team members.

Importance of the First Line 12
The first line of the change description should indicate the type of change, providing a summary of the entire change. This summary is used in various contexts, such as code review tools, email notifications, and history summaries within Code Search.

Effective Code Review 123
A good change description is essential for effective code review. The description should explain why the change was proposed, what problem it solves, and how it was implemented. This information helps reviewers understand the context of the issue and the code changes, enabling them to provide constructive feedback.

Collaboration and Knowledge Transfer 14
A well-written change description facilitates collaboration and knowledge transfer among team members. It provides a historical record of the changes, allowing developers to understand the reasoning behind the changes and learn from each other's experiences.

### Assistant - 2024-09-18 12:26:32



### Assistant - 2024-09-18 12:26:32

To generate effective pull request descriptions from diffs, it's essential to focus on crafting concise, informative summaries that enhance code review and collaboration. The first line should provide a clear summary of the type and purpose of the change, enabling easy reference in tools, email notifications, and historical records. A well-written description explains the problem being solved, the rationale behind the changes, and how they were implemented, promoting efficient code reviews and knowledge transfer across the team.

### User - 2024-09-18 12:27:03

Make this more of an instruction. E.g., "generate a pull request from these diffs. It should be a concise, informative summary..."

### Assistant - 2024-09-18 12:27:08

Generate a pull request description from these diffs. It should be a concise, informative summary that starts with a clear first line indicating the type and purpose of the change. The description should explain the problem being addressed, the rationale behind the changes, and how they were implemented. Ensure that the description promotes effective code review and facilitates collaboration by providing the necessary context and helping team members understand the changes.

### User - 2024-09-18 14:51:37

Summarize this without losing any of the substance: 
Format
A commit message has two parts: a subject and a body. These are separated by a blank line.

Subject
The subject line should be concise and easy to visually scan in a list of commits, giving context around what code has changed.

Prefix the subject with the primary area of code that was affected (e.g. web:, cmd/searcher:).
Limit the subject line to 50 characters.
Do not end the subject line with punctuation.
Use the imperative mood in the subject line.
Prefer	Instead of
Fix bug in XYZ	Fixed a bug in XYZ
Change behavior of X	Changing behavior of X
Example:

cmd/searcher: Add scaffolding for structural search

Body
The purpose of a commit body is to explain what changed and why. The how is the diff.

Pull request reviews happens in PRs, which should contain a good subject and description. When a PR is approved, we prefer to squash merge all commits on the PR branch into a single commit on master. After clicking "Squash and merge", edit the body of the final commit message so that it is clean and informative. The commit body should either be empty (assuming that you have a good PR description), or a brief summary of your change (which could be exactly your PR description if it is concise). It should not include unimportant details from incremental commits on the PR branch (e.g. * add test, * fix test, * try X, Update filename.md, Co-Authored-By...).

### Assistant - 2024-09-18 14:51:50

A commit message consists of two parts: a subject and a body, separated by a blank line.

**Subject:**  
- Keep it concise and scannable, providing context on the affected code.  
- Prefix the subject with the primary area of the code (e.g., `web:`, `cmd/searcher:`).  
- Limit the subject to 50 characters and avoid punctuation at the end.  
- Use the imperative mood (e.g., "Fix bug in XYZ" instead of "Fixed a bug in XYZ").  
  Example: `cmd/searcher: Add scaffolding for structural search`

**Body:**  
- Explain what changed and why; the diff shows how.  
- In PRs, ensure a good subject and description. Upon PR approval, squash merge commits into one.  
- The commit body should be either empty (if the PR description is clear) or a concise summary, excluding incremental commit details (e.g., "* add test," "* fix test").

### User - 2024-09-18 16:01:55

What should a change description (especially one that aims to be concise) say about the individual files changed? The goal is to avoid redundancy with either the information in the PR itself (e.g., the list of files) or with information that should be in the overall change description. 

### Assistant - 2024-09-18 16:02:06

A concise change description should briefly mention the individual files changed only when it adds meaningful context that isn't redundant with the PR's file list or overall description. Focus on the *purpose* of the changes in each file and how they contribute to the overall change, rather than simply listing the files. For example, note if a file was updated to fix a specific issue, implement a feature, or refactor code, but avoid repeating information that is clear from the diff itself. Here's how to approach it:

- Mention files if they play a crucial role in the change (e.g., "Updated `api.js` to handle new validation logic").
- Highlight structural or significant changes (e.g., "Refactored `config.yaml` to streamline configuration options").
- Avoid detailing small, incremental changes (e.g., formatting, minor bug fixes) unless they are essential to understanding the purpose.

This ensures that the change description is informative without being redundant.

