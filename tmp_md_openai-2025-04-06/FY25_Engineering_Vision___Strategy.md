# FY25 Engineering Vision & Strategy

Created: 2024-01-15 14:36:10
Last Updated: 2024-01-15 15:37:17

### User - 2024-01-15 14:36:10

Here are a bunch of raw notes thinking about an engineering strategy doc. Draft the engineering strategy doc. 

FY25 Eng Vision and Strategy
Author: Erika Rice Scherpelz
Date: 2024-01-15
Status: WIP

Goal
This document aims to define an engineering vision and strategy for FY25. This is complementary to the overall business strategy captured in the MSEM and the Product Strategy + Roadmap.
Vision 
Sourcegraph’s engineering teams are able to quickly deliver high quality product experiences on a foundation that balances velocity, maintainability, and operational overhead. 
Scratchpad

End of year message
I have been thinking about next year, and what we’ll need to do technically to scale to the success we are aiming for. 

The number one goal for our engineering teams is, always, to support our product goals. Yet to enable long term success, we also need to invest in a reliable and secure foundation. For next year, I’d love to see us increasing our operational maturity, improving our architecture, reducing our maintenance burden and costs, and increasing our ability to iterate quickly. 

I’m also excited to invest in enterprise readiness. Every feature we build should meet the bar of being ready to release to our largest customers. Maybe not on day one, but with a clear plan for investment. I am excited to work together with product, design, and GTM to set and meet a high bar. 

I think of this as “slimming down to scale up”. I want us to focus on building products and systems that are excellent, both technically and for the user. Although there will always be tradeoffs, I’m excited to look for win-win solutions which improve quality while also simplifying. 

How we make engineering decisions

Build for what we need, but build it well. As a company focused on innovation and still growing towards profitability, we don’t yet have a sustainable runway.


Slack notes
Source graph. Technical vision notes. Engineering's goal is to build systems that meet the needs of our users and are business. This includes fulfilling functional requirement and also includes building systems that allow us to develop quickly, deploy frequently and reliably, run system stably, and meet a quality bar for both functional, operational, and security needs that fulfills the requirements of our most stringent enterprise customers.
1:08
Themes for 2024 : support our product goals. Improve our operational efficiently, especially for our cloud managed instances but ideally for self-hosted customers and dotcom too. Reduce our maintenance burden to allow us to move more quickly. Invest in documentation and automation that allows more to be accomplished with the same number of people. Should capture the y of that. One aspect of it is delivering features, another is cost savings, another is that if we plan for success we need to be able to support many more customers, which requires moving to be lower touch.
1:09
Next question is how low of the level of detail do I want to get in this strategy? I think the teams should drive most of it, but I would like to be opinionated enough such that if the teams and leadership are aligned on the vision and strategy, then proposals that align with it will not be rejected. When we review plans. We might still argue priorities. There's a lot of different goals we want to achieve. But people will not be told that what they propose is not even relevant




Diagnosis 
We have two products that need to be more integrated but are currently technologically quite separate. 
Our product is scattered with partially finished features which have unclear ownership.
We want to continue to deliver new value to our customers while also delivering on the value we claim we already provide.
Our engineering org is small compared the surface area of customer support and code we need to maintain. 
The business needs us to increase usage and also reduce costs. 
Our current code base is slowing us down, not helping us move more quickly


Guiding policies
Wide audience, frequent use features
Better together
Deliver what we promise
Reduce maintenance burden, reduce cost to run, reduce operational overhead
Do it one way

Actions
Things we should do
Things we shouldn’t do



Evaluation criteria
From here
Many interesting properties only available through universal adoption (“we run our own hardware”)
Concentrate tooling investment onto smaller space (“we run in a mono repo”)
Reduce energy lost on conflict (“we are a product engineering company”)
Control your innovation budget (all three)
New hires, especially senior new hires, forced to engage explicitly with strategy rather than having option of ignoring it (all three)



### Assistant - 2024-01-15 14:36:45

# FY25 Engineering Vision and Strategy

**Author:** Erika Rice Scherpelz  
**Date:** 2024-01-15  
**Status:** Work in Progress (WIP)

## Goal

