# Beta Process and Launches

Created: 2024-12-09 16:31:36
Last Updated: 2024-12-09 16:46:58

### User

*[user_editable_context content]*

### User - 2024-12-09 16:31:36

Let's draft up a doc about some process change suggestions. The goal is to be a short document proposing some process changes to share with the rest of the company for review.

The current process that this is relative to is here: https://www.notion.so/sourcegraph/Software-Development-Life-Cycle-SDLC-639073eefb534c52b5dc21dc309f0ee0?pvs=4 

Here is the canonical list of things we want to do:
Decouple launch moments (quarterly, owned by marketing) from releases (monthly, owned by product/eng)
The quarterly launch calendar will contain external commitments. This will give us more flexibility in moving things around in a given quarter.
Default to all major new features going through beta before GA. Marketing is free to make launch moments out of the beta (after all, competitors are making launch moments out of demo videos and EAPs)
I'd like for the quarterly launch moments to fall into the 2nd month of the quarter, so we can use the buzz from the event to drive deal closings in month 3 of the quarter. So target March 22 (tentative) as the next launch date?
Streamline the monthly release process to be a "min viable" release focused on changelogs and internal documentation

Here are more extensive notes from a conversation. Note that the conversation was evolving so things said earlier are overriden by things said later where they contradict:

