# PR Style Guide ACK

Created: 2024-10-15 16:03:12
Last Updated: 2024-10-15 16:20:28

### User - 2024-10-15 16:03:12

Here is a PR style guide. For now, just ACK this

# Pull requests

This guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:

1. How to create a PR
2. How to make the PR easy to review
3. How to review PRs
4. What "quick stamp"s mean

## 1. How to create a PR

This section defines guidelines for PRs.

- Suggested branch naming convention: `initials/description`
    
    Example: `aa/replace-button-title` 
    
- To make it easier to skim commit history, name the PR with
    - the team associated with the change
    - a short but precise description of the change
    
    Example: `search: update repo filter to be faster`
    
- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance.
    
    Example: `team/search`
    
- If the PR is a result of a related GitHub issue, include “Closes #12345” in the PR’s description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue). This will also link the ticket and the PR together so that if anyone looks at either in the future, they won’t have any issue trying to find the corresponding ticket/PR as it will be noted in the sidebar.
- Defer merging a PR until at least one person has approved of the changes.

Suggested but not required:

- If the PR makes a visual change to the UI (ex: changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.
- Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.

Further reading:

- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)

## 2. How to make the PR easy to review

To create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:

1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.
    1. You can take advantage of the “draft” mode for previewing and self-checking, and mark it ready for review once it’s ready.
2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.
3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.
4. **Choose 1 or 2 targeted reviewers:** Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. 
5. **Stay focused on the goal**: Keep the changes in your PR focused on the specific goal and avoid unrelated changes.
6. **Optimize for reviewers:** Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.
7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.
8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.
9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., "What changes would be helpful?"
10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.
11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.
12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.

By following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.

### Choosing reviewers

## 3. How to review PRs

### Checklist of things to look for

1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).
2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or "future-proofing".
3. **Review tests**: Ensure tests are adequate and appropriate.
4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.
5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.
6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.
7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).
8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.
9. **Dependencies**: Review any new dependencies and ensure they are appropriate.
10. **Security**: Check for potential security issues.
11. **Performance**: Consider potential performance issues and their impact.
12. @Joe Chen Backwards compatible?

### Soft skills around code reviews

Reviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.

1. Prioritize code reviews
    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.
2. Be mindful of your communication
    - Use "**we**" instead of "you" when discussing code changes.
    - Make **polite requests** instead of commands, e.g., "Could we...?"
    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.
3. Focus on improvement and learning
    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.
    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.
4. Handle bugs and large PRs appropriately
    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.
    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.
5. Offer sincere praise and positive feedback
    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.
6. Resolve conflicts and stalemates
    - Accept the PR if only minor or optional changes remain.
    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.

Following these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.

## 4. What "quick stamp"s mean

"Quick stamp" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A "quick stamp" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.

### Expectations and responsibilities of a stamper

As a stamper, you should:

1. Review the PR to your usual standards, even if it's a request for a "quick stamp."
2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.
3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:
    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or
    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.

Remember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.

### The GitHub "stampers" team

The GitHub "stampers" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the "stampers" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.

To join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.

## 5. Cody-related PRs

Cody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we’ve decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.

What you as an engineer need to do:

- Remember that it may not always be clear-cut what “Cody-related” means. Use your best judgment.
- For the same reason, this process can’t be easily automated. → There is unfortunately no reminder to add the label.
- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)
- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.
- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it’s an OSS contribution, add the label yourself.
- **Think QA:** We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product.

### Assistant - 2024-10-15 16:03:15



### Assistant - 2024-10-15 16:03:15

ACK. Let me know if you need any edits, elaborations, or suggestions based on this guide.

### User - 2024-10-15 16:04:14

In the style of this doc, draft the "Choosing reviewers" section to be consistent with these two messages. The goal is to be concise and actionable rather than philosophical.

Message 1:
We have teams with wide timezone spreads, and sometimes you may feel delayed waiting on code reviews. What I would encourage everyone to do is:
At the start of the project choose 1-2 designated reviewers who are within ~3hrs of your working hours
Preferably on your team, but if that's not possible, then it may be fine to find someone not on the team if they have appropriate context
Introduce them to the project
Share the Linear project
Take some time to meet with them sync to introduce them to the project's goals and planned approach
Preferentially send reviews to the designated reviewer
This won't solve all of our timezone problems, but by doing a bit of prep to ramp someone up on context, my hope is that we can reduce the problem where folks have a hard time jumping in on reviews because they don't feel like they have the context to be any more qualified than anyone else to do the review. This also gives us the opportunity to load balance reviews better by giving folks with less context on the overall system more opportunities to build up that context.
Thoughts?

Message 2: 
It makes sense to me to unlock reviews if you struggle with that, but when the person is from outside your team I think you should still make sure that your team members also review the code, even if post-merge.
Why?
Ownership is a team level concern, not an individuals - and when one person in a team regularly gets reviews from outside the team only there will be a low bus factor and a more difficult time for team members to provide support.
Also, I expect that regardless of how much context you share, an outsider will not be able to provide the same depth for the review.
Random example: Reviewing a new gitserver endpoint is not that difficult, just check that the generated git command looks sane and you should be good.
But spotting the ways it could be exploited or making it really performant by utilizing some lower level git concept is something you only build up as knowledge over months or years of building the subsystem.

### Assistant - 2024-10-15 16:04:19

{
  "name": "choosing_reviewers",
  "type": "document",
  "content": "### Choosing Reviewers\n\n- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.\n\n- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.\n\n- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.\n\n- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge."
}

### Tool (canmore.create_textdoc) - 2024-10-15 16:04:19

