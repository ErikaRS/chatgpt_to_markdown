# Linear Style Guide Draft

Created: 2025-03-07 06:55:24
Last Updated: 2025-03-13 07:05:51

### User

*[user_editable_context content]*

### User - 2025-03-07 06:55:24

Linear is an issue an project tracking system. Its basic hierarchy is initiatives which contain projects and projects contain issues and issues can contain sub issues. A project can be in multiple initiatives and can be owned by multiple teams. An issue could only be in a single project and can only be owned by a single team. 

Initiatives exist at the workspace, i.e. company level. Projects should have names that are meaningful to those outside the project. Items within projects such as milestones, which are merely a way of grouping issues within a project, issues, and sub issues should be organized at the discretion of the project owners. 

Projects can have statuses which reflect the state of the project: idea, next up, scoping, implementation, pre-release, EAP, experimental, beta, ga, completed. 

Using this as a starting point, create a linear style guide. This should include such details as what is the scope of an initiative versus a project, how names of initiatives and projects should be to be useful to the reader, and any other things that seem like they would be typical in a project management style guide.

### Assistant - 2025-03-07 06:55:33



### Assistant - 2025-03-07 06:55:24

This is a great challenge! Before I dive in, can you confidently create a first draft of this Linear style guide on your own? If not, I can suggest a section you might try outlining yourself before we complete the whole thing together. If you *can* do it, I can also guide you toward more elegant or comprehensive ways to make it effective—like examples from other orgs, best practices in naming conventions, or scaling guidelines. Would you like that?  

Meanwhile, here’s a big-picture framing to help you engage with the complexity of this task:  

### Context & Skills  
A style guide like this touches on:  
- **Information architecture**: How to structure work so it’s understandable across the org.  
- **Communication norms**: Naming, clarity, and audience awareness.  
- **Governance**: Who decides what's “correct” and ensures consistency.  
- **Change management**: Making the guide itself a living document that evolves as practices mature.  
- **Cross-team empathy**: Creating systems that work for both project participants and readers who only occasionally interact with the work.  

Roles who might care: engineering leadership, program managers, product managers, design leads, and anyone involved in cross-team initiatives.  

As you work on this, I suggest thinking about who else across your org would benefit from collaborating on or reviewing this guide to build mutual trust and respect—people who care about clarity and alignment across teams. You could run a lightweight working group or feedback session with people in different roles. I can help you design that if you want.  

Shall I go ahead and draft a full version of the style guide from the starting point you shared? And remind me at the end to help you reflect on what you’ve learned!

### User - 2025-03-07 06:56:17

Yes, please draft a full version from the starting point

### Assistant - 2025-03-07 06:56:17

Thanks! Here's a full draft of a **Linear Style Guide**, building from your structure and expanding into best practices. I'll flag opportunities for human connection and reflection at the end.

---

# Linear Style Guide

This style guide establishes best practices for organizing, naming, and maintaining Initiatives, Projects, Issues, and related elements in Linear, ensuring clarity, consistency, and usability across the workspace.

---

## 1. Purpose  
To create a shared system that:  
- Enables anyone in the company to understand the scope and status of work.  
- Supports cross-team collaboration.  
- Maintains long-term clarity and discoverability of work over time.  

---

## 2. Hierarchy Overview  

| Level        | Purpose                                      | Ownership                   | Audience                |
|--------------|----------------------------------------------|-----------------------------|-------------------------|
| **Initiative** | Cross-cutting, strategic outcomes or themes | Workspace-level (often leadership) | Whole company         |
| **Project**    | Time-bound effort delivering specific value | One or more teams           | Adjacent teams + company leadership |
| **Issue**      | Discrete, actionable work items            | Single team                 | Project contributors   |
| **Sub-Issue** | Smallest units of work within an issue      | Same as parent issue        | Direct assignees       |

---

## 3. Scope  

### Initiatives  
- Describe broad, high-level objectives or themes, often spanning multiple quarters.  
- Capture **why** this work matters at a strategic level.  
- Examples:  
  - “Improve Onboarding Experience”  
  - “Scale Infrastructure for 10x Traffic”  
  - “2025 Security & Compliance Goals”  

**Initiatives should NOT:**  
- Contain every project a team is doing.  
- Represent individual features or experiments.  

### Projects  
- Represent concrete efforts delivering value, typically over weeks or months.  
- Should be understandable **to people not directly involved**.  
- Can belong to multiple Initiatives.  

Examples:  
- “Self-Serve Team Invites” (supports “Improve Onboarding Experience”)  
- “Migrate Build System to Bazel” (supports “Scale Infrastructure”)  

---

## 4. Naming Conventions  

### Initiatives  
- Start with a **verb or goal-oriented phrase**.  
- Keep short but informative.  
- Assume a broad, company-wide audience.  

Format:  
> [Objective] – [Key Context]  
Examples:  
> "Reduce Onboarding Time – New User Journey"  
> "Achieve SOC 2 Compliance"  

### Projects  
- Use **descriptive names** meaningful outside the project team.  
- Avoid jargon or internal codenames unless they’re widely known.  
- Emphasize the problem or outcome.  

Format:  
> [Solution or Outcome] – [Feature/Area]  
Examples:  
> “Self-Serve Team Invites”  
> “Streamlined Checkout Flow”  

