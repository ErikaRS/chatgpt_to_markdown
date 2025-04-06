# Org Change Comm Accepted

Created: 2024-05-06 17:49:33
Last Updated: 2024-05-06 17:56:24

### User - 2024-05-06 17:49:33

Help me put together comms for an org change. To start, here is an overview of the change. Do not respond to this. Just say "accepted":
Given that we are hiring up to two new managers for the Cody team, now is the right time to do some org design and figure out the right organizational structure for making Cody successful. This document discusses the problems we want to solve and recommends a high level org structure:
Two teams: Cody Core and Cody Prime
Manager of the Core team will be the single-threaded leader for Cody
We will continue Strat engagements, but Strat is a label on the Core team’s work, not a team
The Cody team structure will shift to match this new structure:
Members of the Cody Enterprise team will be split between Cody Core and Cody Prime
David Veszelovszki will go back to being an IC
Erika Rice Scherpelz will interim manage Cody Core
Eric Shamow will interim manage Cody Prime
Quinn Slack and Beyang Liu will no longer act as interim leads for the Cody Clients team
There are no changes to the AI, Code Search, Product Platform, Security, or Infrastructure teams
PM and Design responsibilities will not change


### Assistant - 2024-05-06 17:49:35



### Assistant - 2024-05-06 17:49:35

Accepted.

### User - 2024-05-06 17:50:05

Here is the changes to reporting structure. Again, just say "accepted"
Cooney, Dominic	Clients	Beyang (Beyang) Liu	Cody Product Experience	Erika (interim)	Cody - Core
Bugakov, Valerii	Clients	Beyang (Beyang) Liu	Cody Product Experience	Erika (interim)	Cody - Core
Kumar, Naman	PLG / Noodle	Dávid (David) Veszelovszki	Cody Growth Engineering - PLG	Erika (interim)	Cody - Core
Geirsson, Ólafur	Clients	Beyang (Beyang) Liu	Cody Product Experience	Erika (interim)	Cody - Core
Ross, Thomas	Clients	Beyang (Beyang) Liu	Cody Product Experience	Erika (interim)	Cody - Core
Spiess, Philipp	Clients	Beyang (Beyang) Liu	Cody Product Experience	Erika (interim)	Cody - Core
Nauta, Rik	Enterprise	Cezary (Cezary) Bartoszuk	Cody Growth Engineering - Enterprise	Erika (interim)	Cody - Core
Khan, Arafat Dad	Enterprise	Cezary (Cezary) Bartoszuk	Cody Growth Engineering - Enterprise	Erika (interim)	Cody - Core
Woo, Beatrix	Clients	Beyang (Beyang) Liu	Cody Product Experience	Erika (interim)	Cody - Core
Yegge, Stephen	Clients	Beyang (Beyang) Liu	Cody Product Experience	SQS	Cody - Core
Gutekanst, Stephen	Enterprise	Cezary (Cezary) Bartoszuk	Cody Growth Engineering - Enterprise	Erika (interim)	Cody - Core
Veszelovszki, Dávid	PLG	Erika Rice Scherpelz	Cody Growth Engineering - PLG	Eric Shamow (interim)	Cody - Prime
Smith, Chris	PLG	Erika Rice Scherpelz	Cody Growth Engineering - PLG	Eric Shamow (interim)	Cody - Prime
Yemets, Taras	Enterprise	Cezary (Cezary) Bartoszuk	Cody Growth Engineering - Enterprise	Eric Shamow (interim)	Cody - Prime

### Assistant - 2024-05-06 17:50:06

Accepted.

### User - 2024-05-06 17:54:22

Finally, here is the high level org design and goals. Again, just say "accepted"
Preferred option
Two team split between Cody Core and Cody Prime
Split the organization into two teams:
Core: the primary experience the user thinks of as Cody. 
Prime: all the functionality for managing and monetizing the user experience.
Cody Core would be notably larger than Cody Prime. 

Cody Core: 
End-to-end ownership of the in-client user experience for all customers, PLG & Enterprise 
Owns
Clients, including releases
Code Search would continue to own Cody Web
Agent
Cody Enterprise features in the Sourcegraph instance
Supporting different enterprise configurations
Overall usage of LLMs
Overall product architecture

Cody Prime:
End-to-end ownership of everything that helps with managing and monetizing the user experience, for both PLG and Enterprise
Owns
PLG accounts, teams, invites, and payment
Analytics, usage metering, license management, billing, abuse, rate limiting, proxying to LLMs
Cody Gateway