{"result": "Successfully created text document 'choosing_reviewers' which will be referenced in all future messages with the unique identifier textdoc_id: '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765", "name": "choosing_reviewers"}

### Assistant - 2024-10-15 16:04:19

Let me know if this aligns with your expectations or if you'd like me to adjust anything further.

### User - 2024-10-15 16:06:27

Now let's update this whole doc:
# Pull requests

This guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:

1. How to create a PR
2. How to make the PR easy to review
3. How to review PRs
4. What "quick stamp"s mean

## 1. How to create a PR

This section defines guidelines for PRs.

- Suggested branch naming convention: `initials/description`
    
    Example: `aa/replace-button-title` 
    
- To make it easier to skim commit history, name the PR with
    - the team associated with the change
    - a short but precise description of the change
    
    Example: `search: update repo filter to be faster`
    
- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance.
    
    Example: `team/search`
    
- If the PR is a result of a related GitHub issue, include “Closes #12345” in the PR’s description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue). This will also link the ticket and the PR together so that if anyone looks at either in the future, they won’t have any issue trying to find the corresponding ticket/PR as it will be noted in the sidebar.
- Defer merging a PR until at least one person has approved of the changes.

Suggested but not required:

- If the PR makes a visual change to the UI (ex: changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.
- Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.

Further reading:

- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)

## 2. How to make the PR easy to review

To create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:

1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.
    1. You can take advantage of the “draft” mode for previewing and self-checking, and mark it ready for review once it’s ready.
2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.
3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.
4. **Choose 1 or 2 targeted reviewers:** Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. 
5. **Stay focused on the goal**: Keep the changes in your PR focused on the specific goal and avoid unrelated changes.
6. **Optimize for reviewers:** Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.
7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.
8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.
9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., "What changes would be helpful?"
10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.
11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.
12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.

By following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.

### Choosing reviewers

- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.
- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.
- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.
- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge.

## 3. How to review PRs

### Checklist of things to look for

1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).
2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or "future-proofing".
3. **Review tests**: Ensure tests are adequate and appropriate.
4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.
5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.
6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.
7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).
8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.
9. **Dependencies**: Review any new dependencies and ensure they are appropriate.
10. **Security**: Check for potential security issues.
11. **Performance**: Consider potential performance issues and their impact.
12. @Joe Chen Backwards compatible?

### Soft skills around code reviews

Reviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.

1. Prioritize code reviews
    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.
2. Be mindful of your communication
    - Use "**we**" instead of "you" when discussing code changes.
    - Make **polite requests** instead of commands, e.g., "Could we...?"
    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.
3. Focus on improvement and learning
    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.
    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.
4. Handle bugs and large PRs appropriately
    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.
    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.
5. Offer sincere praise and positive feedback
    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.
6. Resolve conflicts and stalemates
    - Accept the PR if only minor or optional changes remain.
    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.

Following these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.

## 4. What "quick stamp"s mean

"Quick stamp" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A "quick stamp" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.

### Expectations and responsibilities of a stamper

As a stamper, you should:

1. Review the PR to your usual standards, even if it's a request for a "quick stamp."
2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.
3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:
    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or
    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.

Remember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.

### The GitHub "stampers" team

The GitHub "stampers" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the "stampers" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.

To join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.

## 5. Cody-related PRs

Cody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we’ve decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.

What you as an engineer need to do:

- Remember that it may not always be clear-cut what “Cody-related” means. Use your best judgment.
- For the same reason, this process can’t be easily automated. → There is unfortunately no reminder to add the label.
- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)
- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.
- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it’s an OSS contribution, add the label yourself.
- **Think QA:** We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product.

### Assistant - 2024-10-15 16:06:55

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "# Pull requests\n\nThis guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:\n\n1. How to create a PR\n2. How to make the PR easy to review\n3. How to review PRs\n4. What \"quick stamp\"s mean\n\n## 1. How to create a PR\n\nThis section defines guidelines for PRs.\n\n- Suggested branch naming convention: `initials/description`\n    \n    Example: `aa/replace-button-title` \n    \n- To make it easier to skim commit history, name the PR with\n    - the team associated with the change\n    - a short but precise description of the change\n    \n    Example: `search: update repo filter to be faster`\n    \n- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance.\n    \n    Example: `team/search`\n    \n- If the PR is a result of a related GitHub issue, include \"Closes #12345\" in the PR's description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue). This will also link the ticket and the PR together so that if anyone looks at either in the future, they won't have any issue trying to find the corresponding ticket/PR as it will be noted in the sidebar.\n- Defer merging a PR until at least one person has approved of the changes.\n\nSuggested but not required:\n\n- If the PR makes a visual change to the UI (e.g., changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.\n- Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.\n\nFurther reading:\n\n- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)\n\n## 2. How to make the PR easy to review\n\nTo create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:\n\n1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.\n    1. You can take advantage of the \"draft\" mode for previewing and self-checking, and mark it ready for review once it's ready.\n2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.\n3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.\n4. **Choose 1 or 2 targeted reviewers**: Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. \n5. **Stay focused on the goal**: Keep the changes in your PR focused on the specific goal and avoid unrelated changes.\n6. **Optimize for reviewers**: Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.\n7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.\n8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.\n9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., \"What changes would be helpful?\"\n10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.\n11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.\n12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.\n\nBy following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.\n\n### Choosing reviewers\n\n- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.\n- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.\n- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.\n- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge.\n\n## 3. How to review PRs\n\n### Checklist of things to look for\n\n1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).\n2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or \"future-proofing\".\n3. **Review tests**: Ensure tests are adequate and appropriate.\n4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.\n5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.\n6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.\n7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).\n8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.\n9. **Dependencies**: Review any new dependencies and ensure they are appropriate.\n10. **Security**: Check for potential security issues.\n11. **Performance**: Consider potential performance issues and their impact.\n12. **Backward compatibility**: Ensure changes are backward compatible if required.\n\n### Soft skills around code reviews\n\nReviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.\n\n1. **Prioritize code reviews**\n    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.\n2. **Be mindful of your communication**\n    - Use \"**we**\" instead of \"you\" when discussing code changes.\n    - Make **polite requests** instead of commands, e.g., \"Could we...?\"\n    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.\n3. **Focus on improvement and learning**\n    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.\n    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.\n4. **Handle bugs and large PRs appropriately**\n    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.\n    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.\n5. **Offer sincere praise and positive feedback**\n    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.\n6. **Resolve conflicts and stalemates**\n    - Accept the PR if only minor or optional changes remain.\n    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.\n\nFollowing these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.\n\n## 4. What \"quick stamp\"s mean\n\n\"Quick stamp\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A \"quick stamp\" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.\n\n### Expectations and responsibilities of a stamper\n\nAs a stamper, you should:\n\n1. Review the PR to your usual standards, even if it's a request for a \"quick stamp.\"\n2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.\n3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:\n    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or\n    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.\n\nRemember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.\n\n### The GitHub \"stampers\" team\n\nThe GitHub \"stampers\" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the \"stampers\" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.\n\nTo join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.\n\n## 5. Cody-related PRs\n\nCody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we've decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.\n\nWhat you as an engineer need to do:\n\n- Remember that it may not always be clear-cut what \"Cody-related\" means. Use your best judgment.\n- For the same reason, this process can't be easily automated. \u2192 There is unfortunately no reminder to add the label.\n- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)\n- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.\n- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it's an OSS contribution, add the label yourself.\n- **Think QA**: We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:06:55

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:06:55