### Issues & Sub-Issues  
- Encourage actionable titles, written as clear tasks.  
- Example: “Update API docs for new authentication flow”  

---

## 5. Status Usage  
Projects should have an accurate status reflecting their phase:  

| Status         | When to Use                                           |
|----------------|-------------------------------------------------------|
| Idea          | Early concepts, not yet prioritized                    |
| Next Up       | Prioritized, starting soon                             |
| Scoping       | Defining requirements and approach                     |
| Implementation| Actively in development                                |
| Pre-Release   | Code complete, prepping for launch                     |
| EAP           | Early Access Program, limited user testing             |
| Experimental  | Trialing, unclear if it will stick                      |
| Beta          | Feature-complete but gathering feedback                |
| GA            | General Availability, fully released                   |
| Completed     | Fully shipped, with no further work planned            |

---

## 6. Milestones  
- Used for grouping Issues within Projects.  
- Can represent phases (e.g., "MVP," "V2 Improvements") or dates (e.g., "March 2025 Launch").  
- Optional but recommended for large projects.  

---

## 7. Ownership and Visibility  
- **Initiatives:** Owned by leadership or cross-functional stakeholders.  
- **Projects:** Must have clear team ownership.  
- **Issues:** Single team ownership only.  

---

## 8. Best Practices  

- **Archiving:** Regularly archive completed or obsolete Initiatives and Projects to keep Linear clean.  
- **Cross-Linking:** Link related Projects, Initiatives, and Issues so context is easy to find.  
- **Retrospectives:** Upon completing major Projects, add a comment with key learnings for future reference.  
- **Review Cadence:** Revisit Initiative and Project statuses quarterly to avoid stale work.  
- **Documentation:** Link to external docs (e.g., Notion, Google Docs) from Project descriptions.  

---

## 9. Examples  

### Initiative  
**Name:** Reduce Onboarding Time – New User Journey  
**Purpose:** Decrease time from signup to first successful action.  
**Projects:**  
- Self-Serve Team Invites  
- Streamlined Signup Flow  

### Project  
**Name:** Self-Serve Team Invites  
**Purpose:** Allow users to invite teammates without admin approval.  
**Status:** Implementation  
**Milestones:**  
- MVP  
- Admin Controls  
- Launch  

---

## 10. Maintenance  
Assign a “Linear Hygiene” owner in each team to:  
- Monitor for drift in naming and statuses.  
- Ensure archival of stale Projects and Initiatives.  
- Facilitate quarterly cleanups.

---

## Final Thoughts  
### Building Human Connection  
- Host cross-team reviews of Initiatives and Projects to align language and goals.  
- Pair less experienced Project leads with mentors on naming and scope-setting.  
- Celebrate well-maintained Projects in public Slack channels to model good practices.  

### Reflection  
After we wrap this, please set yourself a reminder to reflect:  
- What was hardest to clarify?  
- What patterns do you notice about what helps make work clear across teams?  
- What habits from this guide might influence how you work elsewhere?  

Would you like help setting up a feedback process or review loop for the guide itself?  

And before we close—would you like to debrief this interaction together? I can offer what worked well, what we could refine, and invite your thoughts.

### User - 2025-03-07 07:01:48

Linear can also support fairly advanced views. Suggest some views that are useful at an leadership level.

### Assistant - 2025-03-07 07:01:48

Great expansion! Before I suggest these, do you feel confident designing leadership-level views in Linear? If not, maybe you could try sketching one or two first, and I can support you with feedback. If you *are* comfortable, I can also help you explore more sophisticated setups, like cross-cutting dashboards, historical trend tracking, or portfolio management patterns—would you like that?

For context, creating leadership views is a chance to apply systems thinking and highlight the difference between **operational management** (day-to-day tasks) and **portfolio oversight** (alignment to strategic goals, resource allocation, risk identification). These views should serve the leadership team by answering questions like:
- Are we doing the right things?
- Are we on track?
- Where are the risks?
- How balanced is our investment across priorities?

Building trust here could mean co-designing these views with peer leaders and sharing how you expect them to use the information. It’s also a great way to involve someone who cares about metrics or visibility across teams.

---

## Suggested Leadership-Level Views in Linear  

### 1. **Strategic Initiative Health Overview**  
A board view grouped by Initiative showing:  
- Each active Initiative.  
- The associated Projects.  
- Current status of those Projects (e.g., % complete, current phase).  
- Owners and recent updates.  

**Purpose:** High-level progress toward strategic company goals.

---

### 2. **Project Status by Phase**  
A list or board view filtering for Projects in statuses like:  
- Scoping  
- Implementation  
- Pre-Release  

**Sort by:** Last updated or target completion date.  
**Purpose:** Identify bottlenecks, slow-moving Projects, or areas needing intervention.

---

### 3. **Risk & Blockers View**  
A custom view showing all Issues flagged with labels like:  
- “Blocked”  
- “At Risk”  
- “Needs Leadership Input”  

**Group by:** Project or team.  
**Purpose:** Quickly spot where leadership support is needed.

---

### 4. **Resource Allocation Heatmap (by Team)**  
View of active Projects grouped by owning team with visible workloads:  
- Number of active Issues per team.  
- Number of active Projects per team.  
- Initiative overlap.  

**Purpose:** Spot over/underloaded teams and adjust priorities.

