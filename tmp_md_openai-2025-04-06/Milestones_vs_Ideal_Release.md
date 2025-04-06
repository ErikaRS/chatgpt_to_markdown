# Milestones vs Ideal Release

Created: 2024-11-12 04:46:46
Last Updated: 2024-11-12 05:41:22

### User

*[user_editable_context content]*

### User - 2024-11-12 04:46:46

Compare and contrast the milestones defined in this list with the list defined in "IDEAL FINAL RELEASE"

## **BASIC FUNCTIONALITY - Nov 25th, 2024**

*Minimum viable dogfooding product* 

**Goal:** restart the project, get stronger internal feedback

**Scope:**

- Improved intent detection - @Jan Hartman
- New search
    - Keyword search approximates behavior (NLS v.0) - @Camden Cheek
    - @scope Language + Code Mirror - @Naman Kumar @Felix Kling
    - Results page - @Naman Kumar @Felix Kling
        - Open results locally in IDE

Stretch goal:

- First external feedback from Enterprise customers

## **Dec 18th, 2025**

## MVP FOR CUSTOMERS

- Personalization (manual)
- NLS  v1
    - Quality framework?
- Intent v2
- Filters

## **Jan 15th, 2025**

# FINAL RELEASE

**Goal:** Complete enough to get meaningful feedback from customers

**Scope:**

- New app homepage and information architecture
- Smooth interaction between IDE and web
- Ability to follow up on Search results with a question (@searchResults functionality)

## **Jan 29(Feb 5?) 2025**

**Goal:** strong product release

**Scope:**

- Finely tuned intent detection
- Evaluated and effective NLS
- Suggested prompts and/or impactful prompt integration into followups
- Integration with MTSG private code for Sourcegraph Teams

- QA’d and stable product

# IDEAL FINAL RELEASE

- New, simple search designed to solve the majority of search use cases only
    - **M1** @scope syntax
    - **M1** Natural language search (keyword-driven)
    - **M2** Manual personalization to the user’s repos, not all the code
- **M1** Codemirror
- **M1** Intent detection
    - Specifics about targeted categories (previously, we had search-entity, search-functionality, chat)
    - Get a better model online
        - Data!
        - Fine-tune model with new architecture
    - 
- Chat functionality
    - Editable context
- A new app homepage and information architecture
    - @Felix Kling wants a “recent repositories”
        - @Taiyab Raja Could relate to “my projects” requirement
    - prompts library
    - advanced search
    - recent repos
- Interaction
    - Between IDE and Web:
        - Paths to advanced (current) search
        - Code navigation
        - Editing code
    - Web to IDE
        - Configuration
    - Threads - start with a problem, curate context, refine, follow up question
        - This is only starting to be defined
    - Shared chat history
