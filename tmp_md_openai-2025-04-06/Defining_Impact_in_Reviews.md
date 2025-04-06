# Defining Impact in Reviews

Created: 2023-09-19 14:20:24
Last Updated: 2023-09-19 14:20:24

### User - 2023-09-19 14:20:24

Define "impact" as it's currently used in a performance review process

### Assistant - 2023-09-19 14:21:04

"Impact" in the context of a performance review process typically refers to the measurable or observable effect an employee's work has on the organization, its goals, or its stakeholders. This concept can be broken down in a few ways:

1. **Quantitative Impact**: This can be measured in terms of numbers. For example, if an employee in a sales role brought in $1 million in revenue, that's a direct quantitative impact. Another example might be an IT professional who improves system efficiency, resulting in a 25% speed increase in processing tasks.

2. **Qualitative Impact**: This is more about the intangible effects of an employee's work. For instance, an employee might have introduced a new process that improved team morale or provided exceptional customer service that enhanced the company's reputation.

3. **Scope of Impact**: This can vary from local (affecting a team or department) to global (affecting the entire organization or beyond). An employee might make a change that improves the workflow of their immediate team (local impact) or introduce a new company-wide initiative that transforms the business (global impact).

4. **Duration of Impact**: Some impacts are short-lived, while others have long-term consequences. A marketing campaign that boosts sales for a month has a different duration of impact than a new product line that provides sustained revenue for years.

5. **Direct vs. Indirect Impact**: An employee might have a direct impact by achieving something themselves, or they might have an indirect impact by enabling or supporting others to achieve results.

In a performance review, discussing an employee's impact is a way to recognize and evaluate their contributions to the organization. It's not just about tasks completed; it's about the ripple effects of those tasks and how they align with the company's objectives. Evaluating impact can help determine promotions, raises, bonuses, and other career development opportunities.

### User - 2023-09-24 13:10:16

For software engineers, the impact of their work on the business is a trailing indicator because software needs to be deployed and adopted before it has impact. This problem is exacerbated when software is released quarterly.

However, most performance review cycles only look at work done within the period being evaluated, e.g. the last 6 months.

How can a company that wants to assess people primarily on impact fairly evaluate people and incentivize projects longer than the review cycle given these constraints?

### Assistant - 2023-09-24 13:10:40

Addressing the misalignment between the timeframe of performance reviews and the delayed impact of software engineering projects requires a holistic approach. Here are some strategies that companies can adopt:

1. **Track and Attribute Past Projects**: During a review cycle, not only should current projects be assessed, but the impact of projects from previous cycles should be evaluated as well. This way, if a project from a prior period is now showing significant impact, that can be attributed to the engineers involved.

2. **Set Clear Expectations**: If the company is adopting a long-term perspective on projects, it's crucial to communicate this to employees. Engineers should know that the real value of their work might not be realized immediately but will be recognized eventually.

3. **Use Leading Indicators**: While the actual business impact (e.g., user adoption, revenue increase) is a trailing indicator, there are leading indicators that can suggest potential success. These might include code quality, the potential market size for a feature, or positive feedback during user testing.

4. **Milestone-Based Evaluation**: Instead of focusing solely on the final impact, break down projects into milestones. Recognize and reward employees for reaching these milestones, even if the full impact of the project isn't realized by the end of the review period.

5. **Feedback from Cross-Functional Teams**: Software doesn't operate in a vacuum. Getting feedback from teams like sales, marketing, and customer support can provide insights into the potential and actual impact of a feature or project.

6. **Encourage Documentation**: Engineers should be encouraged to document not just their code, but also their decision-making processes, challenges faced, and the potential business impact they foresee. This can provide valuable context during reviews.

7. **Long-Term Incentives**: Consider implementing long-term incentives, like stock options or bonuses that vest after a certain period, to reward sustained impact. This can motivate engineers to think long-term and align their incentives with the company's.