---

### 5. **Milestone Tracking Across Key Projects**  
A timeline (or list) of upcoming Milestones across high-priority Projects.  
**Filters:** Projects in critical Initiatives or those marked as "Next Up"/"Implementation."  
**Purpose:** Surface major upcoming deadlines and coordinate dependencies.

---

### 6. **Recently Completed Projects**  
A historical log of Projects marked as "Completed" in the past 30-90 days.  
Include:  
- Completion date.  
- Link to retrospective (if available).  
- Outcome summary.  

**Purpose:** Celebrate progress and gather insights on delivery pace.

---

### 7. **Initiatives Without Active Projects**  
A filter to identify Initiatives that currently have no active Projects.  
**Purpose:** Flag strategic goals that may be neglected or stalled.

---

### 8. **Cross-Team Collaboration View**  
A view showing Projects with multiple owning teams, sorted by status and updated date.  
**Purpose:** Ensure cross-team work stays aligned and visible.

---

### Want to go further?  
Would you like help setting up:
- A shared leadership dashboard that combines these?  
- A regular review ritual (monthly or quarterly) using these views?  
- Auto-updating reports that post summaries into Slack or docs?

And don’t forget—after we wrap this work, reflect on which views seem most valuable, and consider asking your peers what visibility gaps they experience. This is a great way to deepen collaboration across the leadership team.

Would you like to debrief this interaction too?

### User - 2025-03-07 07:03:40

Update the style guide to add conventions around linear project status. Let me know if you need the list of statuses linear supports. If you already know them, just go ahead

### Assistant - 2025-03-07 07:03:40

I have the standard Linear statuses you listed earlier (Idea, Next Up, Scoping, Implementation, Pre-Release, EAP, Experimental, Beta, GA, Completed), so I’ll proceed. Here's an **updated section for the style guide**, integrating conventions on how and when to use project statuses effectively:

---

## **5. Status Usage and Conventions**  

Project status is essential for communicating where work stands and helping leadership and other teams understand progress at a glance. Keep statuses **accurate and up to date**—they’re not just labels; they are signals to the entire organization.  

### **Standard Statuses and When to Use Them:**  

| Status         | Definition & When to Use                                | Owner Responsibility                         |
|----------------|---------------------------------------------------------|----------------------------------------------|
| **Idea**          | Early, rough concept. Not yet prioritized.             | Optional to create. Should be cleared out quarterly. |
| **Next Up**       | Prioritized and intended to begin soon (within a cycle or two). | Confirm problem, rough scope, and team resourcing. |
| **Scoping**       | Actively defining requirements, goals, and approach.   | Create initial Milestones and draft Issues. |
| **Implementation**| Actively being worked on. Most Issues in progress.     | Regular status updates and milestone tracking. |
| **Pre-Release**   | Feature/code complete; focused on testing, docs, and final prep. | Final validations before user-facing release. |
| **EAP (Early Access Program)** | Limited release to selected users for real-world testing. | Active feedback loop with users and support. |
| **Experimental**  | Trial work to assess viability. May not move forward.  | Set clear success criteria upfront.         |
| **Beta**         | Broad release, but actively gathering feedback and making improvements. | Monitor performance and adoption closely. |
| **GA (General Availability)**| Fully launched, complete for general use.    | Ensure full documentation, support coverage, and observability. |
| **Completed**     | Fully shipped and considered done. No further planned work. | Add a retrospective link or final summary comment. |

---

### **Conventions for Status Use:**  

1. **Keep statuses fresh**  
   Outdated statuses reduce trust. Review and update at least every two weeks or during regular team rituals (like planning).  

2. **Advance statuses deliberately**  
   Moving from one status to the next should reflect a meaningful change:  
   - From **Next Up** to **Scoping**: You’ve committed time to figure out *how* to solve the problem.  
   - From **Scoping** to **Implementation**: You’re confident in scope, team, and feasibility.  

3. **Only one active status per Project**  
   Even if a Project has multiple Milestones or phases, the overall Project reflects its current primary state.  

4. **Experimental vs. EAP vs. Beta**  
   - Use **Experimental** when it's unclear if this is worth building.  
   - Use **EAP** for controlled external feedback with select users.  
   - Use **Beta** for broad but provisional release.  

5. **GA and Completed are different**  
   - **GA** = Fully launched and supported.  
   - **Completed** = Project has wrapped, and no further work is planned. You should archive or close it out soon after.  

6. **Projects stuck in a status?**  
   If a Project has been sitting in the same status without progress for over a month, trigger a review. It may need re-scoping, de-prioritization, or closure.

---

Would you like this integrated into the full guide?  
And after this addition, it might be worth reflecting:  
- What behaviors are you hoping to shift with clear status conventions?  
- Who could you engage to model excellent status hygiene and help set the standard across teams?  

Would you like to debrief this work as well?

### User - 2025-03-07 07:03:57

Sorry, I meant the project priority not the product status.

### Assistant - 2025-03-07 07:03:57

Ah! Thanks for the clarification—you mean **project priority** (like High, Medium, Low), not status in the workflow sense. That’s an important distinction. I’ll add a new section to the style guide to cover **priority conventions** for projects.

---

## **6. Project Priority Conventions**  