I've updated the entire document to include all the requested changes. Let me know if there's anything else you'd like to modify or clarify.

### User - 2024-10-15 16:07:22

Where can this document be made clearer, more actionable, and more concise?

### Assistant - 2024-10-15 16:07:40

{
  "comments": [
    {
      "pattern": "This guide will walk you through the process of creating, reviewing, and approving pull requests \\(PRs\\)\\. It covers the following topics:.*?",
      "comment": "Consider summarizing the topics into a concise bullet list to improve clarity and readability."
    },
    {
      "pattern": "- Suggested branch naming convention: `initials/description`\\n\\s+Example: `aa/replace-button-title`",
      "comment": "Remove the example or make it more succinct to keep the instructions clear and to the point."
    },
    {
      "pattern": "- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance\\.\\n\\s+Example: `team/search`",
      "comment": "Consider simplifying this instruction by combining the guideline and the example into a single, concise sentence."
    },
    {
      "pattern": "Suggested but not required:\\n\\s+- If the PR makes a visual change to the UI \\(e\\.g\\., changing the text of a button\\), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change\\.",
      "comment": "Consider breaking this into two concise bullet points to improve readability and make the suggestions actionable."
    },
    {
      "pattern": "To create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:",
      "comment": "Consider simplifying this introduction by focusing on actionable language, e.g., 'Follow these steps to create a PR that is easy to review.'"
    },
    {
      "pattern": "12\\. \\*\\*Express gratitude for feedback\\*\\*: Thank your reviewer for their feedback and suggestions\\.",
      "comment": "Consider moving this point to the soft skills section to maintain a more technical focus here."
    },
    {
      "pattern": "By following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process\\.",
      "comment": "Consider removing this summary sentence to keep the section concise."
    },
    {
      "pattern": "\\*\\*Select reviewers early\\*\\*: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours\\.",
      "comment": "Simplify this to 'Identify 1-2 reviewers within 3 hours of your working hours at the start of the project.'"
    },
    {
      "pattern": "Reviewing PRs is not only a technical process but also a social one\\. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process\\.",
      "comment": "Consider shortening to 'Reviewing PRs is both technical and social. Follow these guidelines for an efficient, friendly process.'"
    },
    {
      "pattern": "6\\. \\*\\*Resolve conflicts and stalemates\\*\\*:.*?",
      "comment": "Clarify that minor or optional changes can be accepted to avoid blocking the PR unnecessarily."
    },
    {
      "pattern": "\\\"Quick stamp\\\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve\\..*?",
      "comment": "Consider simplifying to 'A \"quick stamp\" is a request for reviewing trivial changes. It should not bypass standard review practices.'"
    }
  ]
}

### Tool (canmore.comment_textdoc) - 2024-10-15 16:07:40

Failed with error. Fix the error and try again before replying to the user.

comments.9.pattern: pattern not found in the document: /6\. \*\*Resolve conflicts and stalemates\*\*:.*?/ pattern must be a python regular expression with valid escape sequences

### Assistant - 2024-10-15 16:07:40

