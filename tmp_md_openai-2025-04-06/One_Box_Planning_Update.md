# One Box Planning Update

Created: 2024-11-19 10:52:03
Last Updated: 2024-11-19 11:00:23

### User

*[user_editable_context content]*

### User - 2024-11-19 10:52:03

Start a draft with this content:

During our planning offsite, The one box team moved one box from existential-feeling risk to a plan that is still ambitious by which has scoped, understood risks. We focused our discussion and planning on natural language search, personalization, and overall user experience. 
Accomplishments:
Milestone planning: We established a detailed set of milestones for one box, focusing on the higher risk areas: integrating natural language search, intent detection, and search personalization. Each milestone was broken down into actionable items, including risk assessment and dependency identification.
UI/UX design and review: We reviewed and iterated on a unified design for the one box interface. Some key focus areas included overall design, scopes, filters, and search personalization.
Implementation: We spent some time on implementation, including moving search results to use the search API (instead of the Cody context API), testing intent detection on CPU (decided to defer post Jan 29th), and a proof of concept for replacing Lexical with ProseMirror. 
November 28th: The focus of this milestone is getting internal feedback. It will include:
Initial version of natural language search built on streaming search API
Updated UI for scopes
Chat input component improvements
Intent detection improvements
Risks and mitigations: 
Ranking quality and intent detection: These remain significant technical risks, and the team will iterate on them throughout the next two months. To mitigate these, we have put a strong emphasis on collecting high-quality training data and refining the underlying models through iterative testing.
Cross-team alignment: The parallel development efforts across multiple work streams pose risks related to misalignment and dependencies. The team is putting coordination mechanisms in place to address this (e.g., meetings, async updates).

### Assistant - 2024-11-19 10:52:09



### Assistant - 2024-11-19 10:52:09

{
  "name": "one_box_update",
  "type": "document",
  "content": "During our planning offsite, the One Box team moved one major risk from existential-feeling uncertainty to a plan that is still ambitious but scoped, with understood risks. Our focus was on natural language search, personalization, and overall user experience.\n\n**Accomplishments:**\n- **Milestone Planning**: We established a detailed set of milestones for One Box, concentrating on higher-risk areas such as integrating natural language search, intent detection, and search personalization. Each milestone was broken down into actionable items, including risk assessments and dependency identification.\n- **UI/UX Design and Review**: We reviewed and iterated on a unified design for the One Box interface, with key focus areas including overall design, scopes, filters, and search personalization.\n- **Implementation**: We worked on implementation tasks such as moving search results to use the Search API instead of the Cody Context API, testing intent detection on CPU (deferred until after January 29th), and a proof of concept for replacing Lexical with ProseMirror.\n\n**Next Milestone: November 28th**\nThe focus of this milestone is to gather internal feedback. It will include:\n- Initial version of natural language search built on the streaming Search API\n- Updated UI for scopes\n- Chat input component improvements\n- Intent detection improvements\n\n**Risks and Mitigations:**\n- **Ranking Quality and Intent Detection**: These remain significant technical risks, and the team will iterate on them throughout the next two months. To mitigate these, we are emphasizing high-quality training data collection and refining the underlying models through iterative testing.\n- **Cross-Team Alignment**: Parallel development across multiple work streams poses risks related to misalignment and dependencies. To mitigate these, we are establishing coordination mechanisms, such as regular meetings and async updates, to ensure alignment." 
}

### Tool (canmore.create_textdoc) - 2024-11-19 10:52:09

{"result": "Successfully created text document 'one_box_update' which will be referenced in all future messages with the unique identifier textdoc_id: '673cde5894e481919e2bb45d670e622c'", "textdoc_id": "673cde5894e481919e2bb45d670e622c", "name": "one_box_update"}

### Assistant - 2024-11-19 10:52:09

I've drafted an update based on your offsite discussion for the One Box team. Let me know if there are any specific parts you'd like to elaborate on or if there's anything else you need. Also, remember to reflect on how you can build trust and alignment with other teams, especially given the cross-team challenges mentioned.

### User - 2024-11-19 10:52:30

What is in the summary below that is missing from the summary on the right? Where are they inconsistent?