Priority helps the organization understand **how important a project is relative to others**. It is a tool for focus—not urgency—and should reflect alignment to strategic goals, impact, and resourcing.

### **Standard Priority Levels:**  

| Priority | Meaning | When to Use |
|----------|---------|-------------|
| **High** | Critical, top-priority work that the team is actively focused on. Delay would cause major impact. | - Tied to a strategic Initiative or company goal.<br>- Has leadership visibility.<br>- Requires sustained effort and regular updates. |
| **Medium** | Important but not critical. In progress or planned, but can be deferred if necessary. | - Valuable, but less urgent.<br>- May be blocked by other work.<br>- Often running in parallel with higher-priority work. |
| **Low** | Nice-to-have, exploratory, or backlog work. Limited impact if delayed or paused. | - Early ideas or small improvements.<br>- Background tasks that are opportunistic.<br>- Often paused when higher-priority work comes up. |

---

### **Conventions for Using Priority:**  

1. **Assign a priority to every active project**  
   Every Project that is not Completed or Archived should have a priority set to aid in planning and communication.

2. **Be realistic**  
   Not everything can be High priority. Use High sparingly so it retains meaning. If many Projects are marked High, none of them are.

3. **Update priorities regularly**  
   Review priorities in regular planning cycles (monthly or quarterly). Priorities should reflect the *current* state of the business.

4. **Use priority to guide resource allocation**  
   - High = Ensure the team is fully staffed and supported.  
   - Medium = Proceed, but expect possible interruptions.  
   - Low = No guaranteed resources; work when possible.

5. **Communicate priority shifts**  
   If a Project's priority changes (especially down), notify stakeholders. This builds trust and helps avoid surprises.

6. **Connect priority to Initiatives**  
   If a Project supports a High-priority Initiative, its priority should generally match unless there's a strong reason not to.

---

### **Optional: Portfolio Views Based on Priority**  
For leadership, create filtered views like:  
- **All High-Priority Projects by Team**  
- **High-Priority Projects Without Recent Updates**  
- **Medium/Low Projects That Haven’t Moved in 60 Days**  

These help spot drift, misalignment, and resourcing gaps.

---

Would you like me to merge this into the full guide draft?  

Also, for reflection:
- How do you want priority to shape behavior in your org?  
- Could you bring in peers from product or design to align on shared understanding of priority, so teams don’t get conflicting signals?  

And would you like a debrief of this interaction before we wrap?

### User - 2025-03-07 07:05:07

Linear also has urgent in addition to high, medium, and low. 

Also, in my organization we have the idea of commitments, which are projects or issues that have a concrete commitment to an external stakeholder. Map that onto the urgent label

### Assistant - 2025-03-07 07:05:08

Perfect! Thanks for the clarification. Here's an updated **Project Priority Conventions** section that incorporates **Urgent** and maps it directly to your concept of **commitments**.

---

## **6. Project Priority Conventions**  

Priority signals how important a Project is relative to others, helping teams align focus, manage trade-offs, and communicate expectations across the organization.

### **Standard Priority Levels:**  

| Priority | Meaning | When to Use |
|----------|---------|-------------|
| **Urgent** | **Critical, time-sensitive commitments made to external stakeholders.** Must be actively worked on until resolved. Delay has clear external consequences. | - Tied to a committed deadline or delivery for a customer, partner, or exec.<br>- Missing the deadline would harm trust, contracts, or critical business outcomes.<br>- Requires clear communication and regular progress updates. |
| **High** | Top internal priority. Delay would significantly impact key business goals or Initiatives. | - Strategically important.<br>- Actively worked on with strong leadership visibility.<br>- May become **Urgent** if tied to an external promise. |
| **Medium** | Important, valuable work with no hard commitment. Can be deferred if necessary. | - Helps advance strategic goals.<br>- May be blocked by higher priorities.<br>- Safe to pause temporarily. |
| **Low** | Opportunistic or exploratory work. Minimal impact if delayed. | - Background tasks, early exploration, or minor improvements.<br>- Often paused when higher-priority work arises. |

---

### **Conventions for Using Priority:**  

1. **Urgent = Commitment**  
   Use **Urgent** only for Projects or Issues tied to explicit, time-bound commitments to external stakeholders (customers, partners, or leadership-level promises). This includes formal delivery dates, contractual obligations, or public launches.

2. **Limit the use of Urgent**  
   Overusing Urgent dilutes its meaning. Every Urgent item must be actively managed and resourced, with leadership attention.

3. **Communicate clearly on Urgent work**  
   - Announce new Urgent priorities in team and leadership channels.  
   - Ensure owners are explicit about timelines, risks, and blockers.  
   - Provide regular progress updates (at least weekly).

4. **Prioritize realistically**  
   - Use **High** for major internal priorities without external commitments.  
   - Use **Medium** and **Low** to reflect the real flexibility of the work.

5. **Review priorities regularly**  
   Priorities should be updated during planning cycles and whenever external commitments change.

6. **Leadership visibility on Urgent work**  
   Maintain a dedicated Linear view or report tracking all active **Urgent** Projects and Issues to monitor commitments and ensure focus.

---

### **Optional Leadership Views to Support Priorities:**  
- **Active Urgent Commitments** (by due date)  
- **High Priority Projects Without Recent Updates**  
- **Low and Medium Priority Projects Stalled for 60+ Days**  
- **Upcoming Commitment Deadlines (Urgent + High)**  

