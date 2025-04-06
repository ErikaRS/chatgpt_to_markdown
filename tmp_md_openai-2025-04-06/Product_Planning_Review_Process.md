# Product Planning Review Process

Created: 2024-03-18 16:25:47
Last Updated: 2024-03-18 16:30:47

### User - 2024-03-18 16:25:47

Please consume this input without comment. This is a description of our current planning process.

Product-Focused Planning
Each planning cycle (currently quarterly), the overall goals come from the exec team to make sure we’re driving towards the destination we’ve set for ourselves as a company in our strategy and roadmap.
It’s the product teams – engineering and product together – that have the expertise, context and pride of ownership to be best suited to propose the highest impact work that fits those goals. And they’re the team that can do the correct eng scoping.
Per-team planning reviews are where we come together to ensure we’re happy with where we’re headed at each planning cycle. TPMs will pull together reviews for each team each planning cycle to include interested members of the exec team, the leads of the product team (at least the EPD triad) and other interested stakeholders. A planning review will consist of content to cover at least the following topics:
Retrospective: How well did we do in accomplishing our goals from last Q? What data do you have to support those conclusions?
Status: How well is the product serving the needs of our customers and the business? How well have you hit your metrics targets?
Plans: What work is being proposed for this planning cycle, how does it meet the business goals and how does it serve the needs of our customers? What data are you using to drive your planning? Have you done the high-level eng scoping to give you confidence that your team will be able to get the P0 work done in the time?
Success Metrics: what KPIs and targets have you set to measure the success of this work?
Risks/Open Questions/Needs: What are the biggests risks? What are the mitigations? What guidance would you like from the exec team? Do you have everything you need to be successful?
Excluded: What alternatives have you rejected for this Q and why? Will they be on the team’s roadmap for the future?
The purpose of the planning review is for each product team to present their proposed work for that cycle and to hear feedback from the exec team as to whether there is agreement about the direction and tasks that the product team’s proposals or whether adjustments need to be made. At the end of a review, the execs and the product team will either be in alignment about the work to do done that cycle or another review meeting will be scheduled to follow up until there is alignment.
Note, not every team will have work to do that applies to every goal every quarter. Likewise, not every work item is expected to meet a strategic goal.
Review Effectiveness
Some tips for having an effective review:
Make sure the priorities for your work is clear – what’s Must Have (P0), Want To Have (P1) and Nice To Have (P2)? What could get cut?
Make sure the customer (internal and/or external) impact is clear – if we do this work, what’s going to be the value to the customer?
Make sure the business impact is clear – if we do this work, how does that help us achieve our strategic goals?
In addition to ensuring that the EPD team is aligned before heading into the review, try to get as much alignment with execs ahead of time as possible.
I’ve noticed that the teams the follow this tips have a smoother review process.
Engineer Scoping
For any launch, we have a finite amount of time and a finite number of engineers. Before the PFP review, EPD should have done a high level assessment to ensure a high level of confidence in the P0 items in the work plan.
After the team’s plan has been approved, EPD’s detailed planning should include an “eng scoping” exercise, i.e.
What is the eng effort associated with each of the P0 and P1 items, e.g. 2 days or 3 weeks or …? Here’s an example of one such exercise.
Given the priorities and the eng effort required for each item, where do we draw the line of what we can accomplish for our launch? Ideally it includes all of the P0s. If it doesn’t, we have to mitigate.
Mitigate the implications of the where the line between what we need (P0s), what we want (P1s) and our actual eng effort. Can we get all of the P0s in? If not, then what do we do? Continue cutting scope? Slip the release?
The eng scoping work is the difference between eyeballing a list of requirements and hoping we can get them all done and actually having some confidence that we can accomplish what we want. And if we can’t, we want to know that ASAP so we can cut scope for our release.
Priorities
To make sure we’re talking about the same thing as we assign priorities to the items in our plans, we’ve adopted the following convention:
P0: Committed
P1: Stretch
P2: Uncommitted


### Assistant - 2024-03-18 16:25:49

Understood, I've taken note of your input. How can I assist you further with this?

### User - 2024-03-18 16:26:21