{
  "comments": [
    {
      "pattern": "This guide will walk you through the process of creating, reviewing, and approving pull requests \\(PRs\\)\\. It covers the following topics:.*?",
      "comment": "Consider summarizing the topics into a concise bullet list to improve clarity and readability."
    },
    {
      "pattern": "- Suggested branch naming convention: `initials/description`\\n\\s+Example: `aa/replace-button-title`",
      "comment": "Remove the example or make it more succinct to keep the instructions clear and to the point."
    },
    {
      "pattern": "- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance\\.\\n\\s+Example: `team/search`",
      "comment": "Consider simplifying this instruction by combining the guideline and the example into a single, concise sentence."
    },
    {
      "pattern": "Suggested but not required:\\n\\s+- If the PR makes a visual change to the UI \\(e\\.g\\., changing the text of a button\\), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change\\.",
      "comment": "Consider breaking this into two concise bullet points to improve readability and make the suggestions actionable."
    },
    {
      "pattern": "To create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:",
      "comment": "Consider simplifying this introduction by focusing on actionable language, e.g., 'Follow these steps to create a PR that is easy to review.'"
    },
    {
      "pattern": "12\\. \\*\\*Express gratitude for feedback\\*\\*: Thank your reviewer for their feedback and suggestions\\.",
      "comment": "Consider moving this point to the soft skills section to maintain a more technical focus here."
    },
    {
      "pattern": "By following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process\\.",
      "comment": "Consider removing this summary sentence to keep the section concise."
    },
    {
      "pattern": "\\*\\*Select reviewers early\\*\\*: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours\\.",
      "comment": "Simplify this to 'Identify 1-2 reviewers within 3 hours of your working hours at the start of the project.'"
    },
    {
      "pattern": "Reviewing PRs is not only a technical process but also a social one\\. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process\\.",
      "comment": "Consider shortening to 'Reviewing PRs is both technical and social. Follow these guidelines for an efficient, friendly process.'"
    },
    {
      "pattern": "\\*\\*Resolve conflicts and stalemates\\*\\*\\n\\s+- Accept the PR if only minor or optional changes remain\\.",
      "comment": "Clarify that minor or optional changes can be accepted to avoid blocking the PR unnecessarily."
    },
    {
      "pattern": "\\\"Quick stamp\\\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve\\..*?",
      "comment": "Consider simplifying to 'A \"quick stamp\" is a request for reviewing trivial changes. It should not bypass standard review practices.'"
    }
  ]
}

### Tool (canmore.comment_textdoc) - 2024-10-15 16:07:40