This document outlines the engineering vision and strategy for the fiscal year 2025 (FY25), in alignment with the overarching business strategy detailed in the MSEM and the Product Strategy + Roadmap. Our focus is to empower Sourcegraph’s engineering teams to swiftly deliver top-quality product experiences founded on a balance of speed, maintainability, and operational efficiency.

## Vision

Envisioning an environment where our engineering teams can rapidly create high-quality product experiences, we aim to establish a robust foundation that harmonizes velocity, maintainability, and operational overhead.

## Diagnosis

- **Product Integration Challenges:** Our two main products require greater integration but currently face technological separations.
- **Incomplete Feature Landscape:** Our product features scattered, partially completed works with ambiguous ownership.
- **Balancing Delivery and Maintenance:** The challenge is to continue delivering new customer value while fulfilling existing commitments.
- **Resource Constraints:** Our engineering organization is relatively small, given the extensive customer support requirements and the breadth of code maintenance.
- **Business Expectations:** There is a dual demand from the business side to increase usage while also cutting costs.
- **Codebase Hurdles:** Our current codebase is more of a barrier than an accelerator to our progress.

## Guiding Policies

- **Prioritizing Broad and Frequent Use Features:** Focus on features that cater to a wide audience and are used frequently.
- **Better Together Approach:** Emphasize integration and synergy among products and teams.
- **Delivering on Promises:** Commit to providing the full value of what we claim in our offerings.
- **Maintenance and Cost Efficiency:** Actively work towards reducing the maintenance burden, operational costs, and overhead.
- **Standardization of Processes:** Streamline processes by adopting a unified approach wherever feasible.

## Strategic Actions

### Things We Should Do

- **Enhance Operational Maturity:** Increase our focus on operational excellence, including architecture improvements, maintenance reduction, and cost optimization.
- **Prioritize Enterprise Readiness:** Ensure every feature is designed to meet the highest standards, suitable for our largest customers.
- **Seek Win-Win Solutions:** Aim for solutions that simultaneously elevate quality and simplify processes.
- **Invest in Documentation and Automation:** Leverage documentation and automation to amplify our capabilities without proportionally increasing our team size.

### Things We Shouldn’t Do

- **Overextend Beyond Needs:** Avoid building beyond immediate requirements but ensure what is built is of high quality.
- **Neglect Long-Term Foundations:** Refrain from sacrificing long-term reliability and security for short-term gains.

## Evaluation Criteria

- **Universal Adoption and Efficiency:** Assess the impact of strategies like running our own hardware and centralizing tool investments.
- **Conflict Reduction:** Focus on reducing internal conflicts by adhering to a clear product engineering identity.
- **Innovation Budget Control:** Manage and allocate our innovation resources effectively.
- **Engagement with Strategy:** Encourage new hires, especially at senior levels, to actively engage with and contribute to our strategic vision.

## Conclusion

Our engineering strategy for FY25 is designed to position Sourcegraph at the forefront of technological innovation, customer satisfaction, and operational excellence. By adhering to these principles and actions, we aim to scale our success and meet the evolving demands of our users and the market.

### User - 2024-01-15 15:30:12

Below is my current draft. Comment on ways to make it more clear, more concise, and more actionable. General stylistic or copy edit feedback is also welcome.