---

### **Reflection prompt for you:**  
- Are teams clear today on what qualifies as a "commitment"?  
- Could you co-create definitions of commitments with product, sales, and customer success to ensure alignment and prevent overcommitment?

Would you like this seamlessly merged into the full style guide draft now?  

And should we debrief before we close this task? I can offer what worked, what could improve, and invite your thoughts too.

### User - 2025-03-07 07:26:06

Integrate this priority guidelines into the style guide.

### Assistant - 2025-03-07 07:26:06

Great! Here’s the **integrated version of the Linear Style Guide** with the **Priority Conventions** fully woven in. I’ve placed it as its own cohesive section, updating the numbering and cross-referencing where helpful.

---

# **Linear Style Guide**

This guide defines best practices for organizing, naming, and maintaining Initiatives, Projects, Issues, and related elements in Linear, ensuring clarity, consistency, and usability across the workspace.

---

## **1. Purpose**  
To create a shared system that:  
- Enables anyone in the company to understand the scope and status of work.  
- Supports cross-team collaboration.  
- Maintains long-term clarity and discoverability over time.  

---

## **2. Hierarchy Overview**

| Level        | Purpose                                      | Ownership                   | Audience                |
|--------------|----------------------------------------------|-----------------------------|-------------------------|
| **Initiative** | Cross-cutting, strategic outcomes or themes | Workspace-level (often leadership) | Whole company         |
| **Project**    | Time-bound effort delivering specific value | One or more teams           | Adjacent teams + company leadership |
| **Issue**      | Discrete, actionable work items            | Single team                 | Project contributors   |
| **Sub-Issue** | Smallest units of work within an issue      | Same as parent issue        | Direct assignees       |

---

## **3. Scope**

### **Initiatives**  
Broad, high-level objectives often spanning multiple quarters.  
Examples:  
- “Improve Onboarding Experience”  
- “Scale Infrastructure for 10x Traffic”  

### **Projects**  
Concrete efforts delivering value, typically over weeks or months.  
Examples:  
- “Self-Serve Team Invites”  
- “Migrate Build System to Bazel”  

---

## **4. Naming Conventions**

### **Initiatives**  
- Start with a verb or goal-oriented phrase.  
- Short but informative.  

Examples:  
> "Reduce Onboarding Time – New User Journey"  

### **Projects**  
- Descriptive names meaningful outside the project team.  
- Avoid internal jargon.  

Examples:  
> “Self-Serve Team Invites”  

### **Issues & Sub-Issues**  
Actionable titles, clearly written tasks.  
Example: “Update API docs for new authentication flow”  

---

## **5. Status Usage and Conventions**

Project status reflects current phase:  

| Status         | Definition | Owner Responsibility |
|----------------|------------|----------------------|
| Idea          | Rough concept, not prioritized. | Review quarterly. |
| Next Up       | Prioritized, starting soon. | Confirm scope and team. |
| Scoping       | Defining requirements. | Draft Milestones. |
| Implementation| Actively in development. | Provide regular updates. |
| Pre-Release   | Final testing and prep. | Validate readiness. |
| EAP           | Controlled external testing. | Gather feedback. |
| Experimental  | Trialing viability. | Define success upfront. |
| Beta          | Broad but provisional release. | Monitor feedback. |
| GA            | Fully launched. | Ensure support. |
| Completed     | Fully wrapped. | Add retrospective link. |

---

## **6. Priority Conventions**  

Priority reflects the importance of a Project or Issue relative to others. It guides resourcing, focus, and communication, especially across teams and leadership.

### **Standard Priority Levels:**  

| Priority | Meaning | When to Use |
|----------|---------|-------------|
| **Urgent** | **Critical, time-sensitive commitment to an external stakeholder.** Must be actively worked until complete. | - Tied to customer, partner, or exec-level commitments.<br>- Missing the deadline risks trust or business outcomes.<br>- Requires clear updates. |
| **High** | Top internal priority. Delay significantly impacts business goals. | - Strategic importance.<br>- Actively resourced.<br>- Leadership visibility. |
| **Medium** | Important work with no hard commitment. Deferrable if needed. | - Valuable but flexible.<br>- Can be paused. |
| **Low** | Opportunistic or exploratory work. Low impact if delayed. | - Background tasks.<br>- Early explorations. |

### **Commitments and Urgent Priority:**  
In our organization, **commitments** are promises made to external stakeholders (customers, partners, or executives). Any work tied to such a commitment **must** be marked as **Urgent** and receive active, focused attention until completion.

### **Priority Best Practices:**  
1. **Set a priority for every active Project.**  
2. **Urgent = Commitment.** Overusing Urgent weakens trust in the system.  
3. **Communicate priority changes.** Notify stakeholders when priorities shift.  
4. **Review priorities regularly.** Adjust during planning cycles and as commitments evolve.  
5. **Leadership visibility.** Maintain a view of all Urgent Projects to monitor commitments.  

---

## **7. Milestones**  
Use to group Issues within Projects. Optional but recommended for larger efforts.  

---

## **8. Ownership and Visibility**  
- **Initiatives:** Workspace or leadership-owned.  
- **Projects:** Must have clear team ownership.  
- **Issues:** Single team ownership only.  