B: Proposal: all big new features go through a beta phase first?
(and we don't commit to GA date until the beta is out?)

E: I like that as a conservatively minded engineering person... but we'd have to consider how that interacts with marketing moments.
E.g., do we have a one box beta? If so, what does that do for Jan 29th and our ability to plan for it if we won't have a GA date pretty much until the product is ready to launch?
(Note: I do agree with you. I'm just trying to push back on the angles that are likely to break so we can stress test.)

B: i mean our competition is doing marketing launches around demo videos and sign up forms
so...
Sourcegraph One beta seems reasonable to me

E: so... maybe...
we lean more heavily on preannouncing for marketing
we launch things first as beta
when we get to GA, we may have another "hey, we actually launched it marketing moment"
but mostly launches are that min-viable-launch (changelogs and internal enablement) that we were discussing in the chat bar
?
I could get behind something like this
(Also, we should totally pull in the TPMs before we finalize anything :upside_down_face: )

B: yeah of course :slightly_smiling_face:
i think we want to decouple the marketing splash from setting expectations of GA stability

E: (Also, FWIW, a lot of this comes down to slight tweaks to our existing SLDC and Product Planning processes... and actually following them more consistently!)

...

E: Yeah, that's the downside. Let's start by saying "thou must go through beta before GA" and see if that alone is enough to provide the visibility and quality bar that TS and Sales are looking for (and that we all want!)

E: Keep the TPM role for now
Consistently make EMs responsible for project / team level stuff
Focus TPMs on initiative level work, not project level work
Work with PMs to get them to take on more of the program management work they aren't currently doing
Continue to have Kalan working on a combination of PM/TPM work, maybe moving him more toward PM over time
Explore expanding Ron's role to be more fully about being the EPD/GTM bridge, including taking on more of Jamie's release related work

### Assistant - 2024-12-09 16:32:08



### Assistant - 2024-12-09 16:32:08

{"name": "process_change_proposal", "type": "document", "content": "### Proposal for Process Changes\n\nThis document outlines proposed adjustments to our existing Software Development Life Cycle (SDLC) and related workflows, aiming to enhance efficiency, align marketing and engineering timelines, and improve product quality.\n\n#### Key Proposals\n\n1. **Decouple Launch Moments from Releases**\n   - **Current State**: Quarterly launch moments are tied to monthly releases, which creates rigid dependencies and scheduling conflicts.\n   - **Proposed Change**: Separate launch moments (quarterly, owned by Marketing) from releases (monthly, owned by Product/Engineering).\n     - The quarterly launch calendar will focus on external commitments and can use flexible timelines within the quarter.\n     - Marketing can leverage existing milestones, including betas, for impactful announcements.\n\n2. **Introduce Beta as a Default Phase for Major New Features**\n   - **Current State**: Features often go directly to General Availability (GA) without a structured beta phase.\n   - **Proposed Change**: All major new features will go through a mandatory beta phase before GA.\n     - GA dates will not be committed to until after the beta launch.\n     - Marketing can create launch moments around betas, leveraging buzz similar to competitor strategies (e.g., demo videos, Early Access Programs).\n\n3. **Standardize Quarterly Launch Timing**\n   - **Current State**: Launch timing lacks alignment with quarterly business goals.\n   - **Proposed Change**: Schedule quarterly launch moments in the second month of each quarter.\n     - This timing will maximize momentum from the launch event to drive deal closings in the final month of the quarter.\n     - Example: Target March 22 as the next launch date.\n\n4. **Streamline Monthly Release Processes**\n   - **Current State**: Monthly releases involve unnecessary overhead, detracting from changelog and documentation focus.\n   - **Proposed Change**: Optimize the monthly release process for minimal viable delivery:\n     - Focus on changelogs and internal documentation.\n     - Reduce dependencies on marketing or GA-readiness.\n\n#### Supporting Notes\n\n1. **Beta and GA Visibility**\n   - A structured beta phase will:\n     - Provide better visibility into progress and quality for stakeholders.\n     - Align expectations across teams, ensuring Sales and Technical Support have sufficient preparation.\n   - GA launches can still serve as secondary marketing moments if desired.\n\n2. **Consistency in Existing Processes**\n   - Many of these changes involve slight adjustments to our current SDLC and Product Planning processes.\n   - Greater consistency in following these processes will be critical to achieving intended outcomes.\n\n3. **Role Clarifications and Optimizations**\n   - Retain the TPM role but refine focus:\n     - **Engineering Managers (EMs)**: Responsible for project and team-level management.\n     - **TPMs**: Focused on initiative-level coordination.\n     - **PMs**: Encouraged to take on additional program management responsibilities.\n     - Expand Ron\u2019s role to strengthen EPD/GTM bridging efforts, including release-related work.\n\n#### Next Steps\n\n1. Share this proposal with stakeholders (e.g., TPMs, EMs, PMs) for feedback.\n2. Gather input on:\n   - Feasibility of decoupling launches and releases.\n   - Practical challenges of enforcing a mandatory beta phase.\n   - Proposed timing for quarterly launches.\n3. Pilot the new processes in the upcoming quarter, iterating based on lessons learned.\n\n---\n\nPlease review and provide feedback to refine these proposals further before we finalize implementation."}

### Tool (canmore.create_textdoc) - 2024-12-09 16:32:08

{"result": "Successfully created text document 'process_change_proposal' which will be referenced in all future messages with the unique identifier textdoc_id: '67578c04c7108191b00753c4e513fffd'", "textdoc_id": "67578c04c7108191b00753c4e513fffd", "name": "process_change_proposal"}

### Assistant - 2024-12-09 16:32:08

This draft captures the proposed process changes and their rationale. Would you like to dive deeper into any specific sections, such as the beta phase implementation or role clarifications? Let me know if you have additional considerations or feedback to integrate!

### User - 2024-12-09 16:46:22

Add a Problem / Goal statement at the beginning

### Assistant - 2024-12-09 16:46:57

{"updates": [{"pattern": ".*", "replacement": "### Proposal for Process Changes\n\n#### Problem / Goal Statement\n\nOur current Software Development Life Cycle (SDLC) ties quarterly marketing launch moments directly to monthly product releases, creating rigid dependencies and limiting flexibility. This proposal aims to address these challenges by decoupling these processes, improving alignment between marketing and engineering, and enhancing the overall quality and visibility of our product development efforts.\n\nThis document outlines proposed adjustments to our existing SDLC and related workflows, aiming to enhance efficiency, align marketing and engineering timelines, and improve product quality.\n\n#### Key Proposals\n\n1. **Decouple Launch Moments from Releases**\n   - **Current State**: Quarterly launch moments are tied to monthly releases, which creates rigid dependencies and scheduling conflicts.\n   - **Proposed Change**: Separate launch moments (quarterly, owned by Marketing) from releases (monthly, owned by Product/Engineering).\n     - The quarterly launch calendar will focus on external commitments and can use flexible timelines within the quarter.\n     - Marketing can leverage existing milestones, including betas, for impactful announcements.\n\n2. **Introduce Beta as a Default Phase for Major New Features**\n   - **Current State**: Features often go directly to General Availability (GA) without a structured beta phase.\n   - **Proposed Change**: All major new features will go through a mandatory beta phase before GA.\n     - GA dates will not be committed to until after the beta launch.\n     - Marketing can create launch moments around betas, leveraging buzz similar to competitor strategies (e.g., demo videos, Early Access Programs).\n\n3. **Standardize Quarterly Launch Timing**\n   - **Current State**: Launch timing lacks alignment with quarterly business goals.\n   - **Proposed Change**: Schedule quarterly launch moments in the second month of each quarter.\n     - This timing will maximize momentum from the launch event to drive deal closings in the final month of the quarter.\n     - Example: Target March 22 as the next launch date.\n\n4. **Streamline Monthly Release Processes**\n   - **Current State**: Monthly releases involve unnecessary overhead, detracting from changelog and documentation focus.\n   - **Proposed Change**: Optimize the monthly release process for minimal viable delivery:\n     - Focus on changelogs and internal documentation.\n     - Reduce dependencies on marketing or GA-readiness.\n\n#### Supporting Notes\n\n1. **Beta and GA Visibility**\n   - A structured beta phase will:\n     - Provide better visibility into progress and quality for stakeholders.\n     - Align expectations across teams, ensuring Sales and Technical Support have sufficient preparation.\n   - GA launches can still serve as secondary marketing moments if desired.\n\n2. **Consistency in Existing Processes**\n   - Many of these changes involve slight adjustments to our current SDLC and Product Planning processes.\n   - Greater consistency in following these processes will be critical to achieving intended outcomes.\n\n3. **Role Clarifications and Optimizations**\n   - Retain the TPM role but refine focus:\n     - **Engineering Managers (EMs)**: Responsible for project and team-level management.\n     - **TPMs**: Focused on initiative-level coordination.\n     - **PMs**: Encouraged to take on additional program management responsibilities.\n     - Expand Ron’s role to strengthen EPD/GTM bridging efforts, including release-related work.\n\n#### Next Steps\n\n1. Share this proposal with stakeholders (e.g., TPMs, EMs, PMs) for feedback.\n2. Gather input on:\n   - Feasibility of decoupling launches and releases.\n   - Practical challenges of enforcing a mandatory beta phase.\n   - Proposed timing for quarterly launches.\n3. Pilot the new processes in the upcoming quarter, iterating based on lessons learned.\n\n---\n\nPlease review and provide feedback to refine these proposals further before we finalize implementation.\n"}]}

### Tool (canmore.update_textdoc) - 2024-12-09 16:46:57

{"result": "Successfully updated text document with textdoc_id '67578c04c7108191b00753c4e513fffd'", "textdoc_id": "67578c04c7108191b00753c4e513fffd"}

### Assistant - 2024-12-09 16:46:57

I’ve added a Problem/Goal Statement at the beginning to provide context for the proposed changes. Let me know if there’s anything else you’d like to adjust or refine!