Draft:
Goal
This document aims to define an engineering vision and strategy for FY25. This is complementary to the overall business strategy captured in the MSEM and the Product Strategy + Roadmap.
Vision 
Sourcegraph’s engineering teams are able to quickly deliver high quality product experiences on a foundation that balances velocity with an efficient and secure foundation.
Where we are today
Challenges
This section defines some areas where we are falling short of this vision today:
Integration of Cody and Code Search: We have two products that need to be integrated but are currently technologically quite separate. 
E.g., our “better together” story at the moment is limited to searching over enterprise code base for providing chat context
Incomplete features: Our product is scattered with partially finished or unscaled features which have unclear ownership. This means that the experience our customers have often doesn’t match what we sell them, especially for large complex customers. 
E.g., Own, Packages, Code Monitoring, Code Insights, Executors, Perforce support, etc. 
High maintenance burden: Our engineering organization is small given the extensive customer support needs and breadth of code we maintain. 
E.g., the Platform teams and the Code Search team spend significant eng time debugging issues ranging from executor issues to slow code insights graphs to precise indexing failures to Perforce failures to bad licensing failure cases to…
Controlling our burn: We need to reduce operating costs of the systems we run. (Reducing operating costs for self-hosted customers is also a plus.)
E.g., running dotcom is a significant operational cost, many cloud customers are underwater (their revenue does not exceed their operating costs)
Legacy code base: Our current code base is slowing us down, not helping us move more quickly.
E.g., Packages make assumptions that make it hard to change Source’s code. We have multiple ways of implementing code navigation (Precise with compiler-based SCIP, search based, squirrel, tree-sitter). 
Strengths
We also have a number of strengths we can build on:
Better defined ownership: The move back to home teams and away from Job Fair has provided clarity around ownership. 
Responsive engineering team: Our engineers are highly responsive to the needs of our customers and to their fellow Sourcegraph teammates. 
Product guidance: Our product team has gotten stronger and is now providing much clearer direction for the engineering teams. 
Strong technical team: Our engineers bring strong technical expertise and collaborative skills. 
Guiding Policies
These guiding policies are meant to help align engineering decisions with our needs in FY25. While some of them are evergreen, others will shift over time. They are ordered. If you must make trade-offs between these policies, choose the ones higher up the list, but do so in a way that fulfills the rest as much as possible.
Support our business and product goals: The number one goal of our engineering team is to support Sourcegraph’s business and product goals, now and in the future.
Application: Utilize the product roadmap and quarterly guidance (e.g., for May) to determine where your team can add value.
Application: Find ways, at both the product and the infrastructure layer, to continue to reduce our operational costs. Where the first item is about accomplishing more with the same number of people, this item is focused on reducing our computational burden. 
Build for what we know we need, but build it well: There’s no point in investing in projects whose return on investment is many quarters out. However, that doesn’t mean building low quality software. We should only build as much as we know we need, but we should build it well. 
Application: When looking at a large project, divide it into pieces that are safe to pause after a quarter.
Application: Find ways to get iterative feedback on features, on a 1-month or faster cadence. 
Application: When you make short term compromises, understand how long it will take to pay them back. If the cost of the work around plus fixing it costs more than just doing it the right way, strongly bias toward just doing it the right way. If you can’t make sure that your leadership is committed to paying that extra cost. 
Reduce the burden: We need to reduce our maintenance burden as well as operational costs. We need to simplify our systems to do things one way, well, instead of doing them many different ways with hard to understand trade-offs. We need to slim down in the near term so that we can scale up to orders of magnitude more users over time. 
Application: Invest in architectural improvements, documentation, and automation so that we can move more quickly and accomplish more with the same number of people. 
Deliver what we claim: We can’t fix every problem, but we can find areas where the gap between what we say we’ve built and the customer experience in practice undermines trust. Let’s invest in fixing this gap.
Application: Every feature we build, both new and existing, should meet the bar of being ready to release to our largest customers, maybe not on day one, but with a clear plan for investment to get there. 



### Assistant - 2024-01-15 15:30:38

Your draft of the FY25 Engineering Vision and Strategy is comprehensive and covers key areas such as current challenges, strengths, and guiding policies. Here are some suggestions for making it more clear, concise, and actionable, along with stylistic and copy edit feedback:

### Clarity
- **Define Technical Terms:** Some terms like "Cody," "Code Search," "executor issues," or "SCIP" might not be universally understood. Consider adding brief explanations for such terms.
- **Consistent Formatting for Examples:** Present examples in a consistent manner. For instance, use bullet points or parentheses consistently to maintain a uniform structure.

### Conciseness
- **Eliminate Redundancies:** Phrases like "We need to simplify our systems to do things one way, well, instead of doing them many different ways with hard to understand trade-offs" could be shortened to "Simplify systems to adopt a unified, efficient approach, avoiding complex trade-offs."
- **Summarize Lengthy Sentences:** For example, "If you must make trade-offs between these policies, choose the ones higher up the list, but do so in a way that fulfills the rest as much as possible" could be "Prioritize higher-listed policies, balancing others as feasible."