8. **Regular Check-ins**: Instead of waiting for formal review periods, have regular check-ins (e.g., monthly or quarterly) where progress and potential impact are discussed. This provides opportunities for course correction and continuous feedback.

9. **Foster a Long-Term Mindset**: Create a company culture that values long-term gains over short-term wins. This can be reinforced through leadership communication, training, and the stories and achievements that are celebrated within the company.

10. **Rethink Review Cycles**: If possible, consider adjusting the review cycles themselves. For instance, having a more frequent lightweight review combined with a comprehensive annual review might allow for a better assessment of both immediate contributions and long-term impact.

By adopting these strategies, companies can better align their performance review process with the often delayed impact of software engineering projects, ensuring that engineers are fairly evaluated and incentivized for their contributions.

### User - 2023-09-24 13:12:04

What are concrete ways software engineering departments can track and attribute past projects?

### Assistant - 2023-09-24 13:12:29

Tracking and attributing past projects effectively requires a combination of tools, processes, and cultural practices. Here are some concrete ways software engineering departments can achieve this:

1. **Version Control Annotations**: Utilize version control systems like Git. Every commit has an author, allowing for easy tracking of who contributed to what. Git blame, for instance, shows line-by-line authorship of a file.

2. **Project Management Tools**: Platforms like Jira, Trello, or Asana can help track tasks and user stories. By ensuring that each task is assigned to an individual or team and linking tasks to larger project goals, you can trace back contributions.

3. **Documentation**: Encourage engineers to document their projects, including design decisions, challenges faced, and expected outcomes. Over time, this documentation can serve as a historical record, making it easier to attribute impact.

4. **Post-Deployment Reviews**: Regularly schedule reviews after a project has been live for a certain duration (e.g., 3 or 6 months). Assess the actual impact versus the projected impact and attribute successes and learnings to the involved team members.

5. **Feedback Loop with Business Teams**: Establish a feedback mechanism with sales, customer support, and marketing teams. They can provide insights into how new features or changes are being received by users, helping in attributing impact.

6. **Changelogs**: Maintain detailed changelogs for each release. This not only helps in tracking changes but can also serve as a record for attributing features or fixes to specific engineers or teams.

7. **Internal Wikis or Databases**: Create a centralized location where project details, contributors, timelines, and outcomes are recorded. Platforms like Confluence or Notion can be useful for this purpose.

8. **Automated Impact Metrics**: Implement automated tools to measure the impact of features or changes. For instance, if a performance improvement is expected from a change, have metrics in place to automatically track and report the improvement after deployment.

9. **Regular Retrospectives**: After a project's completion, hold retrospective meetings where the team discusses what went well, what could be improved, and the impact of their work. Document these discussions for future reference.

10. **Mentorship and Pair Programming**: Encourage experienced engineers to mentor newer team members. This not only helps in skill development but also ensures that knowledge about past projects is passed down.

11. **Recognition Programs**: Implement programs where team members can nominate their peers for significant contributions to past projects. This not only helps in attribution but also fosters a positive culture of recognition.

12. **Archived Communication**: Use communication tools like Slack or Microsoft Teams, where discussions are archived. Over time, these threads can serve as a record of who worked on what, especially if the team is diligent about discussing projects and decisions in dedicated channels.

13. **Surveys and Feedback**: Occasionally survey team members about past projects, asking for their insights on long-term impact, unexpected outcomes, and contributions that might have been overlooked in initial evaluations.

By implementing a combination of these methods and ensuring that they are consistently practiced, software engineering departments can effectively track and attribute past projects, ensuring that contributions are recognized even if their impact becomes apparent much later.

### User - 2023-09-24 13:13:21

Give a set of evaluative questions to ask in post deployment reviews. List data that should be collected in advance of such a review. 

### Assistant - 2023-09-24 13:13:50

Certainly! Post-deployment reviews, often known as "post-mortems" or "retrospectives" in the tech world, are essential for continuous improvement. Here are some evaluative questions and the data that should be collected:

### Evaluative Questions:
1. **Impact & Results**:
   - What was the intended outcome of this deployment, and did we achieve it?
   - Were there any unexpected benefits or side effects?

2. **Performance Metrics**:
   - How did system performance change post-deployment?
   - Were there any performance regressions?

3. **Quality & Reliability**:
   - Were there any critical bugs or issues post-deployment?
   - How quickly were we able to identify and rectify these issues?

4. **Adoption & Usage**:
   - How quickly did users adopt the new features or changes?
   - What feedback have we received from users regarding the deployment?

5. **Process & Execution**:
   - Were there any challenges or hiccups during the deployment process?
   - Were there deviations from the deployment plan? If so, why?

6. **Communication & Collaboration**:
   - How effectively did teams communicate during the deployment?
   - Were all relevant stakeholders kept informed?

7. **Lessons Learned**:
   - What went particularly well that we should replicate in future deployments?
   - What challenges did we face, and how can we mitigate them in the future?

8. **Documentation & Training**:
   - Was the documentation updated promptly and accurately post-deployment?
   - Did the team receive adequate training or knowledge transfer for the changes?

9. **Resource Utilization**:
   - Did we utilize resources (human, computational, financial) efficiently?
   - Were there any resource bottlenecks or wastages?

### Data to Collect in Advance:

1. **Performance Data**:
   - Baseline performance metrics (before deployment).
   - Post-deployment performance metrics.

2. **Error & Issue Tracking**:
   - Logs of errors or issues reported post-deployment.
   - Time taken to resolve these issues.

3. **Usage & Adoption Metrics**:
   - User activity data before and after deployment.
   - Feedback or surveys from users regarding the new features or changes.

4. **Deployment Logs**:
   - Detailed logs of the deployment process.
   - Timestamps of each stage of deployment.

5. **Resource Utilization Data**:
   - Metrics on server load, bandwidth usage, and other computational resources.
   - Man-hours spent on the deployment.

6. **Communication Records**:
   - Logs or records of communications, especially if there were incidents or challenges.
   - Feedback from stakeholders or teams involved in the deployment.

7. **Documentation Updates**:
   - A record of documentation changes or updates post-deployment.
   - Feedback from team members on the adequacy and clarity of documentation.

By preparing with the right data and asking these evaluative questions, teams can gain valuable insights from their post-deployment reviews, leading to improved processes and outcomes in future deployments.

### User - 2023-09-24 19:18:39

How else might you assess long term impact in performance reviews? Focus on business impact

### Assistant - 2023-09-24 19:19:09

Assessing long-term business impact in performance reviews requires a broader perspective that extends beyond immediate deliverables and outcomes. Here are some approaches and considerations for evaluating long-term business impact:

1. **Revenue and Profitability Metrics**:
   - Did the individual's work contribute to sustained revenue growth or profitability over time?
   - Did they introduce or work on features/products that became major revenue drivers?

2. **Customer Retention and Satisfaction**:
   - Did the individual's contributions lead to increased customer retention or loyalty?
   - Were there significant improvements in customer satisfaction scores or Net Promoter Score (NPS) linked to their work?

3. **Market Share and Expansion**:
   - Did the individual play a role in products or initiatives that helped the company capture a larger market share or enter new markets?

4. **Operational Efficiency**:
   - Did the individual introduce tools, processes, or methodologies that resulted in long-term operational savings or efficiency gains?

5. **Innovation and Thought Leadership**:
   - Has the individual proposed or implemented ideas that positioned the company as a leader or innovator in its field?

6. **Strategic Partnerships and Relationships**:
   - Has the individual fostered relationships or partnerships that have brought long-term benefits to the company?

7. **Scalability and Sustainability**:
   - Did the individual contribute to projects or initiatives that enhanced the scalability of products or services?
   - Have they introduced sustainable practices or solutions that benefit the company in the long run?