Overall account management architecture for Cody, including subscriptions, accounts, and licenses for both PLG and Enterprise

Why this option? The biggest request when it comes to making things work better on Cody is to reduce the number of cooks in the kitchen, reduce the need to pull in so many people and teams for even simple decisions, to increase the decision making authority of someone. By dividing Cody into two parts, both of which have end-to-end ownership of business value but also both of which have distinct ownership of code, we can increase decision making velocity and clarity while still avoiding the problem of having a team that’s too large to manage. 

Downsides: 
By getting rid of the PLG and Enterprise split, it’s possible that the team may invest too much in one user population at the expense of the other. E.g., the potential for large deals could cause us to focus on enterprise specific features instead of broader appeal features. Solving this problem will require discipline at the planning level to make sure we’re adhering to our overall goal of delighting pro devs to win enterprises. 
The Core team will be very large — at the upper bound of what one manager should realistically be given. Over time, we will need to split the core team. At that point, a Clients/Services split within the core team may make sense because the architecture will 


Appendix: Decision criteria details
Here are some decision criteria that will be used to evaluate options and a brief discussion of the challenges that inspired them.

Delight pro devs to win enterprises
Problem: Self-Serve vs Enterprise. Are we focusing too much on Enterprise customers? Too much on PLG customers? Both sentiments come up often. The underlying challenge is that we see these things as separate. 
Therefore: Our team structure needs to strongly support the PLG to Enterprise pipeline. 

Single-threaded Cody leadership
Problem: Lack of clear, authoritative leadership. The most consistent theme in feedback about how to improve Cody’s efficiency is that we need to introduce a single-threaded leader: a DRI whose sole focus is Cody. 
Therefore: Cody eng should have a single-threaded leader. 

Make space for “whatever it takes” customer work
Problem: Customer challenges using Cody. Our current planning process and org structure incentivizes shipping features. 
Therefore: Our team structure should create space to allow us to do whatever it takes to make customers successful without making it a zero-sum tradeoff between that and planned feature work.

Clear team responsibility
Problem: Lack of clear team missions and structure. To paraphrase a common sentiment, every Cody decision requires bringing in half a dozen people. On the flip side, there are critical pieces, like the Agent, which are staffed on a “best effort”. We have also seen the Enterprise team mission shift significantly since the strat model was established, and there’s confusion about how the team will be most effective. 
Therefore: Teams should have clear missions where they can own their area. Our team structure should align well with quickly making decisions, executing well, and making sure all pieces are owned. 
Caveat: There’s not a clean way to map our current architecture cleanly onto a team structure, so teams will need to collaborate to be successful. 

Staff to win
Problem: Teams are stretched thin. We are constantly pulling resources from important projects to staff even more important projects. The boundaries between teams make it hard to shift work from one team to another. 
Therefore: We need to staff teams such that they have the necessary skills, ownership, and numbers to execute on their mission effectively. We should have larger teams that are more adaptable rather than smaller teams that are more specialized. 
Caveat: Org structure alone won’t fix this. We also need more people.


### Assistant - 2024-05-06 17:54:23

Accepted.

### User - 2024-05-06 17:55:01

Now, draft a message to #team-people-managers, a channel of all of the people managers in the company, following the general style of this post: 
Team, I want to give you the heads up that Steve is moving from his current Eng leadership role into an IC role, focused on Cody, architecture, and all the awesome Stevey blogs and chats with devs/customers about Cody. Erika will now lead all of Engineering. 

Steve, Erika and I are all really excited about this. Erika’s an awesome leader who’s brought so much clarity and focus to the eng org, and I know she’ll continue to make things better in this expanded role. Steve brings really valuable experience to the team, having built lovable products at Amazon, Google, and Grab, and we’ll all benefit from having him closer to the code, architecture, and product (he knows IC and management roles well). Plus, this shift makes a lot of sense given where we’re headed as a company — building one lovable Code Intelligence product.

A huge thank you to both Erika and Steve for everything they’ve already done and looking forward to seeing us get even better with this shift!

There will be a few shifts to reporting and team structure for Cody teams as part of this. Details and FAQ are in the 🧵.

Please keep this confidential to this group. I’ll announce it to the company later today. 


-THREAD-