One Box offsite summary
Eight members of the one box team met in Holland last week with the goal of quickly aligning on some technical decisions, then getting to work on the product. On the first day, we discovered that there were more open questions than were answerable in a single day. No matter, we had two full days remaining. This occurred every day.
Despite deviating from the plan, by the end of the offsite we had defined the major components, de-risked several major issues, and aligned on the work required for each. A bit about each major component:
Natural Language Search
A simple code search syntax that supports 70% of search use cases. It will leverage the same @scope contexts that chat currently uses and be driven by a new pattern type
There are three sub-projects here:
Creating a new pattern type to support this merger :white_check_mark:
Designing and building @scope chips in search
Personalization and ranking
This project will continuously evolve as we measure search quality against our developing benchmarks
Julie Tibshirani and Camden Cheek will own this component.
Intent detection
Intent detection is a lightweight ML model we are training that runs while the user is forming their question. It determines if the query is best served by code search or the LLM, then directs the response to either chat or search as required. We are also designing it to be extensible for other intents in FY26.
Like Natural Language Search, this project will continuously evolve as we improve training data and methods.
Jan Hartman owns this component and has already retrained the model and is seeing better results.
One box interface interaction
This project forms the basis of the user experience and informs how users search, use results in follow-ups, interface with code navigation on the web, and interact between the IDE and the web.
Subprojects:
A new, more expressive, and extensible input. Felix has begun implementing this effort.
Improved context selection and suggestion functionality (currently in design)
Responsive designs between the web and IDE panels
Naman Kumar owns the build component of this project supported by Felix Kling
Rob Rhyne owns the design component with support from Taiyab Raja
Finally, we planned the scope of three releases:
November 28th (linear) - designed to get better internal feedback
December 18th - designed for EAP style external feedback
January 15th - one box GA
Thanks to everyone who met for several long days with very few breaks to hash all of this out. We're already seeing lots of momentum:
The new new patterntype:nls, has been merged by 
@Julie
 and 
@Camden Cheek
. This will power one box search.
A new version of the intent model has been trained by 
@Jan Hartman
The new input was started by 
@Felix Kling
 and is based on ProseMirror by the creator of CodeMirror
Finally, 
@Erika RS
 will have an update for us with her take.

### Assistant - 2024-11-19 10:52:42

Here’s a detailed comparison between the offsite summary on the left and the One Box summary in the current document:

### Missing Details in the Document:
1. **Team Members and Offsite Setting:**
   - The left summary explicitly mentions eight members of the One Box team meeting in Holland and their goal of aligning on technical decisions before diving into product work.
   - The current document lacks details about who attended, where it was held, or the context for the offsite. Adding these details would help humanize the experience and show the scale of the planning efforts.

2. **Evolution of the Planning Process:**
   - The left summary narrates how the planning deviated from expectations, with more open questions arising each day, yet still making significant progress.
   - This storytelling aspect adds a dimension of how challenges were faced and overcome during the offsite, which is missing in the current summary.

3. **Major Components and Ownership:**
   - The left summary breaks down each major component—Natural Language Search, Personalization and Ranking, Intent Detection, and Interface Interaction. It also names the specific owners for each sub-project (e.g., Julie Tibshirani and Camden Cheek for Personalization, Jan Hartman for Intent Detection).
   - The current document lists achievements but does not assign ownership or mention individuals responsible for specific tasks. Including this could help clarify accountability and recognition for the team.

4. **Sub-Projects Breakdown:**
   - The left summary contains a clear breakdown of the sub-projects for each major component, such as:
     - Natural Language Search, which has three sub-projects, including creating a new pattern type and building @scope chips.
     - Input design using ProseMirror.
   - The current document mentions some tasks at a high level, like moving search results to use a new API and a proof of concept for replacing Lexical with ProseMirror, but it does not provide the same granular breakdown of ongoing sub-projects or who’s leading them.

5. **Upcoming Releases and Schedule:**
   - The left summary lays out three planned releases: November 28th, December 18th, and January 15th, including the goals for each phase.
   - The current document only includes the November 28th milestone without mentioning the broader release schedule.

6. **Recent Progress and Recognition:**
   - The left summary highlights specific recent progress, like merging the new pattern type, training a new version of the intent model, and starting on the new input based on ProseMirror.
   - Recognizing specific team members and their contributions helps reinforce accountability and morale, which is absent in the current document.

### Inconsistencies:
1. **Intent Detection:**
   - The left summary describes intent detection as an ML model that determines whether a query is best served by code search or an LLM, providing detailed functional insights.
   - The current document mentions intent detection improvements but lacks depth on what the model is specifically designed to do or how it will evolve.

2. **Milestones vs. Releases:**
   - In the left summary, the milestones are clearly tied to the releases scheduled through January, with explicit goals for each stage.
   - The current document mentions only the November 28th milestone and its focus, omitting the longer-term timeline and broader release goals.

3. **Communication Style and Tone:**
   - The left summary includes a casual tone, mentioning that team members “met for several long days with very few breaks” and acknowledging everyone’s effort.
   - The current summary is more formal and lacks this element of appreciation for the hard work, which could make it feel less personal and motivating.