{"result": "Successfully added comments to text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:07:40

I've added comments to make the document clearer, more concise, and actionable. Let me know if you need further adjustments or specific sections improved.

### User - 2024-10-15 16:16:17

Given this line:
Stay focused on the goal: Keep the changes in your PR focused on the specific goal and avoid unrelated changes.

Apply this feedback:
Comment 1: 
I personally think it’s fine to include small and unrelated code cleanups in a PR. I like the boy scout rule (”leave campground cleaner than when you found it”). The overhead of using GitHub PRs combined with our async culture makes it impractical to break everything into small PRs. I think alternative code review system like https://graphite.dev/ would improve the situation, but I don’t think we have enough problems with GH PRs yet to justify switching a system (let’s start with Linear)

Comment 2: 
I also do piggybacks from time to time, but that always comes at the risk of “initially thought to be benign, turns out holding back the review approval (that are completely unrelated to the core changes proposed)”.

Feel like we need some novel wording for:

Out of principle, you’re advised to “stay focused”. In practice, “piggyback at your own risk”.  

### Assistant - 2024-10-15 16:16:47

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "# Pull requests\n\nThis guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:\n\n1. How to create a PR\n2. How to make the PR easy to review\n3. How to review PRs\n4. What \"quick stamp\"s mean\n\n## 1. How to create a PR\n\nThis section defines guidelines for PRs.\n\n- Suggested branch naming convention: `initials/description`\n    \n    Example: `aa/replace-button-title` \n    \n- To make it easier to skim commit history, name the PR with\n    - the team associated with the change\n    - a short but precise description of the change\n    \n    Example: `search: update repo filter to be faster`\n    \n- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance.\n    \n    Example: `team/search`\n    \n- If the PR is a result of a related GitHub issue, include \"Closes #12345\" in the PR's description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue). This will also link the ticket and the PR together so that if anyone looks at either in the future, they won't have any issue trying to find the corresponding ticket/PR as it will be noted in the sidebar.\n- Defer merging a PR until at least one person has approved of the changes.\n\nSuggested but not required:\n\n- If the PR makes a visual change to the UI (e.g., changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.\n- Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.\n\nFurther reading:\n\n- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)\n\n## 2. How to make the PR easy to review\n\nTo create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:\n\n1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.\n    1. You can take advantage of the \"draft\" mode for previewing and self-checking, and mark it ready for review once it's ready.\n2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.\n3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.\n4. **Choose 1 or 2 targeted reviewers**: Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. \n5. **Stay focused on the goal**: Keep the changes in your PR focused on the specific goal and avoid unrelated changes. Small, unrelated cleanups are acceptable if they follow the \"leave it better than you found it\" principle, but be mindful of the risk that such changes could delay review approval if they turn out to be more complex than anticipated. In practice, piggybacking on unrelated changes is done at your own risk.\n6. **Optimize for reviewers**: Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.\n7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.\n8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.\n9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., \"What changes would be helpful?\"\n10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.\n11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.\n12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.\n\nBy following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.\n\n### Choosing reviewers\n\n- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.\n- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.\n- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.\n- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge.\n\n## 3. How to review PRs\n\n### Checklist of things to look for\n\n1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).\n2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or \"future-proofing\".\n3. **Review tests**: Ensure tests are adequate and appropriate.\n4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.\n5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.\n6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.\n7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).\n8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.\n9. **Dependencies**: Review any new dependencies and ensure they are appropriate.\n10. **Security**: Check for potential security issues.\n11. **Performance**: Consider potential performance issues and their impact.\n12. **Backward compatibility**: Ensure changes are backward compatible if required.\n\n### Soft skills around code reviews\n\nReviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.\n\n1. **Prioritize code reviews**\n    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.\n2. **Be mindful of your communication**\n    - Use \"**we**\" instead of \"you\" when discussing code changes.\n    - Make **polite requests** instead of commands, e.g., \"Could we...?\"\n    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.\n3. **Focus on improvement and learning**\n    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.\n    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.\n4. **Handle bugs and large PRs appropriately**\n    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.\n    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.\n5. **Offer sincere praise and positive feedback**\n    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.\n6. **Resolve conflicts and stalemates**\n    - Accept the PR if only minor or optional changes remain.\n    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.\n\nFollowing these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.\n\n## 4. What \"quick stamp\"s mean\n\n\"Quick stamp\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A \"quick stamp\" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.\n\n### Expectations and responsibilities of a stamper\n\nAs a stamper, you should:\n\n1. Review the PR to your usual standards, even if it's a request for a \"quick stamp.\"\n2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.\n3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:\n    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or\n    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.\n\nRemember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.\n\n### The GitHub \"stampers\" team\n\nThe GitHub \"stampers\" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the \"stampers\" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.\n\nTo join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.\n\n## 5. Cody-related PRs\n\nCody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we've decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.\n\nWhat you as an engineer need to do:\n\n- Remember that it may not always be clear-cut what \"Cody-related\" means. Use your best judgment.\n- For the same reason, this process can't be easily automated. \u2192 There is unfortunately no reminder to add the label.\n- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)\n- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.\n- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it's an OSS contribution, add the label yourself.\n- **Think QA**: We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:16:47

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:16:47

I've updated the guidance about staying focused on the goal in PRs to reflect the feedback, balancing the importance of focus with the reality of small cleanups. Let me know if there's anything else you'd like to adjust or clarify.

### User - 2024-10-15 16:16:57

Make the "stay focused on the goal" item more concise. Keep it closer to the length of the other items

### Assistant - 2024-10-15 16:17:28

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "# Pull requests\n\nThis guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:\n\n1. How to create a PR\n2. How to make the PR easy to review\n3. How to review PRs\n4. What \"quick stamp\"s mean\n\n## 1. How to create a PR\n\nThis section defines guidelines for PRs.\n\n- Suggested branch naming convention: `initials/description`\n    \n    Example: `aa/replace-button-title` \n    \n- To make it easier to skim commit history, name the PR with\n    - the team associated with the change\n    - a short but precise description of the change\n    \n    Example: `search: update repo filter to be faster`\n    \n- Apply applicable team label to the PR so that the associated team can easily find and identify PRs at a glance.\n    \n    Example: `team/search`\n    \n- If the PR is a result of a related GitHub issue, include \"Closes #12345\" in the PR's description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue). This will also link the ticket and the PR together so that if anyone looks at either in the future, they won't have any issue trying to find the corresponding ticket/PR as it will be noted in the sidebar.\n- Defer merging a PR until at least one person has approved of the changes.\n\nSuggested but not required:\n\n- If the PR makes a visual change to the UI (e.g., changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.\n- Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.\n\nFurther reading:\n\n- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)\n\n## 2. How to make the PR easy to review\n\nTo create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:\n\n1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.\n    1. You can take advantage of the \"draft\" mode for previewing and self-checking, and mark it ready for review once it's ready.\n2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.\n3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.\n4. **Choose 1 or 2 targeted reviewers**: Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. \n5. **Stay focused on the goal**: Keep changes focused on the specific goal, but small, unrelated cleanups are acceptable if they add value and don't complicate the review.\n6. **Optimize for reviewers**: Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.\n7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.\n8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.\n9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., \"What changes would be helpful?\"\n10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.\n11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.\n12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.\n\nBy following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.\n\n### Choosing reviewers\n\n- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.\n- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.\n- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.\n- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge.\n\n## 3. How to review PRs\n\n### Checklist of things to look for\n\n1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).\n2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or \"future-proofing\".\n3. **Review tests**: Ensure tests are adequate and appropriate.\n4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.\n5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.\n6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.\n7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).\n8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.\n9. **Dependencies**: Review any new dependencies and ensure they are appropriate.\n10. **Security**: Check for potential security issues.\n11. **Performance**: Consider potential performance issues and their impact.\n12. **Backward compatibility**: Ensure changes are backward compatible if required.\n\n### Soft skills around code reviews\n\nReviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.\n\n1. **Prioritize code reviews**\n    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.\n2. **Be mindful of your communication**\n    - Use \"**we**\" instead of \"you\" when discussing code changes.\n    - Make **polite requests** instead of commands, e.g., \"Could we...?\"\n    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.\n3. **Focus on improvement and learning**\n    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.\n    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.\n4. **Handle bugs and large PRs appropriately**\n    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.\n    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.\n5. **Offer sincere praise and positive feedback**\n    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.\n6. **Resolve conflicts and stalemates**\n    - Accept the PR if only minor or optional changes remain.\n    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.\n\nFollowing these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.\n\n## 4. What \"quick stamp\"s mean\n\n\"Quick stamp\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A \"quick stamp\" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.\n\n### Expectations and responsibilities of a stamper\n\nAs a stamper, you should:\n\n1. Review the PR to your usual standards, even if it's a request for a \"quick stamp.\"\n2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.\n3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:\n    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or\n    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.\n\nRemember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.\n\n### The GitHub \"stampers\" team\n\nThe GitHub \"stampers\" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the \"stampers\" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.\n\nTo join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.\n\n## 5. Cody-related PRs\n\nCody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we've decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.\n\nWhat you as an engineer need to do:\n\n- Remember that it may not always be clear-cut what \"Cody-related\" means. Use your best judgment.\n- For the same reason, this process can't be easily automated. \u2192 There is unfortunately no reminder to add the label.\n- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)\n- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.\n- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it's an OSS contribution, add the label yourself.\n- **Think QA**: We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:17:28

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:17:28

I've made the "stay focused on the goal" item more concise to align better with the length of the other points. Let me know if there's anything else you'd like me to adjust.

### User - 2024-10-15 16:17:54

Consider simplifying this introduction by focusing on actionable language, e.g., 'Follow these steps to create a PR that is easy to review.'

### Assistant - 2024-10-15 16:17:58

{
  "updates": [
    {
      "pattern": "To create a PR that is easy to review and fosters a positive collaboration with your code reviewer, follow these guidelines:",
      "replacement": "Follow these steps to create a PR that is easy to review:"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:17:58

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:17:58

I've simplified the introduction to focus on actionable language as suggested. Let me know if there's anything else you'd like to adjust.

### User - 2024-10-15 16:18:15

Update the draft to this:
# Pull requests

This guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:

1. [How to create a PR](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)
2. [How to make the PR easy to review](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)
3. [How to review PRs](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)
4. [What "quick stamp"s mean](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)
5. [Cody-related PRs](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)

## 1. How to create a PR

This section defines guidelines for PRs.

- **Branch naming**
    - Convention: `initials/description`
    - Example: `aa/replace-button-title`
- **PR names:** To make it easier to skim commit history, name the PR with
    - Convention: `team: short but precise description of the change`
    - Example: `search: update repo filter to be faster`
- **Team labels:** Apply a team label to the PR so that the associated team can easily find PRs.
    - Example: `team/search`
- **Link the PR and the issue:** Provides context for for future readers.
    - If the PR is a result of a GitHub issue, include “Closes #12345” in the PR’s description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).
    - If the PR is a result of a Linear issue, you must enable linking from the issue. You can either:
        - Autolink: Click the first indicated icon and say “Closes <issueID>” in the PR description
        - Magic branch: Click the second indicated icon which will create a magic branch name which handles autolinking.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7ce844a-fe2e-4102-b77e-e852aee3841b/9899895f-f3da-45f6-86ed-b4628b67dc23/image.png)
    
- **Approvals:** Defer merging a PR until at least one person has approved of the changes.

Suggested but not required:

- **Visual changes:** If the PR makes a visual change to the UI (ex: changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.
- **Self-assignment:** Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.

Further reading:

- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)

## 2. How to make the PR easy to review

Follow these steps to create a PR that is easy to review:

1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.
    1. You can take advantage of the “draft” mode for previewing and self-checking, and mark it ready for review once it’s ready.
2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.
3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.
4. **Choose 1 or 2 targeted reviewers:** Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. 
5. **Stay focused on the goal**: Keep changes focused on the specific goal. Small, unrelated cleanups are acceptable if they add value and don't complicate the review.
6. **Optimize for reviewers:** Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.
7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.
8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.
9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., "What changes would be helpful?"
10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.
11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.
12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.

By following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.

### Choosing reviewers

- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.
- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.
- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.
- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge.

## 3. How to review PRs

### Checklist of things to look for

1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).
2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or "future-proofing".
3. **Review tests**: Ensure tests are adequate and appropriate.
4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.
5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.
6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.
7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).
8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.
9. **Dependencies**: Review any new dependencies and ensure they are appropriate.
10. **Security**: Check for potential security issues.
11. **Performance**: Consider potential performance issues and their impact.
12. @Joe Chen Backwards compatible?

### Soft skills around code reviews

Reviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.

1. Prioritize code reviews
    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.
2. Be mindful of your communication
    - Use "**we**" instead of "you" when discussing code changes.
    - Make **polite requests** instead of commands, e.g., "Could we...?"
    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.
3. Focus on improvement and learning
    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.
    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.
4. Handle bugs and large PRs appropriately
    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.
    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.
5. Offer sincere praise and positive feedback
    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.
6. Resolve conflicts and stalemates
    - Accept the PR if only minor or optional changes remain.
    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.

Following these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.

## 4. What "quick stamp"s mean

"Quick stamp" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A "quick stamp" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.

### Expectations and responsibilities of a stamper

As a stamper, you should:

1. Review the PR to your usual standards, even if it's a request for a "quick stamp."
2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.
3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:
    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or
    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.

Remember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.

### The GitHub "stampers" team

The GitHub "stampers" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the "stampers" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.

To join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.

## 5. Cody-related PRs

Cody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we’ve decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.

What you as an engineer need to do:

- Remember that it may not always be clear-cut what “Cody-related” means. Use your best judgment.
- For the same reason, this process can’t be easily automated. → There is unfortunately no reminder to add the label.
- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)
- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.
- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it’s an OSS contribution, add the label yourself.
- **Think QA:** We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product.