Here’s an overview of reporting changes (org chart for reference):
We will have two main Cody teams: Cody Growth Engineering and Cody Product Experience. 
The Cody PLG, Cody Enterprise, and Cody Strat teams will come together to form one team called the Cody Growth Engineering team which will report to @erika. @Cezary B and @David V will lead that team.
@Cezary Bartoszuk will continue to manage Strat and Enterprise
@David V will continue to manage PLG, with @Bee Woo moving to PLG to provide client support.
@Chris Smith will report to @Erika and will work with both PLG and Enterprise.
The Cody Clients, Cody Context, and Cody Services teams  will come together to form the Cody Product Experience team and will report to @beyang.
@stevey will manage the external dev consultants working on JetBrains for the time being. This will allow us to keep moving fast here since Steve is already very familiar with the work being done. 
@Beatrix will be moving to the Cody Growth Engineering team (listed above) to help that team move quickly when there are client changes. Thank you Bee for the work you’ve done on Cody!
AI will continue work in tandem with this team and report to @rishabh. @rishabh will report to @beyang.
There are no changes on the Search and Platform side of engineering.

See FAQs - Eng leadership change - Feb 2024 for more information.


### Assistant - 2024-05-06 17:55:25

**Subject:** Upcoming Changes to Cody Team Structure and Management

**Message:**
Team,

I wanted to give you all a heads-up about some upcoming changes within the Cody team structure that will help us enhance our organizational effectiveness and focus on delivering exceptional value to our users.

**Leadership Updates:**
We're introducing a new structure for the Cody teams, which will now be split into two distinct units: **Cody Core** and **Cody Prime**.

- **Erika Rice Scherpelz** will serve as the interim manager for **Cody Core**, taking on a pivotal role in overseeing the primary user experience and strategic enterprise features. Erika’s leadership and clarity have greatly benefited our engineering efforts, and I'm confident in her ability to lead this larger team.

- **Eric Shamow** will serve as the interim manager for **Cody Prime**, focusing on management, monetization, and operational aspects of the user experience. Eric's expertise will be crucial as we aim to streamline operations and enhance our service offerings.

Additionally, **David Veszelovszki** will transition back to an Individual Contributor role, continuing to make significant contributions without the managerial responsibilities.

**Team Realignment:**
Members from the former Cody Enterprise team will be redistributed between Cody Core and Cody Prime to align with the new structure. This realignment ensures that both teams are optimally staffed to focus on their specific areas of responsibility effectively.

**Departing Interim Leads:**
Quinn Slack and Beyang Liu will step back from their interim lead roles within the Cody Clients team, as the new leadership takes on their responsibilities.

**No Changes in Other Areas:**
It's important to note that there are no changes to the AI, Code Search, Product Platform, Security, or Infrastructure teams. PM and Design responsibilities will also remain unchanged.

We believe these changes will reduce complexity, enhance decision-making speed, and improve our ability to deliver outstanding products and services. I am enthusiastic about the future of Cody under this new structure and confident in our leadership team’s ability to guide their teams toward continued success.

**Confidentiality Notice:**
Please keep this information within our group until the official company-wide announcement later today.

Thank you all for your continued hard work and dedication. I am excited to see how these changes propel us forward.

Warm regards,

[Your Name]

### User - 2024-05-06 17:56:09

Make this shorter and start with what is happening. 

### Assistant - 2024-05-06 17:56:22

**Subject:** Important Organizational Changes to Cody Team Structure

**Message:**
Team,

We are making some significant changes to the Cody team structure to streamline our operations and enhance our focus. Here's what's happening:

- **Cody Core and Cody Prime:** We're splitting the Cody team into two units. **Erika Rice Scherpelz** will interim manage Cody Core, focusing on the primary user experience and strategic enterprise features. **Eric Shamow** will interim manage Cody Prime, which will handle the management and monetization aspects.

- **Leadership Adjustments:** David Veszelovszki will return to an IC role, contributing his expertise without managerial responsibilities. Quinn Slack and Beyang Liu are stepping back from their interim lead roles as we transition to the new leadership structure.

**Additional Details:**
- The former Cody Enterprise team members will be reassigned appropriately to align with this new structure.
- There are no changes to other teams like AI, Code Search, Product Platform, Security, or Infrastructure.

These changes are designed to enhance decision-making velocity and focus on delivering exceptional value to our users. Please keep this information confidential until the broader company announcement later today.

Thanks for your cooperation and commitment during this transition.

Best,
[Your Name]

