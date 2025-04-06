# Enterprise Ownership Concerns

Created: 2024-03-19 07:01:31
Last Updated: 2024-03-19 07:02:20

### User - 2024-03-19 07:01:31

Summarize the key emotional and factual takeaways from this feedback:
THE ORIGINAL NOTE:
Quinn and Beyang want to see the Enterprise/Strat team really taking on ownership of the whole end-to-end experience of customers, including being the ones to monitor and aggregate feedback and collaborate with the client teams on things like making quality improvements (e.g., multi-repo context quality is known to be low).

They acknowledge that this is adding an additional net new requirement to expectations for the enterprise team, but they would love to see this level of ownership and really being focused on solving the problem end-to-end.

@csells was in the room too, so he knows that this is joint feedback for you and @aravind to take and figure out what to do with.

Thoughts on this? I know you and the team are already stretched thin, and I told Quinn that we'd have to figure out how to make something like this a reality. But do you feel like the change in mindset from owning the enterprise-specific delta to owning the end-to-end enterprise experience and being the ones to drive a partnership with other teams to solve problems enterprises experience is a reasonable framing of ownership?

THE FEEDBACK:
What I am hearing
Above we describe a working model where one set of Cody teams (experience mostly?) is owning the making of features only on a small scale and experimenting (let’s call this the prototyping team), but not driving them with the customer in mind. Specifically here I mean the paying customer vital to the business..
The other team (enterprise) in this setup would be tasked with playing catch-up (null hypothesis, see alternatives below) and tackling technical debt and the long tail of development to drive enterprise grade quality for features that were prototyped essentially. Effectively re-focusing the work on the vital customer
Note: There seems to be an implicit assumption that we can actually operate like that - building features for a different target audience and then revamping them to a different one (that pays). I feel like a more productive approach would for all of us in engineering to regain focus on the vital customer. Strat/enterprise team is one team that has kept this focus.

Historical references: JetBrains set up for failure
This reminds me of the model where VS Code is in mainstream development and JetBrains plays catch up. There we have seen no checks and balances for VS Code team. Instead I observed that JetBrains was responsible for (a) feature development (b) dealing alone with VS Code development breaking JetBrains while (c) the enterprise pressure is mostly on JetBrains.
Conclusion: I feel like we realized this model did not work: We merged the client teams and we are trying to power the JetBrains team, and increase testing coverage.
Side note: In my opinion client teams should also necessarily develop in the same repo to allow for checks and balances between editors’ development. 

The reason I mention that is that I want to highlight how I think we set up JetBrains team for failure. Similarly my gut feeling is that we would be setting up Enterprise team for failure.

Historical references: Multi-tenant effort with features build for single-tenant
(apologies, this section is going to be less tangible than the above, this is second-hand history)

Background: When thinking of architecture, I knew we would talk about multi-tenant. I went and interviewed bunch of people on what were the technical and organizational failure scenarios last time we tried multi-tenant (Rafał and Erik specifically). Here’s an interesting finding:
Multi-tenant effort was not holistic organizationally. That is, we wanted to build a multi-tenant solution retroactively on a fundamentally single-tenant system.
Example: Multi-tenant effort was under way, but batch changes team developing batch changes lived in a single-tenant bubble. The goals of the team were not aligned with multi-tenant environment in mind.
This seems similar to what we’re proposing now: The expectations specifically sounds like we don’t drive a horizontal effort across teams (although it does say collaborate with the client teams - I expand on that below). Why does it not sound like it? Well if it was a horizontal effort, selecting the enterprise team to be responsible seems counter-intuitive (rather each team should own parts and a horizontal team should coordinate)
.
The stress equilibrium: heavy on the long tail where the customer is
There is no stress on the prototyping team. They make solutions that work on a small scale and experiment. There is no goal or incentive for that team not to produce whole lot of technical debt. By tasking another team with enterprise experience end-to-end we make tech debt not the prototyping team’s problem.
The enterprise team is on the other hand under immense pressure because making feature X work for enterprises makes or breaks a $2m deal with Bank Z.
This is even more relevant because of social expectations of work estimates. It feels like it’s just the delta between having something PLG ready and enterprise ready. One can almost imagine this conversation: How hard can it be? I mean it works for PLG right? When can we have it for Bank Z? I already signed a contract promising feature X.

Note: This is not to say that prototyping should have enterprise grade in mind. But this is to emphasize a problem that not only is there stress because of enterprise deal breakers, but also enterprise team’s negotiation position starts from hearing: I mean, it already works, right?