### Assistant - 2024-10-15 16:18:51

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "# Pull requests\n\nThis guide will walk you through the process of creating, reviewing, and approving pull requests (PRs). It covers the following topics:\n\n1. [How to create a PR](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)\n2. [How to make the PR easy to review](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)\n3. [How to review PRs](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)\n4. [What \"quick stamp\"s mean](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)\n5. [Cody-related PRs](https://www.notion.so/Pull-Requests-65ca2cf90370449485fa747fbad1c05c?pvs=21)\n\n## 1. How to create a PR\n\nThis section defines guidelines for PRs.\n\n- **Branch naming**\n    - Convention: `initials/description`\n    - Example: `aa/replace-button-title`\n- **PR names:** To make it easier to skim commit history, name the PR with\n    - Convention: `team: short but precise description of the change`\n    - Example: `search: update repo filter to be faster`\n- **Team labels:** Apply a team label to the PR so that the associated team can easily find PRs.\n    - Example: `team/search`\n- **Link the PR and the issue:** Provides context for for future readers.\n    - If the PR is a result of a GitHub issue, include \"Closes #12345\" in the PR's description in order to [auto-close the related issue once the PR is merged](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).\n    - If the PR is a result of a Linear issue, you must enable linking from the issue. You can either:\n        - Autolink: Click the first indicated icon and say \"Closes <issueID>\" in the PR description\n        - Magic branch: Click the second indicated icon which will create a magic branch name which handles autolinking.\n    \n    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7ce844a-fe2e-4102-b77e-e852aee3841b/9899895f-f3da-45f6-86ed-b4628b67dc23/image.png)\n    \n- **Approvals:** Defer merging a PR until at least one person has approved of the changes.\n\nSuggested but not required:\n\n- **Visual changes:** If the PR makes a visual change to the UI (ex: changing the text of a button), include a screenshot or a video of it in the PR so that a reviewer knows exactly where to focus when looking at the change.\n- **Self-assignment:** Assign the PR to yourself so it is easier to find from search and also easy to switch assignee if need be.\n\nFurther reading:\n\n- [Atlassian's PR guide](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)\n\n## 2. How to make the PR easy to review\n\nFollow these steps to create a PR that is easy to review:\n\n1. **Review your own code before requesting a review**: Double-check your work and ensure it is ready for review.\n    1. You can take advantage of the \"draft\" mode for previewing and self-checking, and mark it ready for review once it's ready.\n2. **Provide a clear PR description**: In the PR description, explain *what* you did and *why* on a high level.\n3. **Document your code**: Answer questions within the code itself so that it's documented for future reference.\n4. **Choose 1 or 2 targeted reviewers**: Ensure the relevant people are reviewing your code. By keeping the number of reviewers small, you are more likely to get a faster turnaround time on a review. More on choosing reviewers below. \n5. **Stay focused on the goal**: Keep changes focused on the specific goal. Small, unrelated cleanups are acceptable if they add value and don't complicate the review.\n6. **Optimize for reviewers**: Consider breaking out very large PRs into smaller ones if they're still making sense when reviewed individually.\n7. **Communicate proactively**: Be proactive in your communication with the reviewer, providing necessary context and updates.\n8. **Clarify your code when needed**: If the reviewer misunderstands something, consider improving the code to make it clearer and more obvious.\n9. **Seek clarification on terse feedback**: If you receive brief or unclear feedback, ask the reviewer for more information, e.g., \"What changes would be helpful?\"\n10. **Be open to alternate solutions**: When presented with an equally good solution, be open to implementing it the reviewer's way, as they may have valuable insights.\n11. **Minimize lag between review rounds**: Respond to feedback promptly to minimize the time the reviewer spends restoring context.\n12. **Express gratitude for feedback**: Thank your reviewer for their feedback and suggestions.\n\nBy following these guidelines, you'll create a PR that is easy to review, fostering a collaborative and efficient code review process.\n\n### Choosing reviewers\n\n- **Select reviewers early**: At the start of a project, identify 1-2 designated reviewers who are within approximately 3 hours of your working hours. Preferably, choose teammates, but if not feasible, look for someone outside the team with appropriate context.\n- **Provide context**: Introduce the designated reviewers to the project. Share the relevant Linear project and meet with them to discuss the goals and approach. This upfront effort helps reduce review delays and builds long-term understanding.\n- **Prioritize team involvement**: While it's okay to seek external reviews to unlock progress, make sure your team members also review the code, even if post-merge. This maintains shared ownership, increases the team's overall bus factor, and ensures team members can provide future support.\n- **Depth of review matters**: Reviewers outside the team may help with general aspects of the code, but team members are often better equipped to catch nuanced issues, like performance optimizations or potential exploits, that require deeper subsystem knowledge.\n\n## 3. How to review PRs\n\n### Checklist of things to look for\n\n1. **High-level design and functionality**: Assess if the design fits within the architecture. Evaluate the functionality and ensure it works as expected, handling edge cases. Request a demo from the developer if needed (e.g., for UI changes).\n2. **Code examination**: Check for readable and maintainable code, avoiding overengineering or \"future-proofing\".\n3. **Review tests**: Ensure tests are adequate and appropriate.\n4. **Naming, style, and comments**: Verify naming and style against common code standards and conventions. Review comments for clarity and relevance.\n5. **Documentation**: Confirm related docs are updated if they are affected by the code changes.\n6. **Code understanding**: Comprehend what each line of code does and ask the developer for clarification if needed.\n7. **Code style**: Most code style checking is automated, but not everything can be. Ensure the code adheres to proper style guidelines, including idiomatic code organization and [writing style](../../../../company-info-and-process/communication/content_guidelines/style_and_mechanics.html).\n8. **Customer-facing labels and messages**: Verify new or modified labels or messages are appropriate, consistent, and follow our style guide.\n9. **Dependencies**: Review any new dependencies and ensure they are appropriate.\n10. **Security**: Check for potential security issues.\n11. **Performance**: Consider potential performance issues and their impact.\n12. **Backward compatibility**: Ensure changes are backward compatible if required.\n\n### Soft skills around code reviews\n\nReviewing PRs is not only a technical process but also a social one. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process.\n\n1. **Prioritize code reviews**\n    - Treat code reviews as a **high priority** task and aim to complete them within one day. It makes for a great culture and is a nice experience for everyone when PRs are reviewed quickly.\n2. **Be mindful of your communication**\n    - Use \"**we**\" instead of \"you\" when discussing code changes.\n    - Make **polite requests** instead of commands, e.g., \"Could we...?\"\n    - **Explain** the reasoning behind your suggestions, ideally tying them to objective principles.\n3. **Focus on improvement and learning**\n    - Aim to bring the code up **a letter grade or two**, helping your colleagues improve over time, rather than giving a list of twenty things to improve. Even if each of your points are valid, it can be overwhelming to receive a long list of suggestions.\n    - If you notice **repeated mistakes**, point out one instance and encourage the developer to look for more occurrences.\n4. **Handle bugs and large PRs appropriately**\n    - Avoid asking the author to fix bugs unrelated to their changes, even if they are nearby. Address significant bugs **separately** or in a different PR.\n    - Encourage **breaking up** large PRs into smaller, more manageable chunks, ideally fewer than 400 lines.\n5. **Offer sincere praise and positive feedback**\n    - Recognize and highlight good work, rather than only pointing out mistakes. It feels good to be appreciated, and it encourages people to keep doing good work.\n6. **Resolve conflicts and stalemates**\n    - Accept the PR if only minor or optional changes remain.\n    - Address disagreements by talking, retreating, or escalating, and then resolve any interpersonal conflict.\n\nFollowing these guidelines will help you create a friendly, efficient, and effective code review process that benefits both you and your team.\n\n## 4. What \"quick stamp\"s mean\n\n\"Quick stamp\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve. However, it is essential to understand that it is not a request for a blind approval. A \"quick stamp\" should never mean bypassing your review standards or blindly approving a PR without understanding the changes.\n\n### Expectations and responsibilities of a stamper\n\nAs a stamper, you should:\n\n1. Review the PR to your usual standards, even if it's a request for a \"quick stamp.\"\n2. Feel free to approve trivial changes, like fixing typos, documentation updates, or reverts.\n3. Use your judgment to determine if you have enough context and confidence to approve the PR. If you lack context or do not feel confident, practice caution and either:\n    - a.) Wait for someone more knowledgeable in the specific area to review the PR, or\n    - b.) Inform the requester that you cannot stamp the PR right away and that you can review it thoroughly when there's time.\n\nRemember, no one should ever blindly approve a PR. It is always up to the reviewer to maintain their review standards and ensure the changes are appropriate.\n\n### The GitHub \"stampers\" team\n\nThe GitHub \"stampers\" team is a group of reviewers who can be reached for reviewing PRs across multiple time zones. This team is particularly helpful when you need a review urgently, for example, when fixing the main branch early in the morning. By being part of the \"stampers\" team, you are not only helping to ensure smooth and efficient PR approvals but also fostering a culture of thorough and responsible reviewing.\n\nTo join the stampers, drop a message on #discuss-engineering or #team-engineering, and someone will add you.\n\n## 5. Cody-related PRs\n\nCody-related PRs are a bit special because we want to release Cody often, without breaking our Search product. For a near-term solution, we've decided to tag each Cody-related PR with either `backport 5.0` or `confirm-no-backport`.\n\nWhat you as an engineer need to do:\n\n- Remember that it may not always be clear-cut what \"Cody-related\" means. Use your best judgment.\n- For the same reason, this process can't be easily automated. \u2192 There is unfortunately no reminder to add the label.\n- When creating a PR, **assign one of the labels**. (Forgot it? You can do it even after merging. Unsure which one to add? Ask around for opinions.)\n- If your PR is labeled for backporting, **backport soon** after merging, to catch the next patch.\n- If you see a Cody-related PR without a label, **send a friendly ping** to the author. If it's an OSS contribution, add the label yourself.\n- **Think QA**: We switched from a monthly release cadence to quarterly + biweekly patches to improve the quality of our search product. With the above-suggested process, Cody kind of abuses patch releases. Be mindful of this, and in your PRs, be conservative if you see that your changes could interfere with the main product."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:18:51

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:18:51