- Prompt Suggestions
- ⭐️ Automatic personal ranking
- Cody context (pool of context Cody (and maybe search) is drawing from
    - Based on: baseline fetching from “Deep Cody” + “my projects” + what’s being targeted in the input
    - Prioritisation of all these context inputs
    - Context suggestions
    - Parallels between context and search
- Extensibility through prompts (an under-defined component)
- Telemetry
- Feedback Collection
- Intent templates
    - Both the LLM and the search results
- ⭐️ Embeddings for natural language search

### Assistant - 2024-11-12 04:47:05



### Assistant - 2024-11-12 04:47:05

It looks like both the milestone list and the "IDEAL FINAL RELEASE" describe similar overarching goals but at varying levels of detail and ambition, focusing on a gradual evolution towards a fully-featured product. Here’s a breakdown of the differences and similarities in the two plans:

### **1. Goals and Progression**
- **Milestone List:**
  - The milestone list defines specific phases and target dates, starting from **Basic Functionality** (Nov 25, 2024) to **Strong Product Release** (Jan 29-Feb 5, 2025).
  - The progression is gradual, focusing initially on achieving **Minimum Viable Dogfooding** and moving towards broader, customer-facing releases. Each milestone incrementally adds features, with an emphasis on gradually gathering **feedback** from both internal and external customers.
  - Goals are focused more narrowly on making sure the product evolves iteratively, testing it incrementally, and expanding from MVP to a more polished **final product**.

- **IDEAL FINAL RELEASE:**
  - This describes the ultimate vision of what a “complete” product looks like. Rather than setting time-bound milestones, it focuses on the **ideal end state**, which means a fully developed, highly polished product.
  - Features include some advanced requirements, like **extensibility through prompts**, **automatic personal ranking**, and **shared chat history**, which are not highlighted in the earlier milestones. The **IDEAL FINAL RELEASE** aims to be a definitive version that encompasses **all desired functionalities**, focusing on solving the majority of user use cases.

### **2. Scope and Features**
- **Incremental Milestones:**
  - The milestones are built around practical, achievable targets.
  - Features like **improved intent detection**, **manual personalization**, and the **NLS v1** framework are added gradually.
  - New search methods are rolled out incrementally, starting from **keyword-driven search** to a more complete **Natural Language Search (NLS) v1**.
  - There is a clear focus on getting internal feedback first and then moving to **external customer feedback**, with **QA** as the final step before a strong product release.
  
- **IDEAL FINAL RELEASE Features:**
  - Provides a more comprehensive overview, including details like **context management**, **automatic personal ranking**, and **extensibility** that require more sophisticated development and integrations.
  - Features like **prompt suggestions**, **chat functionality**, **shared chat history**, and **embeddings for natural language search** are mentioned, which shows a more **user-centric design**, intending to optimize user interactions over time.
  - **Telemetry**, **feedback collection**, and the concept of **Cody context** are important elements that help continuously adapt the product to the user, making it highly customizable and responsive.

### **3. Focus on Personalization and User Experience**
- **Milestones:**
  - Initially, there is **manual personalization**, and only towards the end do features like **suggested prompts** start becoming evident.
  - The features are incremental, each release acting as a foundational layer to support future upgrades, leading up to **strong integration** of different product aspects by the final product release milestone.
  
- **IDEAL FINAL RELEASE:**
  - There is a heavy emphasis on **personalization**—manual personalization of repos evolves into **automatic personal ranking** and managing **context suggestions**.
  - The "ideal" version appears to be more proactive in providing a curated and personalized experience, compared to the reactive iterations in the milestone list.
  - Embeddings are specifically called out for natural language search, suggesting the aim for more **context-aware, intelligent** search that feels intuitive for the user.

### **4. Integration and Interaction**
- **Milestones:**
  - The **milestones** gradually integrate **interaction between the IDE and the web** but keep it relatively basic, ensuring smooth operation between web and local environments.
  - The integration focuses more on **basic synchronization**—following up on search results, new homepage architecture, etc.

- **IDEAL FINAL RELEASE:**
  - Integration and interaction are envisioned at a much more advanced level:
    - **Advanced paths** between IDE and web that handle code navigation and more complex **shared configurations**.
    - Features like **chat threads** that evolve from a problem to a curated conversation show a deeper focus on **building continuity** across the user journey.
    - Integration of shared chat histories further aims to create an environment where the **context is retained**, making user transitions between platforms seamless.

### **5. Feedback and Telemetry**
- **Milestones:**
  - There are implicit mentions of **feedback loops**—primarily the stretch goal for external customer feedback after basic functionality and a target to gather meaningful feedback after the final release.
  
- **IDEAL FINAL RELEASE:**
  - There is a much deeper focus on **Telemetry** and **Feedback Collection** mechanisms, which are critical to optimizing the product based on detailed, contextual data from users. This shows a focus on **long-term adaptability and improvement**.

### **6. Completeness**
- **Milestones:**
  - Each milestone is a **building block** toward a robust release, ensuring each stage is usable in some context (e.g., internal teams, early external customers).
  - The milestones represent an iterative rollout strategy, ensuring that valuable feedback is collected and integrated at each stage.

- **IDEAL FINAL RELEASE:**
  - It represents a more **holistic vision** of what the final product should do, including details that are often not achievable until a product is mature.
  - The end product aims for **total integration**—between the IDE and web, chat contexts, personalized search, etc. The completeness here means creating an advanced system that behaves intelligently in every context, with minimal manual intervention from users.

### **Summary**
- The **milestone-based list** is primarily a roadmap to reach specific targets and gather progressively more feedback, focusing on basic and practical integration of features.
- The **IDEAL FINAL RELEASE** is an aspirational blueprint that aims to define a complete, highly functional, and fully integrated product that addresses both existing requirements and expected future user needs.
- The milestones take a pragmatic, step-by-step approach, whereas the **IDEAL FINAL RELEASE** is more of a **visionary design**, emphasizing personalization, seamless interaction, advanced user experience, and adaptability to context.

Would you like to focus on building a plan that incorporates some of the aspirational goals from the **IDEAL FINAL RELEASE** into the immediate milestones, or do you think breaking down the ideal end state into further milestones would be beneficial? It might also be worth reflecting on this planning process later to learn from the complexities in defining and organizing both idealized and practical product states.

### User - 2024-11-12 04:47:35

What is in IDEAL FINAL RELEASE that's missing from the milestones? 

### Assistant - 2024-11-12 04:47:51

The **IDEAL FINAL RELEASE** includes several features, ideas, and elements that are notably absent from the milestones. Below, I outline the unique additions found in the **IDEAL FINAL RELEASE** that are not explicitly covered in the milestone list:

### **1. Advanced Search Capabilities**
- **Embeddings for Natural Language Search (NLS):** 
  - The milestones include **keyword-based NLS v0** and **NLS v1**, which suggests early iterations of natural language search capabilities. However, **IDEAL FINAL RELEASE** specifies **embeddings** for NLS, which implies a more sophisticated approach that leverages semantic understanding to enhance search accuracy.
- **Advanced Search Paths:**
  - The final release aims to offer **paths to advanced (current) search**. This feature appears to be aimed at giving users more depth and flexibility when navigating searches, whereas the milestone list only reaches a simpler keyword-based approach.

### **2. Deep Personalization and Contextual Awareness**
- **Automatic Personal Ranking:**
  - Personalization in the milestone list is **manual**; in contrast, **IDEAL FINAL RELEASE** aims for **automatic personal ranking**, which is a more dynamic and user-centric approach to customize and prioritize search results and contexts.
- **Cody Context and Prioritization:**
  - **IDEAL FINAL RELEASE** has an ambitious vision for managing user context, referring to **Cody context**—a pool of contextual information from sources such as **Deep Cody**, **“my projects,”** and **input targets**. There is also a mention of **context prioritization** and **context suggestions** to help improve user experience. The milestones don’t address these advanced mechanisms, which suggest a level of personalization that adapts in real-time to the user's changing focus and needs.

### **3. Interaction Enhancements**
- **Deep IDE and Web Interaction:**
  - While the milestones cover basic integration between the **IDE and the web**, **IDEAL FINAL RELEASE** expands on this interaction:
    - **Code navigation** and **editing code directly** from one platform to another.
    - **Configuration synchronization** between the IDE and web, making it a seamless experience for developers.
  - There’s also the mention of **shared chat history**, which provides continuity in user experience across platforms, ensuring users can transition between IDE and web contexts without losing any part of the discussion.

### **4. Chat Functionality and Threads**
- **Editable Context in Chat:**
  - The **IDEAL FINAL RELEASE** mentions **editable context** within chat functionality, which gives users the ability to customize and refine the conversational context.
- **Threads for Follow-Up Conversations:**
  - It also introduces **threads**, which begin with a problem, curate context, and refine solutions through **follow-up questions**. This more sophisticated conversational flow isn’t covered in the milestones, which only briefly mention follow-up capabilities from search results.
  
### **5. Prompt Suggestions and Extensibility**
- **Prompt Library and Prompt Suggestions:**
  - The **IDEAL FINAL RELEASE** aims to have a **prompt library** and an enhanced mechanism for **prompt suggestions** or impactful prompt integrations into follow-ups, a concept that’s only partially reflected in the final milestone where “suggested prompts” are mentioned without deeper elaboration.
- **Extensibility Through Prompts:**
  - **Extensibility** via prompts is an under-defined feature in **IDEAL FINAL RELEASE**, which implies giving users more power to extend and customize interactions via prompt-based automation. This is entirely absent in the milestones.

### **6. Intent Templates**
- **Intent Templates for LLM and Search Results:**
  - The **IDEAL FINAL RELEASE** also talks about **intent templates**, which can be used by both the LLM and the search results to guide users or automate certain workflows. This suggests a more structured approach to managing user intent, compared to the more generic mention of **intent detection** in the milestones.

### **7. Telemetry and Feedback Collection**
- **Telemetry** and **Feedback Collection**:
  - Unlike the milestone list, which mainly mentions **feedback loops** from users (internal and external), **IDEAL FINAL RELEASE** calls out **telemetry** and **feedback collection** as dedicated features. This indicates a more systematic approach to continuously improve the product, leveraging user data to drive changes and enhancements.

### **8. Shared Context and Ranking**
- **Shared Chat History** and **Context Suggestions**:
  - The idea of **shared chat history** is unique to the **IDEAL FINAL RELEASE**, and there is a strong focus on leveraging shared context for a seamless experience.
  - **Context suggestions** are another unique feature intended to proactively assist users in navigating complex searches and optimizing the use of Cody’s capabilities.

### **Summary: Missing Features from Milestones**
1. **Advanced Search**: Embeddings for NLS, advanced search paths.
2. **Deep Personalization**: Automatic personal ranking, Cody context, context prioritization, and context suggestions.
3. **IDE and Web Integration**: Advanced code editing and configuration sync, shared chat history.
4. **Chat Enhancements**: Editable context, threads, curated follow-up conversations.
5. **Prompt Library and Extensibility**: Prompt library, impactful suggestions, extensibility through prompts.
6. **Intent Templates**: Structured templates for user intent guidance.
7. **Systematic Feedback Mechanisms**: Telemetry and proactive feedback collection.
8. **Shared Contextual Awareness**: Enhanced chat and context management features for a more cohesive experience.

### **Summary Analysis**
The **IDEAL FINAL RELEASE** envisions a more **polished, integrated, and intelligent product**, heavily focused on **personalization**, **seamless interactions**, and a sophisticated understanding of user context. It extends beyond the milestones by envisioning features that are user-centric, context-aware, and personalized, while also incorporating **systematic adaptability** and a **deep integration** between platforms.

The milestones provide a **realistic roadmap** of incremental development, while the **IDEAL FINAL RELEASE** outlines a **visionary, feature-rich** state that emphasizes not just meeting basic user needs but exceeding them by creating an adaptable, intuitive experience.

Do you think it would be beneficial to prioritize any of these **ideal features** in the near-term milestones, perhaps breaking them down into achievable components? This could help ensure that you move incrementally towards this visionary state while still gaining valuable user feedback along the way. Reflecting on the broader vision later might also help solidify insights on balancing aspirational and incremental goals effectively.

### User - 2024-11-12 05:14:50

I am going to give an updated milestone list. What is in IDEAL FINAL RELEASE that's missing from the milestones? 

## **BASIC FUNCTIONALITY - Nov 25th, 2024**

### Minimum viable dogfooding product

**Goal:** restart the project, get stronger internal feedback

**Scope:**

- Improved intent detection - @Jan Hartman
- New search
    - Keyword search approximates behavior (NLS v.0) - @Camden Cheek
    - @scope Language + Code Mirror - @Naman Kumar @Felix Kling
    - Results page - @Naman Kumar @Felix Kling
        - Open results locally in IDE

Stretch goal:

- First external feedback from Enterprise customers

## **Dec 18th, 2025**

### MVP FOR CUSTOMERS

- Personalization (manual)
- NLS  v1
    - Quality framework?
    - This will be a “however far we get in the time”
- Intent v2
- Filters
- Interactions
    - Moving back and forth between web and IDE
    - Path to advanced search
    - Deeper links into things like blame, history, etc
    - Some will be must have and the rest will be “however far we get”

## **Jan 15th, 2025**

### FINAL TECHNICAL RELEASE

**Goal:** Complete enough to get meaningful feedback from customers

**Scope:**

- Automatic personalization
- New app homepage and information architecture
- Ability to follow up on Search results with a question (@searchResults functionality)
- Finely tuned intent detection
- Evaluated and effective NLS
- Suggested prompts and/or impactful prompt integration into followups
- Integration with MTSG private code for Sourcegraph Teams
- QA’d and stable product

# IDEAL FINAL RELEASE

- New, simple search designed to solve the majority of search use cases only
    - **M1** @scope syntax
    - **M1** Natural language search v0 (keyword-driven)
    - **M2** Manual personalization to the user’s repos, not all the code
- **M1** Codemirror
- **M1** Intent detection
    - Specifics about targeted categories (previously, we had search-entity, search-functionality, chat)
    - Get a better model online
        - Data!
        - Fine-tune model with new architecture
- **M2** Intent v2
    - behind gateway?
- Chat functionality
    - Editable context
- **GA** A new app homepage and information architecture
    - @Felix Kling wants a “recent repositories”
        - @Taiyab Raja Could relate to “my projects” requirement
    - prompts library
    - advanced search
    - recent repos
- **M2** Natural language search v1
    - Undefined improvements
- **M2** Interaction
    - Between IDE and Web:
        - Paths to advanced (current) search
        - Code navigation
        - Editing code
    - Web to IDE
        - Configuration
    - Threads - start with a problem, curate context, refine, follow up question
        - This is only starting to be defined
- Prompt Suggestions
- ⭐️ Automatic personal ranking
- Cody context (pool of context Cody (and maybe search) is drawing from
    - Based on: baseline fetching from “Deep Cody” + “my projects” + what’s being targeted in the input
    - Prioritisation of all these context inputs
    - Context suggestions
    - Parallels between context and search
- Extensibility through prompts (an under-defined component)
- Telemetry
- Feedback Collection
- Intent templates
    - Both the LLM and the search results
- ⭐️ Embeddings for natural language search

### Assistant - 2024-11-12 05:15:08

Upon comparing your **updated milestone list** with the **IDEAL FINAL RELEASE**, the following features, capabilities, and elements are still uniquely present in the **IDEAL FINAL RELEASE** and are **missing** from your milestone list:

### **1. Advanced Personalization & Contextual Awareness**
- **Cody Context**:
  - **Cody context** involves a **pool of context sources** that include "Deep Cody," "my projects," and targeted inputs. It also introduces the idea of **prioritization of context inputs** to deliver personalized and relevant results.
  - This concept is more sophisticated than just automatic personalization; it aims to manage and prioritize multiple sources of context simultaneously. The updated milestones focus only on **basic personalization**, missing the advanced prioritization and adaptability that Cody context offers.
- **Context Suggestions**:
  - Cody also includes **context suggestions** to enhance the user experience dynamically. These suggestions help tailor responses to specific needs based on a user's focus, which is not covered in the updated milestones.

### **2. Chat and Interaction Functionality**
- **Editable Context in Chat**:
  - The **IDEAL FINAL RELEASE** specifically calls out **editable context** within chat functionality. This means users can modify the conversation context to better fit evolving needs, improving precision during interactions.
- **Chat Threads with Refinement**:
  - The ideal release envisions **chat threads** that start with a problem and then allow users to **curate context, refine queries, and ask follow-up questions**. This sophisticated interaction model that supports multi-turn conversations and continuity is not included in the milestone list, which only mentions basic follow-up capabilities.

### **3. Deep Integration and Seamless User Journey**
- **Deeper IDE and Web Interaction**:
  - The **IDEAL FINAL RELEASE** outlines a much deeper integration between **IDE and web**, including:
    - **Editing code directly** between IDE and web.
    - Advanced **code navigation** and seamless **configuration** from web to IDE.
    - This deeper level of integration ensures users can move effortlessly between different environments, preserving the context, which is not captured in the updated milestones beyond basic links and movement between web and IDE.
  
### **4. Advanced Search and Optimization**
- **Embeddings for Natural Language Search**:
  - The **IDEAL FINAL RELEASE** includes **embeddings** for natural language search (NLS), which allow for more nuanced and semantically aware searches. This would result in better understanding and retrieval of relevant content, making searches more intelligent. The milestones include **NLS v1**, but they do not explicitly mention leveraging **embeddings** to enhance its effectiveness.
- **Prompt Library**:
  - A **prompt library** for advanced search and task execution is mentioned in the ideal release but does not appear in the updated milestones. This library would offer predefined prompts for a variety of use cases, helping users to quickly initiate effective actions.

### **5. Telemetry and Feedback Collection**
- **Telemetry**:
  - The **IDEAL FINAL RELEASE** mentions the need for **telemetry** to gather usage data, helping improve product performance and user experience. Telemetry enables fine-grained insights into how users interact with the product, providing actionable data for improvement.
- **Feedback Collection Mechanisms**:
  - Systematic **feedback collection** is also a unique feature in the ideal release. It aims to continuously gather and analyze user input to refine the product iteratively. In contrast, the updated milestones do not explicitly mention a robust feedback collection framework.

### **6. Intent and Extensibility**
- **Intent Templates**:
  - **Intent templates** for both **LLM** and **search results** are mentioned in the **IDEAL FINAL RELEASE**. These templates help the LLM and search tools understand user intent more precisely, guiding the responses and enhancing the search results. This systematic approach to managing intents is absent from the milestones, which only speak to basic versions of intent detection.
- **Extensibility Through Prompts**:
  - **Extensibility through prompts** is an under-defined but critical component mentioned in the ideal release. This suggests users would be able to extend the system’s capabilities via new or customized prompts, providing more power and flexibility in how the system can be used.

### **7. Automatic Personal Ranking**
- **Automatic Personal Ranking**:
  - The ideal release highlights **automatic personal ranking** for personalized search results or recommendations. It provides a mechanism for ranking search results based on relevance to a user's history and context, which is missing from the updated milestones. The milestones only discuss manual and then basic automatic personalization, missing the deeper ranking mechanism that could further tailor the experience.

### **8. Shared Context & Cross-Platform Continuity**
- **Shared Chat History**:
  - The **IDEAL FINAL RELEASE** envisions having a **shared chat history** that would allow users to retain context across different sessions and platforms, ensuring a seamless transition from IDE to web and vice versa. This shared history is crucial for preserving the continuity of discussions and actions but is not present in the milestones.

### **9. Advanced Capabilities of Search and Interaction**
- **Advanced Search Paths & Code Navigation**:
  - The ideal final release includes advanced paths between **IDE and web** and detailed **code navigation** mechanisms that would support users diving deeper into specific areas like **blame** or **history**. The milestones mention the ability to link to such features, but they do not detail a full-fledged capability for advanced paths and code navigation.

### **Summary of Features in IDEAL FINAL RELEASE Missing from Updated Milestones:**
1. **Cody Context & Context Suggestions**: Advanced context handling with prioritized suggestions.
2. **Chat Threads & Editable Context**: Multi-turn conversation flow with the ability to edit context within chat sessions.
3. **Deep Integration**: Advanced IDE-Web integration, including configuration syncing and code navigation.
4. **Embeddings for NLS**: Using embeddings to enhance the semantic understanding of natural language searches.
5. **Prompt Library & Prompt Extensibility**: Predefined prompts and extensibility features for customizable use.
6. **Telemetry & Feedback Collection**: Systematic data collection to drive improvements and adaptation.
7. **Intent Templates**: Structured templates for better intent handling for LLMs and search tools.
8. **Automatic Personal Ranking**: Intelligent ranking of results tailored to user history and interactions.
9. **Shared Chat History**: Cross-platform continuity of chat conversations.
10. **Advanced Search Paths**: Enhanced paths for advanced and context-specific search queries.

### **Summary Analysis**
The **IDEAL FINAL RELEASE** continues to be a more visionary and ambitious version compared to the milestones. It aims to deliver a **deeply personalized, seamlessly integrated, and contextually aware** product, focusing heavily on **advanced search**, **user context management**, and **interaction continuity**. The updated milestones are practical and achievable steps toward that vision but still lack several of the aspirational features that could make the final product significantly more powerful, user-centric, and efficient.

Would you like to consider bringing any of these aspirational features into earlier milestones, perhaps in a phased or simplified form? It might help accelerate progress towards the fully featured vision while also ensuring there’s incremental value at every stage. Let’s also reflect on how these missing features align with your core user goals and explore how best to prioritize them for iterative releases.

