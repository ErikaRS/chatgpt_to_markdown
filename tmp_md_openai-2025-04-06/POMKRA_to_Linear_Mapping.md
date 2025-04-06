# POMKRA to Linear Mapping

Created: 2025-03-22 07:09:09
Last Updated: 2025-03-22 07:12:17

### User - 2025-03-22 07:09:09

Let's map the ideas in this onto our linear project management with milestones mapping to initiatives, key results to projects (maybe?) and activities to issues https://medium.com/@yonatanzunger/the-pomkra-method-bf0f4bb4eb54

### Assistant - 2025-03-22 07:09:21



### Assistant - 2025-03-22 07:09:09

Great! Yonatan Zunger’s **POMKRA method** outlines a structured framework for defining goals and execution plans. Let’s break down the method and then map it onto your **Linear project structure**, where you use:

- **Initiatives** → mapped to big milestones  
- **Projects** → mapped to key deliverables or programs  
- **Issues** → mapped to tasks or activities  

---

### **POMKRA Overview**

POMKRA stands for:

- **Purpose** – Why are we doing this? What's the end goal or the vision?
- **Objectives** – What must we achieve for the purpose to be fulfilled?
- **Measures** – How will we know we’re achieving the objective?
- **Key Results** – What are the measurable intermediate results toward the objectives?
- **Actions** – What will we *do* to achieve those key results?

Zunger treats **Objectives** as larger than Key Results (OKRs do the reverse), and emphasizes **execution traceability**: you should be able to trace any Action back to the Purpose.

---

### **Mapping POMKRA → Linear Structure**

| **POMKRA Element** | **Linear Structure** | **Notes** |
|--------------------|----------------------|-----------|
| **Purpose**         | Company-level mission or top-level strategic doc | This is usually broader than what's in Linear, but it informs all Initiatives. |
| **Objectives**      | **Initiatives**       | These are the high-level goals you're pursuing. |
| **Measures**        | Initiative-level metrics or status definitions | You could track these via custom fields or linked dashboards. |
| **Key Results**     | **Projects**          | These are major deliverables or changes that reflect progress toward Objectives. |
| **Actions**         | **Issues / Sub-issues** | Day-to-day work and tasks to complete projects. |
| **Activities**      | **Issues** (mapped to Actions) | Same as Actions in this case. |

If you think in terms of **outcomes vs outputs**, the mapping flows like this:

- **Purpose** = strategic intent (why)
- **Objectives** = intended outcomes (what we want to see change)
- **Key Results** = intermediate, observable outcomes that show we're on the right track
- **Actions/Activities** = outputs/tasks (how we get there)

---

### **Example Mapping**

**Purpose:** Improve developer velocity and autonomy  
→ *Not represented directly in Linear but underpins initiative-level work*

**Objective (Initiative):** Streamline the PR review and merge process

- **Measure:** PR cycle time < 24h for 90% of PRs

**Key Result (Project):**  
- Automate reviewer assignment and queueing  
- Roll out a PR review SLA policy with team dashboards  
- Simplify pre-merge checks with unified CI feedback  

**Actions (Issues):**  
- Build GitHub bot for reviewer rotation  
- Write documentation for SLA process  
- Implement CI status aggregation widget  

---

### Optional Enhancements

You could also:

- **Tag Issues by Key Result** to track what work contributes where
- Use **Descriptions** in Projects to restate the **Key Result** they represent
- Include **Objective links in Initiative descriptions** to anchor back to the Purpose
- Use a **POMKRA template** when writing up new initiatives/projects

---

Would you like a sample Linear template or naming pattern that encodes this hierarchy?

### User - 2025-03-22 07:09:55

No, the m is milestones, not measures. 

### Assistant - 2025-03-22 07:09:55

Ah, got it—thank you! You're right: in **Zunger's POMKRA**, the **M stands for *Milestones***, not Measures. That makes a big difference. Let’s adjust accordingly and re-map it to your **Linear structure**, where:

- **Initiatives = Milestones**
- **Projects = Key Results (maybe)**
- **Issues = Activities**

---

### **Refresher: POMKRA Breakdown**

- **P**urpose – The overarching goal or "why"  
- **O**bjectives – The specific goals that support the purpose  
- **M**ilestones – Major waypoints or transitions that indicate you're making progress  
- **K**ey Results – The measurable outcomes that confirm progress toward an objective  
- **R**esponsibilities – Who owns what  
- **A**ctivities – Concrete tasks or things being done

---

### **Mapping POMKRA → Linear**