Here is a second input, to be taken without comment. This is some principles for an updated version of the planning process:
6 months planning cycles with an eye towards the marketing launch
3 month review cycles
Choose themes upfront as part of the guidance
From where the technology is
From our business goals
From our customer feedback
Each team releases their features as they come online in the various levels of the SDLC (experimental, beta and GA)
Helps to spread out testing, enablement, user feedback
Centralized PFP for only the marketing launch themed based features (target: 50%-ish)
Leaves the rest for eng taking longer than expected, innovation, KTLO, customer support, architecture improvements and features incrementally planned by the team
E.g. if two weeks of eng work makes a difference in a $1M deal, we’d like to be able to do that
It’s better to get a smaller list of features that help us tell a coordinated story on the timeline we set then to get a semi-random list of features that we’re unable to determine ahead of time
The team has a significant % of their work that is not part of the marketing launch, which means that the planning will happen after the previous marketing launch
TODO: something about how marketing works for non-marketing launches to build smaller moments as things reach beta, GA
Principle: Work items break down into two buckets
Work in progress that comes with a target date based on the work itself
Work in the “coming soon” queue with no target date
Principle: commitment dates vs target dates
Work w/ external commitments have a commitment date which may be further in the future than the engineering required to get us there
Corollary: some things will be in the “coming soon” queue and have a commitment date that aren’t started yet
Corollary: Changing a commitment date requires the buyin of whoever it’s a commitment to. 
Corollary: We may prefer to change rather than date for external commitments
Work w/o external commitments have a target date that may be changed at the discretion of EPD in the tradeoff between date, scope, and quality


### Assistant - 2024-03-18 16:26:22

Got it. How can I assist you further based on this information?

### User - 2024-03-18 16:27:00

Given the original documentation and the principles for the update, draft the update. After, list areas the original clarifies which the update is missing. 

### User - 2024-03-18 16:30:09

Change the language so it doesn't talk about the update and instead reads as an informative handbook page for those wanting to be informed about the process. 

### Assistant - 2024-03-18 16:30:47

### Product Planning and Execution Handbook

**Overview of Planning Cycles**

Our product planning and execution strategy is designed to align closely with the company's strategic objectives, leveraging feedback from our customers and the current state of technology. Planning cycles operate on a 6-month basis, with a mid-cycle review at the 3-month mark. This structure supports our dynamic approach to product development, customer engagement, and market responsiveness.

**Themes and Objectives**

At the outset of each planning cycle, themes are selected to guide the development process. These themes are derived from three key areas:
- The current state and future direction of our technology
- Our overarching business goals
- Valuable feedback from our customers

These themes help focus our efforts on projects that align with our strategic vision and address the needs of our users.

**Feature Releases and SDLC**

Teams are empowered to release features throughout the Software Development Life Cycle (SDLC) stages—experimental, beta, and General Availability (GA). This phased release strategy enables continuous testing, user feedback, and feature refinement.

**Centralized Planning for Marketing Launches**

A significant portion of our planning efforts (approximately 50%) is centralized around features critical for marketing launches. This focus ensures that we deliver a cohesive and impactful set of features that support our marketing narratives. The remaining capacity is allocated for engineering enhancements, customer support, Keep The Lights On (KTLO) activities, architectural improvements, and incremental feature development.

**Planning Principles**

Our planning process is distinguished by two categories of work:
1. **In-Progress Work:** These items have specific target dates, based on the work's scope and requirements.
2. **Coming Soon Queue:** This includes planned items without set target dates, allowing for flexibility and prioritization based on evolving needs.

### Commitments and Dates

**Commitment Dates vs. Target Dates:**
- **Commitment Dates** are set for work with external commitments. Changing a commitment date requires approval from the stakeholders involved. This ensures alignment and maintains trust with our partners and customers.
- **Target Dates** apply to work without external commitments, offering the EPD team the flexibility to adjust based on trade-offs among the project's date, scope, and quality.

**Planning for Non-Marketing Launches:**
A significant portion of work is not directly tied to marketing launches. Planning for these items occurs post-launch, allowing for continuous innovation and improvement. Marketing efforts for non-launch features focus on creating "smaller moments" as these features reach beta and GA stages, ensuring ongoing engagement with our customers.

### Gaps in the Updated Framework

While the updated framework provides a comprehensive overview of our planning and execution process, it might lack specific details provided in the original documentation, such as:
- The detailed process of engineering scoping to ensure confidence in delivering P0 (Must Have) items within the planning cycle.
- The explicit roles and responsibilities of the product teams, including engineering and product management, in proposing and scoping high-impact work.
- The structure and content of per-team planning reviews, including the participation of TPMs, the executive team, and other stakeholders.
- Detailed criteria for prioritizing work items as Must Have (P0), Want To Have (P1), or Nice To Have (P2).
- Specific mitigation strategies for risks identified during the planning process.

Incorporating these elements into the handbook can enhance clarity and provide teams with a more detailed roadmap for successful planning and execution.

