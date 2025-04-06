# AI PR Review Tools

Created: 2024-09-16 20:05:56
Last Updated: 2024-09-16 20:10:54

### User - 2024-09-16 20:05:56

Flesh out this summary, including going a bit more into depth on the tasks (especially the types of improvements such tools might suggest). Also, for each tool listed, create a 1-2 sentence summary for that tool. 

- Summary
    - Value proposition:
        - to author: pre-review before going to human reviewer, surface common categories of issues, reduce toil of writing PR descriptions
        - to reviewer: get help understanding changes
    - Surfaces: CLI, opening PR (author tool), comments (author (and reviewer?) tool)
    - Tasks: summaries for explanation and documentation, suggesting improvements to code in the PR, helping resolve comments, reviewing code
    - Modalities: automatically generated (e.g., generating review comments), interactive (e.g., asking for an explanation of a PR)
    - Tools: a couple of this integrate with static code analysis tools
- [CodeRabbit](https://coderabbit.ai/) ([source](https://github.com/coderabbitai/ai-pr-reviewer) - older version)
    - What it does (from the docs)
        - It provides context-aware review feedback on a pull request within minutes… Developers can chat with the bot within the code, which allows them to provide additional context, ask questions, or have the bot generate code. It learns from your suggestions and gets better over time.
        - **CodeRabbit** seamlessly integrates with GitHub and GitLab repositories… Review feedback is sent back to the pull requests and can be directly committed.
        - **CodeRabbit** integrates into code repositories using GitHub or GitLab webhooks and monitors events related to Pull Request (PR) and Merge Request (MR) changes. A comprehensive review is performed when a PR or MR is created, and for incremental commits and comments addressed to the bot. The feedback is then sent directly back to the PR or MR.
    - What it does (from the old version)
        - **PR Summarization; Line-by-line code change suggestions; Continuous, incremental reviews; Chat with bot; Customizable prompts**
- [CodiumAI PR-Agent](https://www.codium.ai/products/git-plugin/) ([source](https://github.com/Codium-ai/pr-agent))
    - How it works
        - [List of supported commands](https://github.com/Codium-ai/pr-agent?tab=readme-ov-file#overview). Includes
            - Reviewing, describing, improving, asking, test, update changelog, update PR description, and more
    - How it works (from the source page)
        - different interfaces, such as CLI, PR Comments, or by automatically triggering them when a new PR is opened.
- [sourcery.ai](https://sourcery.ai/)
    - How it works
        - instantly reviewing every pull request
        - general feedback, in-line comments, and relevant suggestions.
        - on the lookout for any dangerous things that might have crept into your code.
        - Sourcery checks every PR to make sure it's well designed and flags and fixes dangerous complexity.
- [Bito AI Code Review Agent](https://bito.ai/product/ai-code-review-agent/) ([source](https://github.com/gitbito/codereviewagent/blob/main/README.md))
    - From the product page
        - In both IDE and in git workflow
        - PR summaries, code suggestions,
        - Integrates with static analysis tools and third party tools
    - From the source repo
        - It is an automated AI assistant (powered by OpenAI’s GPT-4 and Anthropic’s Claude 2.1) that will review your team’s code; it spots bugs, issues, code smells, and security vulnerabilities in Pull/Merge Requests (PR/MR) and provides high-quality suggestions to fix them.
        - It seamlessly **integrates with Git providers such as GitHub, GitLab, and Bitbucket (coming soon)**, automatically posting recommendations directly as comments within the corresponding Pull Request. It includes real-time recommendations from static analysis and OSS vulnerability tools such as fbinfer, Dependency-Check, etc., and can include high severity suggestions from other 3rd party tools you use such as Snyk or Sonar.
        - The upcoming Bito's **Native Code RAG** feature will enable the AI Code Review Agent to understand your entire codebase, offering better context-aware analysis and suggestions for a more personalized and contextually relevant code review experience.
- [Korbit](https://www.korbit.ai/)
    - Write PR descriptions, finds issues and explains fixes, interactive code suggestion bot
    - Easily configure Korbit to tell it what types of issues to surface and which to mute.
    - tune Korbit to work with your team's best practices, tech stack, and priorities.
    - Analytics: tracks and reports on all activity so you can easily see team improvement, and know the state of your projects.
- [taskade](https://www.taskade.com/agents/programming/automated-code-review)
    - Integrated seamlessly into development workflows, they analyze code submissions for errors, adherence to coding standards, and various other quality metrics.
    - Beyond error detection, these AI agents advocate for best practices and maintainability in programming. They do so by offering suggestions for code refactoring and optimization,
    - Detect Errors, Enforce Standards, Optimize Code, Security Checks, Code Documentation

### Tool (a8km123) - 2024-09-16 20:06:15

**Promising solutions**

I’m mapping out the summary by adding depth to tasks and detailing each tool. This involves highlighting suggested improvements and providing concise tool overviews.

**Refining the summary**

I’m digging into a more detailed summary, identifying tasks and potential improvements. Each tool will get a concise 1-2 sentence summary to clarify their purpose.

**Highlighting value**

Hm, that's interesting—this offering tantalizes with pre-human review, pinpointing common issues and easing PR description toil, while also aiding reviewers in grasping changes. Automated and interactive modalities seem promising.

**Evaluating code review tools**

I'm gathering info on tools that aid developers by streamlining code reviews, suggesting enhancements, and highlighting key areas for attention. They integrate into command-line interfaces and PR platforms, offering both automatic and interactive support.

**Utilizing AI assistants**

I’m exploring the roles of AI assistants in code reviews, such as CodiumAI PR-Agent for interactive review and Sourcery.ai for instant feedback. These tools enhance the review process and provide valuable insights.

**Evaluating AI enhancements**

I’m examining tools like Bito AI Code Review Agent, Korbit, and Taskade. These AI-driven assistants streamline code reviews, emphasizing identifying errors, suggesting improvements, aligning with best practices, and tracking progress.

**Enhancing the summary**

I’m adding detailed examples of each suggestion, covering refactoring, optimization, and security checks. This makes the summary more informative and applicable.

**Mapping out tasks**

I'm thinking through the duties: summarizing code, suggesting improvements, automating reviews, aiding documentation, and assessing change impacts. This covers a wide range of tasks to ensure code quality and efficiency.

### Assistant - 2024-09-16 20:06:15