8. **Team Growth and Leadership**:
   - Has the individual mentored or developed team members who've become key contributors?
   - Did they establish or contribute to practices that improved team cohesion, productivity, or morale over the long term?

9. **Risk Management**:
   - Has the individual identified and mitigated significant risks that could have had long-term negative effects on the business?

10. **Long-Term Vision Alignment**:
   - How well have the individual's contributions aligned with the company's long-term goals and vision?
   - Have they shown foresight in preparing the company for future challenges or opportunities?

11. **Cultural and Brand Impact**:
   - Has the individual played a role in shaping the company culture in a positive way?
   - Have their actions or contributions positively influenced the company's brand and reputation over the long term?

12. **Feedback from Cross-Functional Teams**:
   - Seek feedback from teams across the organization to understand the ripple effects of an individual's contributions. Often, the long-term impact is felt in areas that might not be immediately obvious.

To accurately assess long-term business impact, it's essential to have systems in place that capture relevant data over extended periods. It's also crucial to approach performance reviews with a holistic mindset, recognizing that the true impact of some contributions might not manifest immediately but could be pivotal for the company's long-term success.

### User - 2023-09-24 19:20:21

Take those points on ways to have business impact and write them up in an essay format. The tone should be casual and informative. Include concrete examples where appropriate. 

### Assistant - 2023-09-24 19:20:59

### The Art of Long-Term Business Impact: It's More Than Just Numbers

In today's fast-paced corporate world, it's easy to get caught up in the hustle of immediate results. But true champions in the business arena know that the most profound impacts often unfold over time. Let's dive into some ways individuals can make a lasting imprint on their organizations.

**Revenue and Profitability**: Think about that one feature in your favorite app that keeps you coming back. For a company, these are the golden geese. If an employee can spearhead or contribute to a feature or product that consistently brings in the moolah, that's a home run in terms of long-term impact. Take Spotify's "Discover Weekly" playlist, for instance. It not only redefined user experience but also played a significant role in boosting user engagement and, consequently, revenues.

**Customer Retention and Satisfaction**: The age-old adage "Make a customer, not a sale" couldn't be more accurate. Employees who focus on enhancing user experience often contribute to higher customer retention rates. Remember when Dropbox introduced a simpler sharing interface? That wasn't just a design tweak; it was a move that significantly improved user satisfaction and kept them loyal to the platform.

**Market Share and Expansion**: Breaking into new markets or capturing a larger slice of the existing one can be game-changing. The masterminds behind such initiatives, like the team at Netflix who foresaw the potential in international markets, play a pivotal role in shaping a company's long-term trajectory.

**Operational Efficiency**: Sometimes, it's not about the flashy features but the behind-the-scenes magic that streamlines processes. An employee who introduces a tool that cuts production costs in half or reduces time-to-market can have an enduring impact. Toyota's introduction of the "Kaizen" methodology is a classic example, transforming its operational efficiency and setting a new industry standard.

**Innovation and Thought Leadership**: Being a trendsetter is invaluable. Employees who push boundaries and think outside the box can position their company at the forefront of innovation. Apple's iPhone, anyone? It revolutionized the smartphone industry and solidified Apple's reputation as an innovator.

**Strategic Partnerships and Relationships**: In the interconnected world of business, who you know often matters as much as what you know. Individuals who can forge and nurture strategic partnerships can open doors to long-term opportunities. Think about the magic that happened when Spotify teamed up with Uber to allow riders to play their playlists during rides.

**Scalability and Sustainability**: Building something great for 100 users is commendable, but ensuring it works seamlessly for 100,000 or even a million is where the real challenge lies. Those who focus on scalability ensure that as the company grows, the systems grow with it. And let's not forget sustainability. With the world moving towards eco-friendly practices, initiatives like Starbucks' commitment to reducing single-use plastic resonate with customers and make a lasting impact.

