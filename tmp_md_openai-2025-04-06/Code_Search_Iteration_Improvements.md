# Code Search Iteration Improvements

Created: 2023-11-03 12:27:12
Last Updated: 2023-11-03 12:29:37

### User - 2023-11-03 12:27:12

Give a list of suggestions for ways this can be made more clear and concise

The core search functionality of Code Search has not seen much investment in the last 1-2 years. As part of planning in Q4 2023, the Search Suite team has chosen to invest in key parts of the core search workflow. The goal is to make Code Search lovable, i.e., improve Code Search, especially the core search flows, so that every pro dev uses and loves it. The approach to doing this is to iteratively make improvements that grow key metrics, especially DAU and DAU/MAU%. 
A secondary problem is that to improve quality of features when they are released, Product encourages the use of early access program (EAP) features for initial validation and testing before we turn them on more broadly. EAP feedback is meant to help shape the requirements and find issues. The idea is that we release a feature as EAP, work with handpicked customers to enable it, get feedback, make improvements, repeat as needed, and then finally release it more broadly.
Both of these development models benefit from being able to get changes to customers more quickly. Otherwise, we are limited to one iteration per quarter which means that it can take several quarters to get a feature released, even if it requires minimal changes based on the feedback. 
Our current recommended solution for iterating more quickly has been to abuse the biweekly patch releases. This recommendation came out of Cody development, but it is applicable to anything that is part of the main Sourcegraph deployment. The advantages of patch releases is that they are visible to customers and cut on a regular basis. The disadvantage of patch releases are that they are meant to be incremental and so should not include changes which have large user interface changes or introduce technical risk. 
This mostly works for EAP features, which are designed to be shipped off by default, as long as the feature is implemented in a way that can be backported. However, for changes we want to be on by default, especially ones that cause significant visible changes to the user experience, abusing the patch releases is not a viable solution. 
We have longer term solutions in progress. However, they will not be available for the Code Search until ???. Thus, we want to explore the feasibility of an intermediate solution.
Constraints of an intermediate solution:
Should solve the primary problem of faster iteration for on-by-default search workflow improvements. 
May also improve the iteration cycle for EAP features.
“May” because patch releases are closer to good enough for EAP
Should not assume that most self-hosted customers will upgrade more frequently than the ~quarterly marketing releases.
May assume that the handpicked customers for an EAP solution will be willing to upgrade.
Should allow us to collect data from real enterprise customer instances.
May limit that data to a subset of customers, e.g., Cloud.
Should allow us to ship backwards incompatible changes (e.g., to the UI or search language) that are on by default
Should not support an unsustainable amount of work or delay our longer term solutions by too much
But “unsustainable” and “too much” are open to negotiation 


### Assistant - 2023-11-03 12:27:28

Here is a revised and more concise version:

---

**Improving Code Search Clarity and Efficiency**

1. **Current State:**
   - Code Search's core functionality has been stagnant for 1-2 years.

2. **Immediate Plan:**
   - The Search Suite team will enhance core search workflows in Q4 2023, aiming to make Code Search a tool that every professional developer relies on and enjoys.

3. **Strategy:**
   - Incremental improvements to boost daily active users (DAU) and the DAU to monthly active users (DAU/MAU) ratio.

4. **Quality Enhancement:**
   - An early access program (EAP) will be used for feature validation and iterative refinement, based on customer feedback, before wider release.

5. **Iteration Speed:**
   - Accelerating delivery to customers is crucial. Currently, updates are limited to quarterly releases, which delays feature availability.

6. **Current Iteration Practice:**
   - Biweekly patch releases, which are fast but should not include major changes, are being misused for rapid iteration.

7. **Issue:**
   - Patch releases are unsuitable for significant, default-on changes due to the risk involved.

8. **Long-term Solutions:**
   - In development, but not ready for immediate deployment to Code Search.

9. **Seeking an Interim Solution:**
   - Aim: Quicker iteration for default-on search improvements without overburdening the team or hindering long-term solutions.

10. **Constraints for the Interim Solution:**
    - Must expedite iteration for core search updates.
    - Could also benefit EAP iterations.
    - Cannot expect most customers to update more frequently than the current quarterly cycle.
    - Assumes EAP participants are willing to update more regularly.
    - Must facilitate data collection from enterprise customer instances.
    - Allows for shipping default-on, backwards incompatible changes.
    - Must be sustainable and not excessively delay long-term solutions.

*Note: The interim solution's feasibility is under exploration, specifics to be determined.*

### User - 2023-11-03 12:29:15

Instead of giving an updated version, give a list of improvements I can make. A list of feedback. A list of critiques. 

### Assistant - 2023-11-03 12:29:37

Certainly! Here's a list of critiques and improvements that can be made to the original text to enhance clarity and conciseness:

1. **Eliminate Redundancies:**
   - Avoid repetitive phrases like "improve Code Search, especially the core search flows," which can be condensed to "improve core search flows."

2. **Define Acronyms Once:**
   - When you first mention an acronym (DAU, MAU, EAP), define it. Afterward, just use the acronym.

3. **Consolidate Points:**
   - Combine related points to avoid scattering similar content throughout the text. For example, group all mentions of the EAP's purpose and process together.

4. **Use Active Voice:**
   - Prefer active voice over passive for direct and clear communication. For instance, "The team has chosen to invest" can become "The team will invest."

5. **Simplify Language:**
   - Replace complex phrases with simpler terms. For example, "The core search functionality of Code Search has not seen much investment" could be "Code Search's core functionality has lacked investment."

6. **Streamline Details:**
   - Only include details that add value to the understanding of the main points. For instance, the detailed explanation of the patch releases' pros and cons could be summarized if it doesn't directly contribute to the core message.

7. **Clarify Goals and Actions:**
   - Clearly differentiate between immediate goals, planned actions, and long-term strategies without mixing them up.

8. **Prioritize Information:**
   - Place the most critical information at the beginning of each section to capture attention and ensure understanding.

9. **Focus on the Solution:**
   - Shift the focus more towards the proposed solutions rather than extensively describing the problems.

10. **Specify Timeframes:**
    - Avoid vague terms like "in the last 1-2 years." If it's significant, specify the exact timeframe.

11. **Direct Address of Problems:**
    - State problems directly and follow immediately with how you intend to address them, which streamlines the flow of information.

12. **Avoid Jargon:**
    - Limit the use of jargon to what's necessary for the audience. If this is for a broader audience, further simplify technical terms.

13. **Set Clear Constraints:**
    - When listing constraints, avoid ambiguous phrases like “closer to good enough” and quantify what "too much" delay means.

14. **Provide Clear Deadlines and Milestones:**
    - Replace placeholders like "???" with actual deadlines, milestones, or an acknowledgment that these are to be determined.

15. **Concise Summarization:**
    - The summary should encapsulate the main point without extra details — think of it as an executive summary.

By addressing these points, the text can be made more straightforward, actionable, and easier to grasp for the intended audience.