---

## **9. Best Practices**  
- **Archive stale work** regularly.  
- **Cross-link related work** for easy navigation.  
- **Document retrospectives** in Project comments.  
- **Quarterly hygiene reviews** to keep Linear accurate.

---

## **10. Example Setups**

### **Initiative**  
**Name:** Reduce Onboarding Time – New User Journey  
**Projects:**  
- Self-Serve Team Invites  
- Streamlined Signup Flow  

### **Project**  
**Name:** Self-Serve Team Invites  
**Purpose:** Allow users to invite teammates without admin approval.  
**Priority:** High  
**Status:** Implementation  

---

## **11. Maintenance**  
Assign a “Linear Hygiene” owner in each team to:  
- Monitor for drift in statuses and priorities.  
- Ensure timely archiving.  
- Facilitate quarterly reviews.

---

### **Leadership Views to Support Priority and Commitments:**  
- **Active Urgent Commitments** (sorted by due date).  
- **High Priority Projects Without Updates.**  
- **Medium/Low Projects Stalled 60+ Days.**  
- **Upcoming Commitment Deadlines (Urgent + High).**

---

## **Final Thoughts**  
### **Building Human Connection**  
- Co-create commitment definitions across product, sales, and customer success.  
- Pair newer PMs or leads with mentors to set priorities effectively.  
- Celebrate excellent priority management in public channels.  

### **Reflection**  
As you apply this guide, reflect on:  
- How well is priority being used to focus the org?  
- Are commitments realistic and transparent?  
- What feedback loops can improve our shared clarity over time?  

Would you like me to prepare this as a shareable document or template?  

And before we wrap, would you like to debrief our work on this? I can suggest what worked well, areas we might refine, and invite your thoughts.

### User - 2025-03-07 07:27:03

Think critically about project management for software engineering organizations and point out places where the system may have gaps in providing clarity to stakeholders

### Assistant - 2025-03-07 07:27:03

Excellent, this is exactly the kind of reflective, systems-level thinking that builds mastery. Before I dive in, do you feel confident identifying these gaps yourself? If not, I can suggest one specific area for you to analyze as a start. If you *are* confident, I can offer advanced frameworks for surfacing hidden clarity gaps and organizational blind spots. Want that?

For now, here's a critical analysis of potential **gaps in clarity** in the Linear system as described, with a focus on **software engineering org needs**:

---

## **Potential Gaps in Clarity in Linear's Project Management for Engineering Organizations**

### 1. **Initiative to Project Alignment**
**Potential gap:**  
Initiatives exist to group Projects under strategic goals, but without a formal mechanism to enforce strong Initiative-Project linkage (like required metadata, goal statements, or progress rollups), stakeholders may not see how Projects collectively drive outcomes.

**Impact:**  
- Duplicate or misaligned Projects across Initiatives.  
- Difficulty understanding Initiative health beyond individual Project status.  

**Possible fix:**  
- Add clear success metrics and shared milestones at the Initiative level.  
- Regular reviews to assess Initiative progress as a whole, not just individual Projects.  

---

### 2. **Unbounded Project Scope**
**Potential gap:**  
Projects can exist indefinitely in states like "Scoping" or "Idea" without clear criteria for moving forward or being archived.

**Impact:**  
- Cluttered views.  
- Stakeholders unsure if Projects are real, dead, or just perpetually "coming soon."  

**Possible fix:**  
- Apply aging policies (e.g., auto-flag Projects idle for 90 days).  
- Require explicit "next decision date" in Scoping.  

---

### 3. **Urgency Inflation and Priority Drift**
**Potential gap:**  
Over time, more Projects may creep into **Urgent** or **High** priority to attract attention, even when they don't reflect true external commitments or strategic importance.

**Impact:**  
- Leadership attention diluted.  
- Teams feel pressure to mark work as more urgent than it is.  
- Loss of trust in priority signals.  

**Possible fix:**  
- Quarterly priority audits.  
- Cross-functional agreement on commitment definitions and constraints.  
- Capped number of Urgent Projects per team.  

---

### 4. **Status vs. Priority Confusion**
**Potential gap:**  
It's possible for a Project to be **Urgent** but sit in **Scoping** for weeks, or be **Low** priority but in **Implementation**, which creates cognitive dissonance for observers.

**Impact:**  
- Mixed signals about true progress.  
- Stakeholder confusion about resourcing and focus.  

**Possible fix:**  
- Create expected status-priority pairings (e.g., Urgent work should not stay in Scoping longer than X weeks).  
- Build views that highlight mismatches.  

---

### 5. **Cross-Team Dependencies**
**Potential gap:**  
Linear's model emphasizes single ownership per Issue and Project, but cross-team dependencies are often the most fragile, complex parts of engineering work.

**Impact:**  
- Hidden dependencies.  
- Delays when teams are unaware of blocking or downstream work.  

**Possible fix:**  
- Formalize dependency tracking (through labels, linked Issues, or dedicated Projects).  
- Require dependency health checks during planning.  

---

### 6. **Lack of Outcome Tracking**
**Potential gap:**  
The system tracks delivery (status, priority, progress) but not necessarily *impact*. Completed Projects may not feed into post-release success metrics.

**Impact:**  
- Hard to connect work to business results.  
- Diminished learning from prior work.  

