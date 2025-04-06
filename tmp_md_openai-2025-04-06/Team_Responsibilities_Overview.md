# Team Responsibilities Overview

Created: 2024-10-09 16:16:33
Last Updated: 2024-10-09 16:35:52

### User - 2024-10-09 16:16:33

Goal: have a map of different team responsibilities that summarizes each team's scope in 1-3 sentences. It should focus on areas of ownership, not specific projects and technologies. Gaps should be called out separately.

Here are the discussion notes to use to seed this list
Erika Rice Scherpelz How are you all thinking about the identities of your team. Should we rewrite a quick 3 sentence blurb on our teams missions / responsibilities. 

What does everything think is the scope of their team? And then we can identify gaps. 
Eric Shamow- abuse, self service Cody, billing for Cody Enterprise - anything Cody Enterprise admin 
Cloud Ops 
Core Services - dotcom, MSP, consult on service shape at Sourcegraph (Authentication, authorization, platform for scalable services). Defacto owners of things we’ve been breaking out of dotcom
Matt Manela- 
Graph - code navigation, code intelligence, precise indexers and how we differentiate in that space, 
Source - source code, permission handling, licensing, core infrastructure for MT 
Search platform - core search service / back end, symbols, cody context API integration and making Cody have bes context 
Peter Guy- Search 
Code search, batch changes, code monitoring, executors, Cody UI (Cody Web, Cody Chat)
Taking on a lot more user experience related work
Diego Comas- Security
Security engineering, operations, GRC, application security SDLC, secure architecture, 3rd party, monitoring and threat detection,incident response, corporate security, security automation, security compliance 
Grace Shih 
Cody chat experience, autocomplete, Cody API 

Erika Rice Scherpelz what are the gaps? What feels unknown in practice or theory?
Eric Shamow ownership for Cody Architecture - missing concrete ownership of what this architecture looks like.    
Peter Guy Executors - an uncomfortable thing for his team to own. Browser extensions (not necessarily unowned but not high enough priority). 
Release team - Migrator - very painful and misunderstood  
Graph context - want graph team more involved and partially in half hackathon effort 
Cody API - feels like still in transition / ramp up from Olaf.

### Assistant - 2024-10-09 16:16:41



### Assistant - 2024-10-09 16:16:41

{
  "name": "team_scope_summary",
  "type": "document",
  "content": "**Summary of Team Responsibilities**\n\n**Abuse & Billing** (Eric Shamow): Responsible for abuse prevention and mitigation, self-service capabilities for Cody, and billing for Cody Enterprise. Ownership also includes anything related to Cody Enterprise administration.\n\n**Cloud Operations**: Oversees the operational aspects of cloud infrastructure, ensuring reliability and scalability.\n\n**Core Services**: Responsible for dotcom services, managed service provider (MSP) offerings, and consulting on service shape at Sourcegraph, including authentication, authorization, and platform elements for scalable services. Also the de facto owners of services that are being separated out from dotcom.\n\n**Graph Team** (Matt Manela): Manages code navigation and code intelligence, focusing on precise indexers and differentiation in the code navigation space.\n\n**Source Team**: Focuses on handling source code, permissions, licensing, and core infrastructure for multi-tenant environments.\n\n**Search Platform**: Handles the core search service backend, symbols, and Cody context API integration, aiming to provide the best context for Cody.\n\n**Search Team** (Peter Guy): Manages code search, batch changes, code monitoring, executors, and the Cody UI (including Cody Web and Cody Chat). Also expanding responsibilities to include more user experience work.\n\n**Security Team** (Diego Comas): Covers security engineering and operations, GRC (governance, risk management, and compliance), application security, secure development lifecycle (SDLC), secure architecture, third-party risk management, monitoring and threat detection, incident response, corporate security, and automation of security processes.\n\n**Cody Team** (Grace Shih): Focused on enhancing the Cody chat experience, autocomplete features, and the Cody API.\n\n**Identified Gaps**:\n- **Cody Architecture**: There is no clear ownership of Cody's architecture, which needs defined leadership.\n- **Executors**: Ownership is currently with the Search team but feels uncomfortable due to prioritization challenges.\n- **Browser Extensions**: Not unowned, but lacks the necessary prioritization for effective progress.\n- **Migrator (Release Team)**: Painful and misunderstood process that requires more clarity.\n- **Graph Context**: There is a desire for more involvement from the Graph team in providing context, with current efforts being inconsistent.\n- **Cody API**: Ownership and responsibilities are still in transition after Olaf's departure."
}

### Tool (canmore.create_textdoc) - 2024-10-09 16:16:41

{"result": "Successfully created text document 'team_scope_summary' which will be referenced in all future messages with the unique identifier textdoc_id: '67070ed8dfc881919f9544d9df83b3f6'", "textdoc_id": "67070ed8dfc881919f9544d9df83b3f6", "name": "team_scope_summary"}

### Assistant - 2024-10-09 16:16:41

Here's the initial summary of team responsibilities along with identified gaps. Let me know if you'd like to make any adjustments or add more details to this overview.

### User - 2024-10-09 16:34:25

Suggest 5 different names for the Code Search team

### Assistant - 2024-10-09 16:34:27

{
  "comments": [
    {
      "pattern": "\\*\\*Code Search\\*\\*:.*?\\.",
      "comment": "Consider renaming 'Code Search' to a more distinct and descriptive name. Here are five suggestions: 1) 'Code Discovery,' 2) 'Search & Insights,' 3) 'Code Insights Team,' 4) 'SearchWorks,' 5) 'CodeQuest.' These names could better reflect the team's focus and scope."
    }
  ]
}

### Tool (canmore.comment_textdoc) - 2024-10-09 16:34:27

{"result": "Successfully added comments to text document with textdoc_id '67070ed8dfc881919f9544d9df83b3f6'", "textdoc_id": "67070ed8dfc881919f9544d9df83b3f6"}

### Assistant - 2024-10-09 16:34:27

I've suggested potential new names for the "Code Search" team that might better capture its scope and responsibilities. Let me know if any of these resonate or if you'd like further brainstorming on this.

### User - 2024-10-09 16:35:49

What are some other ideas that get at different angles of the scope?

### Assistant - 2024-10-09 16:35:51

{
  "comments": [
    {
      "pattern": "\\*\\*Code Search\\*\\*:.*?\\.",
      "comment": "Consider exploring alternative names that highlight different facets of the team's scope. Here are some angles you could emphasize: 1) Discovery and insights ('Code Explorer', 'Code Insights'), 2) User experience focus ('Search Experience Team'), 3) Technical depth ('Deep Code Search'), 4) Holistic integration ('Unified Search'), 5) Emphasis on change management ('Change Navigator')."
    }
  ]
}

### Tool (canmore.comment_textdoc) - 2024-10-09 16:35:51

{"result": "Successfully added comments to text document with textdoc_id '67070ed8dfc881919f9544d9df83b3f6'", "textdoc_id": "67070ed8dfc881919f9544d9df83b3f6"}

### Assistant - 2024-10-09 16:35:51

I've suggested some alternative naming ideas for the "Code Search" team that focus on different aspects of its responsibilities. Let me know if any of these directions resonate, or if you'd like to explore other angles.