Extra note: One of the common practices in the industry is to force-throw-away the prototype. That is: you have to start from scratch when building the enterprise grade offering (and your problem space is bigger). 

(...) collaborate with the client teams
The only way to interpret this, that is congruent among other statements in the memo as well as my beliefs about Cody development, is a proactive responsibility of making features enterprise-grade across all of Cody.
This is a bigger surface area than all of the other Cody teams combined, because you have to work on every client, every backend piece, and AI components, on every deployment environment, and these are all moving targets.
On top of that the team has to understand a diverse set of enterprise requirements (which PLG is free of).
On top of that the team has to manage collaboration with all the other teams.

The way we plan
We went from more total to more siloed planning with PFP. Presentations are per team with different PMs and EMs involved. Leadership is the nearest necessary common denominator of planning across teams. This promotes independence of team execution.
An enterprise team collaborating closely with all teams on enterprise grade features is a wrench in the wheel of the current planning system (assuming the team is effective). If it is not it likely just fails.

Current team charter(s)
Here’s how I think the enterprise/strat team is acting today:
Developing specific solutions for strat teams (including custom work for POCs with relatively high cost/customer)
Note: this is where on the sales-side our team is nicknamed the deal-landing team.
Developing enterprise-only features (as opposed to leveling up PLG features to enterprise grade - think enterprise analytics as opposed to multi-repo context working in an enterprise environment).
Handling self-hosted environments. It’s a different game than everything else we do.
Customer support (recently about 70% of most senior engineers capacity goes there).
Recently - more staff-level/horizontal efforts like diagnostics, improving customer support collaboration, testing (all of these again - across all of Cody surface area).
With the memo and the recent communication on how we appreciate the strat team efforts, I do not believe we think about the two sets of responsibilities (current and new expectation) as an either-or. Instead I believe leadership would expect the team to handle all of the above.

What I want to stress in this section is how much surface area enterprise/strat team has today. It’s expected to have impactful feature output with enterprise grade, while handling strat customers (and expanding their set) and non-strat customers (JPMC, bet365) in cases where issues are very likely client side with relatively little involvement from client teams.

Potential paths forward
(this section is a work in progress, but wanted to ship this anyway in interest of time and respecting our need for rapid feedback and decision making)
(hypothetical - unfeasible to best of my knowledge) limit our enterprise scope:
We could go in the direction of just JetBrains for enterprises, or just Cloud or just autocomplete.
This would be to limit the surface area the team needs to handle with their enterprise quality ownership.
Obviously this is unrealistic and not aligning with our goals, but I wanted to call it out as an option.
(horizontal team)
Make a team focused only on enterprise grade features working with enterprise PM (no strat, no self-hosted, no enterprise-only features) - just scaling features to enterprises. This could be a relatively small very senior team with a dedicated TPM and a PM.
Note: I just wrote that down, I am actually hesitant to put any weight behind this option. Like self-hosted is naturally a significant part of enterprise. I don’t believe it can be abstracted out - we cannot have one team be scaling out features to enterprises without thinking of self-hosted.
(catch-up team) - I think this is the null hypothesis that stems from the memo
One team is responsible for all things enterprise.
The current planning setup is not made to support this mode.
Assumption: Goal is for the other teams to have roadmaps unrestricted by enterprise needs.
Opinion: it’s a recipe for failure we’re repeating. Happy to expand, but I think it pretty clearly follows from historical lessons above.
(enterprise-first company) - the only feasible option in my opinion
The company starts acting from being PLG first to being Enterprise first.
There is a small team of experimenters pushing new features on the PLG crowd.
The rest of Cody consists of a large enterprise-focused org (this include client teams and AI team).
Enterprise org feature development stems from a few sources:
Enterprise PM and market/sales input.
PLG prototypes
Note: we start talking about PLG development as a prototype. It took us 2 weeks to build, we shipped it, we evaluated it. Now if enterprises want it, we need to throw the prototype away and be ready to sketch development of an enterprise feature anew.
Development-wise PLG and experimentation is catching up behind enterprises not the other way around (or preferably noone plays catch up).
PLG features could be developed as experiments behind feature flags.

Personal take - regarding capacity and managerial expertise
The proposal at first glance seems at a level way beyond my experience to lead.
I do consider myself a junior manager.
I do get a lot of stress from the position we’re in - customer facing, expectations ever increasing, pressure from various directions.
I do try to tie all the loose ends I see with all strength and capacity I have, but it seems not enough.
Now I hear an expectation which to me realistically does not mean a 10% increase of responsibility of a team already spread thin, but a 2x increase.