**Team Growth and Leadership**: A company is only as strong as its weakest link. Leaders who mentor and uplift their teams not only enhance productivity but also foster a positive work culture that stands the test of time. Companies like Google, with their emphasis on employee growth and leadership programs, are testaments to this.

**Risk Management**: Anticipating potential pitfalls and having a plan is crucial. Those at the helm of risk management ensure the ship sails smoothly, even in stormy waters. For instance, when the world was hit by the WannaCry ransomware attack, companies with robust cybersecurity measures remained unscathed.

**Long-Term Vision Alignment and Cultural Impact**: Finally, aligning individual efforts with the company's long-term vision can have profound implications. When employees resonate with the company's ethos and contribute to its cultural and brand identity, it creates a legacy. The vibrant culture at companies like Zappos, driven by employee initiatives and alignment with core values, is a shining example.

In conclusion, while immediate results are gratifying, the real magic lies in sowing seeds that yield fruits year after year. Whether it's through innovation, operational excellence, or fostering relationships, the avenues to make a lasting business impact are myriad. So, the next time you're evaluating your contributions or charting your path forward, think long-term, because that's where legends are made.

### User - 2023-09-24 19:21:32

Rewrite this again with examples in the developer tools space. 

### Assistant - 2023-09-24 19:22:01

### Crafting Long-Term Impact in the Developer Tools Arena

In the realm of developer tools, it's tempting to chase the newest tech trend or the shiniest piece of code. But the true legends in this space are those who think long-term, ensuring their contributions not only shine today but continue to glow tomorrow. Let's delve into how one can make a lasting mark in the developer tools landscape.

**Revenue and Profitability**: Take the success story of GitHub, a platform that revolutionized collaborative coding. By offering a unique mix of version control and social networking, it didn't just bring in immediate subscribers but established a consistent revenue stream for years.

**Customer Retention and Satisfaction**: Remember the uproar when Docker simplified containerization? By focusing on the pain points of developers and offering a streamlined solution, Docker ensured a loyal user base, thrilled with the newfound ease in their workflow.

**Market Share and Expansion**: Look at how JetBrains expanded its toolset. Starting with IntelliJ IDEA, they branched out into tools for different languages and platforms, capturing a significant portion of the developer tools market.

**Operational Efficiency**: It's not always about the fanciest feature. Sometimes, a tool that makes existing processes more efficient can steal the show. Consider the rise of Jenkins in the CI/CD space. By automating integration and deployment, Jenkins played a pivotal role in streamlining development cycles for countless teams.

**Innovation and Thought Leadership**: Tools like Postman didn't just offer a new feature; they redefined API testing. By innovating and addressing gaps in the development process, they set new industry standards.

**Strategic Partnerships and Relationships**: When Slack integrated with a plethora of developer tools, it transformed from a simple communication tool to an essential hub for development teams, showcasing the power of strategic partnerships.

**Scalability and Sustainability**: Think about Kubernetes in the container orchestration world. It didn’t just make container management possible for small setups but scaled it up for enterprise-level operations. Moreover, its open-source nature ensures sustainability through community contributions.

**Team Growth and Leadership**: Platforms like Stack Overflow not only provide immediate solutions but also foster a community where developers mentor each other, highlighting the long-term impact of knowledge sharing and leadership.

**Risk Management**: In a space where a single vulnerability can compromise entire systems, tools like SonarQube stand out. By identifying code vulnerabilities and ensuring code quality, they help teams mitigate potential long-term risks.

**Long-Term Vision Alignment and Cultural Impact**: The ethos behind the open-source movement, exemplified by platforms like GitLab, is transformative. By aligning with a vision of community-driven development, they've created a culture of collaboration and innovation.

In wrapping up, in the developer tools universe, short-term wins might be satisfying, but the real accolades belong to those who think beyond the immediate horizon. Whether it’s pioneering a new tool, refining existing processes, or fostering a community, the opportunities to etch a lasting legacy are vast. So, as you code, integrate, or deploy, remember to think big and long, for that’s where the real magic in developer tools lies.