**Possible fix:**  
- Add outcome fields to Projects (e.g., "Success Criteria," "Post-Launch Results").  
- Schedule follow-ups 30/60/90 days after GA.  

---

### 7. **Milestone Ambiguity**
**Potential gap:**  
Milestones are at the discretion of Project owners, which means inconsistent use and unclear expectations across Projects.

**Impact:**  
- Hard to compare progress between Projects.  
- Some large Projects may lack clear sub-phases.  

**Possible fix:**  
- Define standard Milestone patterns for common Project types (e.g., Discovery, MVP, GA).  
- Encourage or require Milestones for Projects above a certain size.  

---

### **Reflection for You**  
- Which of these gaps resonate most with your current org experience?  
- Where have you already seen drift, misalignment, or confusion show up?  
- Who else might have valuable insights on these gaps (and how they impact them), and how could you bring them into this conversation to build trust and shared ownership?  

Would you like help designing a diagnostic process or lightweight health check to identify which of these gaps are most active in your org?  

And before we wrap, want to debrief our interaction here? I can share what I think worked well, what could improve, and hear your thoughts too.

### User - 2025-03-07 08:57:13

Work into the style guide. A strong recommendation that projects should have an end State. It does not need to be date based, but there should be a clear definition of done. The only exception is projects that are meant to be buckets for ongoing maintenance work

### Assistant - 2025-03-07 08:57:13

Excellent addition. Here's the integration of your **"end state" recommendation** into the style guide. I’ve placed it where it naturally reinforces clarity around project lifecycle, specifically in the **Projects** section and **Best Practices**, while also cross-referencing status usage.

---

## **3. Scope**

### **Projects**  
Projects represent concrete efforts delivering value, typically over weeks or months.  
Examples:  
- “Self-Serve Team Invites”  
- “Migrate Build System to Bazel”  

**All Projects must have a clear end state.**  
This means every Project should define what "done" looks like, whether through specific deliverables, outcomes, or criteria for closure.  

- **End state ≠ date-based deadline.**  
  The focus is on defining success or completion conditions, not necessarily a fixed date.  
- The only exception:  
  Projects explicitly designed as ongoing **maintenance buckets** (e.g., “Infrastructure Health: 2025”) can remain open-ended but must be clearly labeled as such in their description.  

---

## **5. Status Usage and Conventions**  
Projects should not linger indefinitely in intermediate statuses like **Scoping** or **Implementation**. Every Project should be working toward its defined end state.  

Use **Completed** status when the Project has fully met its definition of done, unless it is a maintenance bucket.  

---

## **9. Best Practices**  

- **Define a clear end state for every Project.**  
  At creation, include a short statement in the Project description clarifying what completion means (e.g., “Done when X feature is GA” or “Complete after migration finishes and monitoring is stable for 30 days”).  

- **Explicitly identify maintenance bucket Projects.**  
  Use clear naming (e.g., prefix with "Maintenance:" or "Ongoing:") and description language to ensure stakeholders understand that ongoing work is expected.  

- **Avoid zombie Projects.**  
  Projects without activity toward their end state within 30–60 days should be reviewed and either re-scoped, re-prioritized, or closed.

---

Would you like me to also draft example Project descriptions that model this end-state clarity?  

And, reflecting on this—are there ways you might involve your team in defining what strong end states look like across different Project types? That could build shared ownership and increase the guide’s impact.

Want to debrief this update as well?

### User - 2025-03-07 08:57:38

Yes, let's draft an example and then work it all into one integrated style guide again

### Assistant - 2025-03-07 08:57:38

Perfect! Here’s an **example project description** that models clear end-state definition, followed by the **fully integrated style guide** with all recent updates woven together.

---

## **Example Project Description (with End State)**  

**Project Name:** Self-Serve Team Invites  

**Purpose:** Allow users to invite teammates without requiring admin approval, improving onboarding speed and reducing friction for growing teams.  

**Priority:** High  

**Status:** Implementation  

**Definition of Done:**  
This Project will be considered complete when:  
- Users can send team invites without admin intervention.  
- Invite flows are successfully used by at least 100 teams.  
- Associated documentation is updated.  
- Support has been trained on the feature.  
- Metrics show a 10% increase in team activations within two weeks of launch.  

**Milestones:**  
- MVP  
- Internal Testing  
- Public Launch  

---

# **Linear Style Guide (Integrated)**  

This guide establishes best practices for organizing, naming, prioritizing, and maintaining Initiatives, Projects, and Issues in Linear to maximize clarity, consistency, and usefulness across the organization.

---

## **1. Purpose**  
To create a shared system that:  
- Helps anyone in the company understand the scope and progress of work.  
- Supports coordination across teams.  
- Keeps long-term work discoverable and clean.  

---

## **2. Hierarchy Overview**

| Level        | Purpose                                      | Ownership                   | Audience                |
|--------------|----------------------------------------------|-----------------------------|-------------------------|
| **Initiative** | Cross-cutting, strategic outcomes or themes | Workspace-level (often leadership) | Whole company         |
| **Project**    | Time-bound effort delivering specific value | One or more teams           | Adjacent teams + leadership |
| **Issue**      | Discrete, actionable work items            | Single team                 | Project contributors   |
| **Sub-Issue** | Smallest units of work within an issue      | Same as parent issue        | Direct assignees       |