Personal take - phrasing of the feedback
Given that the team has been working extremely hard supporting strat and non-strat customers. Many have worked over time, stretching themselves, sometimes paying for that with their own health, I find this phrasing upsetting and disheartening:
Quinn and Beyang want to see the Enterprise/Strat team really taking on ownership of the whole end-to-end experience of customers.
It directly implies that the enterprise/strat team did not really take ownership of the whole end-to-end experience of customers.
Let’s compare that with one observation: Vast majority of features are on the client. The null hypothesis when anything breaks for a specific customer should be that it’s a client-side issue. Yet, folks from strat/enterprise team gladly handle the customer issue. Debugging client codebase they have little experience in, and tech-debt they have contributed none of. And they never ever complained about it. Ever.
Note: I actually do not know what is the client teams day to day involvement with customer issues. Perhaps we should look closely into that. From what I overheard, a few times it seemed like individuals in client teams were completely oblivious of enterprise requirements, <speculation>which would suggest lack of participation in customer issue handling</speculation>.
I think Enterprise/Strat team behavior so far has been really taking ownership over end-to-end experience of all of Cody for enterprises. They never say no to debugging issues and issuing fixes that are clearly owned by other teams (look at JetBrains for another example).
I mean like Stephen and Chris now are digging into details of Node.js runtime (in the extensions) for how it dispatches http traffic across the mess of networking libraries. It’s hard to think of going farther beyond their charter. This does look like a strong case of end-to-end handling.

Final anecdote
When I was writing this I was thinking of a civil engineer who designed a bridge that afterwards was built. The bridge was designed to handle cars up to 20’000 lbs of net weight. The engineer and the building crew applied industry standards for tolerance outside of the requirements, picked quality materials to go above and beyond. They delivered a solid bridge. In practice it easily handles 40’000 lbs. When we would test it, it would start likely cracking here and there after we put a 50’000 lbs truck on it, but who really knows when it breaks?

When we’re saying the strat/enterprise team is spread thin, we are really saying that it’s for sure beyond their nominal capacity and well within or outside of a reasonable tolerance range (we don’t really know). Trucks anywhere between 30-40k lbs drive by daily.

Please let’s not break the strat/enterprise team.


### Assistant - 2024-03-19 07:02:19

The feedback outlines concerns and suggestions regarding the proposed operational shift for the enterprise/strategy (strat) team at Cody, emphasizing the need for broader ownership and integration of end-to-end customer experience and enterprise-grade feature development. Here are the key emotional and factual takeaways:

**Emotional Takeaways:**
- **Stress and Capacity Concerns:** The person providing feedback is worried about the team's capacity to handle the new expectations, mentioning that it feels like a significant increase in responsibility rather than a manageable adjustment. This concern is compounded by the current high stress levels due to customer-facing roles, increasing expectations, and the junior management experience of the person.
- **Disheartenment:** The phrasing of the original feedback from Quinn and Beyang, suggesting the team hasn’t fully owned the customer experience, is seen as disheartening and unfair. The respondent highlights the team's extensive efforts and sacrifices, including working overtime and compromising their health, to meet current demands.
- **Ownership and Responsibility:** The feedback suggests that the strat/enterprise team has already been taking substantial ownership of issues and tasks beyond its direct responsibilities, including tackling problems and technical debts created by other teams.

**Factual Takeaways:**
- **Proposed Operational Shift:** The shift implies a transition from a siloed approach, where the prototyping team develops features with limited scale and consideration for enterprise needs, to a more integrated approach where the enterprise team assumes responsibility for making features enterprise-grade and ensuring end-to-end quality.
- **Challenges of Current Model:** The feedback compares the proposed model to past failures, such as the JetBrains vs. VS Code dynamic, illustrating how such setups can lead to one team being overburdened with catch-up work, technical debt, and unaligned incentives.
- **Suggested Improvements:** Several paths forward are considered, including limiting enterprise scope (deemed unrealistic), forming a horizontal team focused solely on enterprise-grade features, and adopting an enterprise-first approach where the company shifts its priority from product-led growth (PLG) to enterprise needs. The latter involves major organizational changes and a significant shift in development focus.
- **Historical Precedents:** The feedback references historical challenges with multi-tenant architecture and the distribution of work and pressure between prototyping and enterprise teams, suggesting that the proposed changes could repeat past mistakes without a significant realignment of priorities and responsibilities.

The feedback calls for a reconsideration of the proposed changes, advocating for a model that balances the workload more evenly, avoids setting the team up for failure, and recognizes the contributions and limitations of the enterprise/strat team. It highlights the need for comprehensive planning, realistic goal-setting, and a shift in organizational culture to truly support enterprise-grade development.