I've updated the document as per your new draft. Let me know if there's anything else you'd like to modify or further refine.

### User - 2024-10-15 16:19:01

Consider shortening to 'Reviewing PRs is both technical and social. Follow these guidelines for an efficient, friendly process.'

### Assistant - 2024-10-15 16:19:07

{
  "updates": [
    {
      "pattern": "Reviewing PRs is not only a technical process but also a social one\\. When reviewing PRs, keep in mind the following guidelines to ensure a thorough, efficient, but also friendly review process\\.",
      "replacement": "Reviewing PRs is both technical and social. Follow these guidelines for an efficient, friendly process."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:19:07

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:19:07

I've shortened the introduction as requested. Let me know if there's anything else you'd like me to adjust.

### User - 2024-10-15 16:19:29

Clarify that minor or optional changes can be accepted to avoid blocking the PR unnecessarily.

### Assistant - 2024-10-15 16:19:34

{
  "updates": [
    {
      "pattern": "\\*\\*Resolve conflicts and stalemates\\*\\*\\n\\s+- Accept the PR if only minor or optional changes remain\\.",
      "replacement": "**Resolve conflicts and stalemates**\n    - Accept the PR if only minor or optional changes remain to avoid blocking the PR unnecessarily."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:19:34

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:19:34

I've clarified that minor or optional changes can be accepted to avoid blocking the PR unnecessarily. Let me know if there's anything else you'd like me to adjust.

### User - 2024-10-15 16:20:23

Consider simplifying to 'A "quick stamp" is a request for reviewing trivial changes. It should not bypass standard review practices.'

### Assistant - 2024-10-15 16:20:28

{
  "updates": [
    {
      "pattern": "\\\"Quick stamp\\\" is a term used when requesting a review for a pull request that is likely to be trivial and easy to approve\\.",
      "replacement": "A \"quick stamp\" is a request for reviewing trivial changes. It should not bypass standard review practices."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-15 16:20:28

{"result": "Successfully updated text document with textdoc_id '670ef4f2ac14819194224a4b150da765'", "textdoc_id": "670ef4f2ac14819194224a4b150da765"}

### Assistant - 2024-10-15 16:20:28

I've simplified the description of "quick stamp" as requested. Let me know if there's anything else you'd like to modify.