### Actionability
- **Clear Action Items:** For each guiding policy, include specific, measurable actions. For instance, under "Reduce the burden," detail the exact architectural improvements or automation tools planned.
- **Timeline and Ownership:** Assign a timeline and responsible parties for each action item to ensure accountability and track progress.

### Stylistic and Copy Edit Feedback
- **Use Active Voice:** Shift from passive to active voice for more direct communication. E.g., "Our product team has gotten stronger and is now providing much clearer direction" to "Our strengthened product team now provides clearer direction."
- **Consistent Capitalization and Formatting:** Ensure consistent capitalization for key terms like 'Engineering', 'Product Goals', etc.
- **Headings and Subheadings:** Use headings and subheadings to break down the document into digestible sections. This enhances readability.

### Additional Suggestions
- **Include a Summary:** Start with an executive summary that gives a snapshot of the entire document.
- **Feedback Mechanism:** Encourage feedback on the strategy, demonstrating openness to evolve the strategy based on team input.

Overall, your draft is well-structured and informative. These suggestions aim to enhance its effectiveness in communicating the FY25 engineering vision and strategy.

### User - 2024-01-15 15:36:29

What are other ideas for guiding policies for an engineering organization. Try to be opinionated, not generic.

### Assistant - 2024-01-15 15:37:16

Creating guiding policies for an engineering organization requires a balance between being specific enough to guide meaningful action and broad enough to apply across various contexts and projects. Here are some opinionated ideas for guiding policies:

1. **Embrace and Drive Technological Innovation:** Prioritize the adoption and development of cutting-edge technologies and methodologies. This means not just keeping up with industry standards but actively seeking to set them. Encourage experimentation and allocate resources for R&D projects that may not have immediate returns but promise to keep the organization at the forefront of technological advancement.

2. **Quality as a Culture, Not a Checkpoint:** Embed quality assurance into every stage of the engineering process, not just as a final step. This involves code reviews, continuous integration, and a culture that sees quality as everyone's responsibility. Encourage engineers to take ownership of the entire lifecycle of the features they develop, from conception to deployment and maintenance.

3. **Customer-Centric Engineering:** Align engineering efforts closely with customer needs and feedback. This doesn’t mean just responding to what customers say they want, but also anticipating their needs and continuously evaluating how changes impact customer experience. This policy should translate into practices like regular user testing, customer feedback loops, and engineering involvement in customer interactions.

4. **Sustainability and Scalability First:** Design systems and solutions with sustainability and scalability in mind from the outset. This involves considering the long-term impact of code and architecture decisions, focusing on maintainable, extensible, and efficient designs. Reject quick fixes that compromise the future scalability and maintainability of the system.

5. **Data-Driven Decision Making:** Base engineering decisions on data and metrics rather than intuition or tradition. Encourage a culture where decisions, from small code changes to large architectural shifts, are supported by empirical evidence and performance metrics.

6. **Foster a Learning and Mentoring Culture:** Promote continuous learning and knowledge sharing within the team. Encourage team members to pursue professional development opportunities and to share their learnings with others. Implement formal mentorship programs and regular tech talks to foster a culture of growth and learning.

7. **Emphasize Collaboration and Communication:** Prioritize clear, open communication within the engineering team and with other departments. Promote a collaborative environment where cross-functional teams work together seamlessly. Encourage engineers to develop soft skills like effective communication and empathy, which are essential for collaborative work.

8. **Security as a Default:** Make security an integral part of the engineering process. This involves regular security training, integrating security checks into the development lifecycle, and adopting a proactive approach to security, rather than reactive.

9. **Prioritize Technical Debt Reduction:** Regularly allocate time and resources for addressing technical debt. This means not just fixing bugs, but refactoring code, updating outdated libraries, and improving documentation. Recognize that reducing technical debt is as important as new feature development.

10. **Autonomy with Accountability:** Empower teams with the autonomy to make decisions and take risks, but couple this with a strong sense of accountability. Encourage teams to own their projects entirely, making decisions that align with broader organizational goals, and hold them accountable for the outcomes.

Each of these policies is opinionated in that it takes a clear stance on how the engineering organization should operate, providing a strong framework to guide decision-making and cultural development.