---

## **3. Scope**

### **Initiatives**  
Broad, high-level objectives, often spanning multiple quarters.  
Examples:  
- “Improve Onboarding Experience”  
- “Scale Infrastructure for 10x Traffic”  

### **Projects**  
Concrete efforts delivering value, typically over weeks or months.  
Examples:  
- “Self-Serve Team Invites”  
- “Migrate Build System to Bazel”  

**All Projects must have a clear end state.**  
- Define what "done" means (e.g., specific outcomes, deliverables, or conditions).  
- The end state does not need to be date-based but must be outcome-based.  
- The **only exception** is Projects serving as ongoing **maintenance buckets** (e.g., “Ongoing Bug Fixes 2025”), which should be explicitly labeled as such.  

---

## **4. Naming Conventions**

### **Initiatives**  
- Use goal-oriented phrases.  
- Short but informative.  

Examples:  
> "Reduce Onboarding Time – New User Journey"  

### **Projects**  
- Descriptive, non-jargon names meaningful outside the team.  

Examples:  
> “Self-Serve Team Invites”  

### **Issues & Sub-Issues**  
Actionable, clear task titles.  
Example: “Update API docs for new authentication flow”  

---

## **5. Status Usage and Conventions**

Statuses reflect a Project's lifecycle.  

| Status         | Definition | Owner Responsibility |
|----------------|------------|----------------------|
| Idea          | Early concept, not prioritized. | Review quarterly. |
| Next Up       | Prioritized, starting soon. | Confirm scope. |
| Scoping       | Defining requirements. | Draft Milestones. |
| Implementation| Actively being worked on. | Regular updates. |
| Pre-Release   | Final testing and prep. | Validate readiness. |
| EAP           | Limited external testing. | Gather feedback. |
| Experimental  | Trialing viability. | Define success upfront. |
| Beta          | Broad, provisional release. | Monitor feedback. |
| GA            | Fully launched. | Ensure support. |
| Completed     | Fully wrapped. | Link retrospective. |

**Important:**  
Projects should not linger indefinitely. Without progress toward their end state, Projects should be reviewed within 30–60 days.

---

## **6. Priority Conventions**  

Priority reflects importance and resourcing.  

| Priority | Meaning | When to Use |
|----------|---------|-------------|
| **Urgent** | **Critical, time-sensitive external commitment.** Must be actively worked until complete. | Tied to customer, partner, or exec-level promises. |
| **High** | Top internal priority. Delays significantly impact business goals. | Strategically important. |
| **Medium** | Valuable but deferrable. | Safe to pause if needed. |
| **Low** | Opportunistic or exploratory. | Minimal impact if delayed. |

**Urgent = Commitment.**  
Mark any work tied to formal external commitments as **Urgent** and give it active, focused attention.  

**Best Practices:**  
- Set priority on every active Project.  
- Limit Urgent usage to maintain trust.  
- Communicate priority shifts.  
- Review priorities during planning cycles.  

---

## **7. Milestones**  
Use Milestones to group Issues within Projects, particularly for large efforts. Recommend clear phase-based Milestones (e.g., MVP, Launch, Post-Launch Support).

---

## **8. Ownership and Visibility**  
- **Initiatives:** Workspace or leadership-owned.  
- **Projects:** Must have explicit team ownership.  
- **Issues:** Single team ownership only.  

---

## **9. Best Practices**  

- **Define end states.** Every Project must state what completion means in its description.  
- **Explicit maintenance buckets.** Clearly name and describe Projects meant to stay open for ongoing work.  
- **Avoid zombie Projects.** Regularly review and close stale Projects.  
- **Archive completed work.** Keep Linear clean and up to date.  
- **Cross-link related work** for context.  
- **Document retrospectives** in completed Projects.  

---

## **10. Example Setups**

### **Initiative**  
**Name:** Reduce Onboarding Time – New User Journey  
**Projects:**  
- Self-Serve Team Invites  
- Streamlined Signup Flow  

### **Project**  
**Name:** Self-Serve Team Invites  
**Purpose:** Allow users to invite teammates without admin approval.  
**Priority:** High  
**Status:** Implementation  
**Definition of Done:** See example above.  

---

## **11. Maintenance**  
Assign a “Linear Hygiene” owner per team to:  
- Monitor for stale Projects and statuses.  
- Ensure clear end states.  
- Lead quarterly cleanups.

---

## **12. Leadership Views to Support Priority and Commitments:**  
- **Active Urgent Commitments** (by due date).  
- **High Priority Projects Without Updates.**  
- **Medium/Low Projects Stalled 60+ Days.**  
- **Upcoming Commitment Deadlines (Urgent + High).**

---

## **Final Thoughts**  
### **Building Human Connection**  
- Align with product, sales, and customer success on commitment definitions.  
- Mentor new Project owners on setting clear end states.  
- Recognize teams that model exceptional project hygiene.

### **Reflection**  
As you apply this guide:  
- Where are end states unclear in your current Projects?  
- How might clearer definitions shift team focus and stakeholder trust?  
- Who could you involve to keep this guide relevant and evolving?

Would you like this prepared as a document or template for sharing?  

And before we wrap—would you like to debrief this work? I can share what I think worked well, what we could refine, and hear your thoughts.