### Potential Enhancements:
- Including **team member names and roles** would enhance clarity around ownership and accountability.
- Adding **context on the location and nature of the offsite** would help provide more human connection and background.
- Emphasizing the **challenges faced during planning** would make the summary feel more authentic and relatable.
- Highlighting the **broader timeline for releases** would give a better understanding of long-term goals.
  
Would you like me to update the current document to reflect any of these additions?

### User - 2024-11-19 10:55:28

Add a paragraph at the end of the current version which thanks Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for their contributions to the planning

### Assistant - 2024-11-19 10:55:35

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "During our planning offsite, the One Box team moved one major risk from existential-feeling uncertainty to a plan that is still ambitious but scoped, with understood risks. Our focus was on natural language search, personalization, and overall user experience.\n\n**Accomplishments:**\n\n- **Milestone Planning**: We established a detailed set of milestones for one box, concentrating on higher-risk areas such as integrating natural language search (including ranking and search personalization), intent detection, and overall interface interactions (including scopes and filters). Each milestone was broken down into actionable items, including risk assessments and dependency identification.\n- **UI/UX Design and Review**: We reviewed and iterated on a unified design for the One Box interface, with key focus areas including overall design, scopes, filters, and search personalization.\n- **Implementation**: We worked on implementation tasks such as moving search results to use the Search API instead of the Cody Context API, testing intent detection on CPU (deferred until after January 29th), and a proof of concept for replacing Lexical with ProseMirror.\n\n**Next Milestone: November 28th**\nThe focus of this milestone is to gather internal feedback. It will include:\n\n- Initial version of natural language search built on the streaming Search API\n- Updated UI for scopes\n- Chat input component improvements\n- Intent detection improvements\n\n**Risks and Mitigations:**\n\n- **Ranking Quality and Intent Detection**: These remain significant technical risks, and the team will iterate on them throughout the next two months. To mitigate these, we are emphasizing high-quality training data collection and refining the underlying models through iterative testing.\n- **Cross-Team Alignment**: Parallel development across multiple work streams poses risks related to misalignment and dependencies. To mitigate these, we are establishing coordination mechanisms, such as regular meetings and async updates, to ensure alignment.\n\nA huge thank you to Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for their invaluable contributions to the planning process. Your efforts were instrumental in making significant progress and aligning on the ambitious goals we set for One Box."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-11-19 10:55:35

{"result": "Successfully updated text document with textdoc_id '673cde5894e481919e2bb45d670e622c'", "textdoc_id": "673cde5894e481919e2bb45d670e622c"}

### Assistant - 2024-11-19 10:55:35

I've added a paragraph at the end to thank Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for their contributions to the planning. Let me know if there's anything else you'd like to adjust or add!

### User - 2024-11-19 10:55:42

Give the current verion an overall more casual tone. 

### Assistant - 2024-11-19 10:55:49

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "During our planning offsite, the One Box team took one of our biggest risks from a feeling of existential uncertainty to a plan that's still ambitious, but now scoped and with clear risks we understand. Our focus was on natural language search, personalization, and overall user experience.\n\n**What We Got Done:**\n\n- **Milestone Planning**: We laid out a solid set of milestones for One Box, focusing on the riskier areas like integrating natural language search (including ranking and personalization), intent detection, and interface interactions (like scopes and filters). We broke each milestone down into actionable steps, with risk assessments and a look at dependencies.\n- **UI/UX Design and Review**: We reviewed and iterated on a unified design for the One Box interface. We zeroed in on things like overall design, scopes, filters, and making search more personalized.\n- **Implementation**: We got our hands dirty with implementation work, including moving search results over to use the Search API instead of the Cody Context API, testing intent detection on CPU (which we've pushed to after January 29th), and putting together a proof of concept for replacing Lexical with ProseMirror.\n\n**Next Milestone: November 28th**\nThe goal for this milestone is to gather some internal feedback. Here's what it will cover:\n\n- Initial version of natural language search built on the streaming Search API\n- Updated UI for scopes\n- Improvements to the chat input component\n- Enhancements to intent detection\n\n**Risks and How We're Handling Them:**\n\n- **Ranking Quality and Intent Detection**: These are still pretty big technical risks, so we’re planning to keep iterating on them over the next two months. To stay ahead of these challenges, we’re focusing on collecting high-quality training data and refining our models through iterative testing.\n- **Cross-Team Alignment**: With multiple work streams running in parallel, there’s always a risk of things getting misaligned or dependencies falling through the cracks. To keep everyone on the same page, we’re putting in place coordination tools like regular meetings and async updates.\n\nA huge thank you to Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for all your amazing contributions to the planning process. Your efforts made a huge difference, and we’re already seeing the momentum towards hitting our ambitious goals for One Box."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-11-19 10:55:49