| **POMKRA Element** | **Linear Structure** | **Notes** |
|--------------------|----------------------|-----------|
| **Purpose**         | Outside Linear (Strategic brief, memo) | Used to frame Initiatives/Milestones |
| **Objectives**      | Outside Linear (can show up in project docs or top-level docs) | Not directly encoded in Linear structure |
| **Milestones**      | **Initiatives**       | Major goals with meaningful transitions—“things that should be true” after this point |
| **Key Results**     | **Projects**          | Tangible sub-goals that show progress toward milestones |
| **Responsibilities**| Assignees / Custom fields in Linear | Who owns each project or issue |
| **Activities**      | **Issues** (and sub-issues) | Specific actions being taken to achieve Key Results |

---

### **Example Mapping in Linear Terms**

**Purpose:** Reduce friction in internal developer workflows  
→ *Framed in external doc or strategy memo*

**Objective:** Improve PR feedback cycles and reduce merge delays  
→ *Also outside Linear, could be noted in Initiative description*

**Milestone (Initiative):**  
- “PR feedback loop is fast, clear, and fair”

**Key Results (Projects):**  
- SLA for reviews implemented  
- Pre-merge check flakiness reduced  
- Automated reviewer assignment working  
- Clear CI feedback in PR UI  

**Responsibilities:**  
- Each project assigned to an owner  
- Custom fields can show additional RACI-type ownership

**Activities (Issues):**  
- Write and socialize SLA  
- Implement bot to rotate reviewers  
- Remove flaky test suite  
- Redesign CI feedback widget

---

### A Note on Milestones vs Key Results

Zunger’s **Milestones** are *state changes*—"things that are true now."  
Key Results are the *evidence* you're achieving what you meant to.  

So if you’re using **Linear Initiatives = Milestones**, then your **Projects as Key Results** can work, *as long as each Project has clear success criteria* that aligns with “here’s how we know the milestone is real.”

---

### Optional Enhancements

- Include **Objectives** in Initiative descriptions  
- Use **Project names** to reflect their Key Result intent (e.g. “Review SLA is defined and adopted”)  
- Add a **POMKRA section** to docs or Linear custom views for alignment  
- Build dashboards where Initiatives are tagged with their Purpose and Objective  

---

Want help drafting a template you could use when entering new Initiatives/Projects in Linear using POMKRA framing?

### User - 2025-03-22 07:11:48

The key thing about milestones is that they are independent units of value delivered. 

### Assistant - 2025-03-22 07:11:49

Yes—that’s the crucial insight. In **POMKRA**, **Milestones are *independent units of value***: they aren't just progress markers; they're **coherent, deliverable outcomes** that **stand alone as valuable**, even if the larger goal isn’t yet complete.

This makes them ideal to map to **Linear Initiatives** *if* you’re treating those Initiatives as *units of value delivery*, not just thematic buckets. Let’s refine the mapping with that lens:

---

### **Refined POMKRA → Linear Mapping**

| **POMKRA**          | **Linear**             | **Notes** |
|---------------------|------------------------|-----------|
| **Purpose**         | External to Linear     | Captured in strategy docs, PRDs, or planning memos |
| **Objective**       | External or Initiative Grouping | Strategic goals that span multiple milestones/initiatives |
| **Milestone**       | **Initiative**         | A standalone, valuable outcome. “This is done and useful.” |
| **Key Result**      | **Project**            | A necessary part of the milestone being real, but not independently valuable on its own |
| **Responsibility**  | **Assignee / Custom fields** | Who owns what across projects and issues |
| **Activity**        | **Issue / Sub-issue**  | What people are actively doing |

---

### **Key Implications of Milestones as Value Units**

- Each **Initiative** (milestone) in Linear should deliver *something concrete and shippable*, not just a phase of work.
- A milestone being “complete” means a user or stakeholder *can now do something they couldn’t before*, or something important is now true.
- This helps teams understand what *really matters* and builds alignment across workstreams.
- Projects (Key Results) can succeed or fail independently, but **only when all succeed does the milestone deliver its intended value**.

---

### **Example: Internal Tooling Improvement**

**Purpose:** Improve developer productivity

**Objective:** Cut down PR merge time

**Milestone (Initiative):**  
**“Review process is responsive and transparent.”**  
- Value unit: reviewers know what to do, developers get quick feedback, stakeholders trust the process.

**Key Results (Projects):**
- PR review SLA defined and enforced  
- CI feedback redesigned for clarity  
- Reviewer load balancing bot deployed  
- Weekly PR metrics dashboard published

**Activities (Issues):**
- Draft and socialize SLA  
- Build reviewer rotation logic  
- Redesign status-check card in UI  
- Write queries and set up dashboards

Each of these projects contributes to the milestone, but **none alone delivers the full unit of value**—only when combined do they satisfy the milestone’s outcome.

---

Would you like help converting a current Linear Initiative into this framing, or creating a checklist/template for defining Milestones this way?