{"result": "Successfully updated text document with textdoc_id '673cde5894e481919e2bb45d670e622c'", "textdoc_id": "673cde5894e481919e2bb45d670e622c"}

### Assistant - 2024-11-19 10:55:49

I've adjusted the text to make it more casual, focusing on a friendly and conversational tone. Let me know if this works for you or if you'd like any further tweaks!

### User - 2024-11-19 10:56:46

The current version is going to be shared along side a reshare of the version on the left. Make the current version more of a high level tl;dr executive summary of the offsite which explicitly references "Rob's post" for those wanting more detail

### Assistant - 2024-11-19 10:56:51

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "During our planning offsite, the One Box team tackled a major risk, turning an uncertain and existential challenge into an ambitious but clearly scoped plan. We focused on three main areas: natural language search, personalization, and overall user experience. \n\nHere's a quick high-level overview of what we accomplished:\n\n- Defined key milestones and broke down work into actionable steps, focusing on high-risk components like natural language search and intent detection.\n- Made significant progress on a unified UI/UX design, including scopes, filters, and personalization improvements.\n- Got started with implementation, including moving search results to the new Search API and experimenting with ProseMirror for a more expressive input.\n\nOur next milestone on November 28th aims to gather internal feedback on core components, including natural language search, scopes, and intent detection.\n\nFor those wanting more detailed insights, please refer to Rob's post, which goes deeper into each component, the sub-projects, and specific contributions made by the team members.\n\nThanks again to Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for all your incredible work and commitment throughout this offsite."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-11-19 10:56:51

{"result": "Successfully updated text document with textdoc_id '673cde5894e481919e2bb45d670e622c'", "textdoc_id": "673cde5894e481919e2bb45d670e622c"}

### Assistant - 2024-11-19 10:56:51

I've transformed the current version into a high-level executive summary and explicitly referenced Rob's post for more details. Let me know if there's anything else you'd like to adjust.

### User - 2024-11-19 10:57:23

Make "One Box" lower case ("one box") throughout.

### Assistant - 2024-11-19 10:57:25

{
  "updates": [
    {
      "pattern": "\\bOne Box\\b",
      "multiple": true,
      "replacement": "one box"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-11-19 10:57:25

{"result": "Successfully updated text document with textdoc_id '673cde5894e481919e2bb45d670e622c'", "textdoc_id": "673cde5894e481919e2bb45d670e622c"}

### Assistant - 2024-11-19 10:57:25

I've changed "One Box" to "one box" throughout the document. Let me know if there's anything else you'd like me to adjust.

### User - 2024-11-19 11:00:16

Sprinkle in a few tasteful emojis

### Assistant - 2024-11-19 11:00:22

{
  "updates": [
    {
      "pattern": "planning offsite in Amsterdam",
      "replacement": "planning offsite in Amsterdam 🇳🇱"
    },
    {
      "pattern": "turned an uncertain and open ended challenge into an ambitious but clearly scoped plan",
      "replacement": "turned an uncertain and open-ended challenge into an ambitious but clearly scoped plan ✨"
    },
    {
      "pattern": "natural language search, intent detection, and one box interface interaction",
      "replacement": "natural language search, intent detection, and one box interface interaction 🔍🤖💡"
    },
    {
      "pattern": "high-level overview of what we accomplished",
      "replacement": "high-level overview of what we accomplished 📋"
    },
    {
      "pattern": "significant progress on a UI/UX design, including scopes, filters, and search personalization improvements",
      "replacement": "significant progress on a UI/UX design, including scopes, filters, and search personalization improvements 🎨"
    },
    {
      "pattern": "November 28th aims to gather internal feedback",
      "replacement": "November 28th aims to gather internal feedback 🗓️"
    },
    {
      "pattern": "Thanks again to Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for all your incredible work and commitment throughout this offsite",
      "replacement": "Thanks again to Rob, Peter, Taiyab, Camden, Felix, Naman, and Jan for all your incredible work and commitment throughout this offsite 🙌"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-11-19 11:00:22

{"result": "Successfully updated text document with textdoc_id '673cde5894e481919e2bb45d670e622c'", "textdoc_id": "673cde5894e481919e2bb45d670e622c"}

### Assistant - 2024-11-19 11:00:22

I've added some tasteful emojis to enhance the document's tone and make it a bit more engaging. Let me know if you need any further tweaks! 😊

