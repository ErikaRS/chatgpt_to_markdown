# Effective Subdomain Creation

Created: 2024-03-28 14:57:49
Last Updated: 2024-03-28 15:05:45

### User - 2024-03-28 14:57:49

What does Team Topologies have to say about the effective creation of subdomains when there is shared code?

### Assistant - 2024-03-28 14:58:22

"Team Topologies" by Matthew Skelton and Manuel Pais is a book that provides a framework for structuring teams in a way that optimizes their workflows and communication patterns, especially in the context of software development. One of the key aspects of the book is the strategic division of software systems into domains and subdomains, and how teams can be organized around these to maximize efficiency and minimize bottlenecks.

When it comes to the creation of subdomains in the presence of shared code, the book emphasizes a few important principles:

1. **Conway's Law**: The book reiterates Conway's Law, which suggests that any organization that designs a system (broadly defined) will produce a design whose structure is a copy of the organization's communication structure. This implies that if you have a shared codebase, you need to carefully consider how the teams are structured around it to ensure that the architecture supports rather than conflicts with this.

2. **Cognitive Load**: "Team Topologies" stresses the importance of managing the cognitive load on development teams. When dealing with shared code, it's crucial to ensure that the teams are not overwhelmed by the complexity of the system. This may involve creating clear boundaries around subdomains so that each team can focus on a specific aspect of the system without being bogged down by the entirety of the shared code.

3. **Team Interactions**: The book outlines four fundamental types of team interactions: collaboration, X-as-a-Service, facilitating, and stream-aligned. For effective creation and management of subdomains with shared code, the book might suggest structuring interactions around these models. For instance, if two teams are working on closely related subdomains, they might engage in a collaboration interaction mode to jointly develop shared components. Alternatively, one team might provide components as a service to other teams, thereby encapsulating the shared code and reducing direct dependencies between teams.

4. **Enabling Teams**: To support the effective creation of subdomains and management of shared code, "Team Topologies" introduces the concept of Enabling Teams. These teams help other teams overcome technical challenges and learn new technologies or practices. In the context of shared code, an Enabling Team could help disseminate best practices for code reuse, modularization, and creating interfaces between subdomains.

5. **Evolutionary Architecture**: The book acknowledges that both organizational structures and software architectures evolve over time. As such, the division into subdomains and the management of shared code should be revisited regularly to ensure they still meet the needs of the business and the teams. This might involve refactoring the shared code or redefining subdomain boundaries as the system and organization evolve.

"Team Topologies" essentially advocates for a thoughtful approach to organizational and architectural design, recognizing that the way teams are structured and interact has a profound impact on the software they produce, especially when dealing with shared code. The aim is to create a harmonious relationship between team organization and software architecture that promotes efficiency, reduces cognitive load, and enables a more adaptable and resilient system.

### User - 2024-03-28 15:02:15

When a domain is large enough to be split into subdomains but the de facto architecture is the Big Ball of Mud, how can teams move toward clear subdomains without getting stuck on unproductive ownership arguments?

### Assistant - 2024-03-28 15:02:50

When a domain is large enough to require splitting into subdomains but is currently entangled in a "Big Ball of Mud" architecture, transitioning to a more structured and efficient model presents several challenges. One of the primary obstacles is avoiding unproductive ownership arguments among teams. Here are strategies inspired by principles from "Team Topologies" and other best practices in software development to facilitate this transition:

1. **Align Around Business Capabilities**: Start by aligning teams and subdomains around business capabilities rather than technical functions. This helps clarify ownership based on business outcomes rather than technical components, which can reduce territorial disputes among teams.

2. **Incremental Refactoring**: Instead of attempting a big-bang rearchitecture, opt for an incremental approach. Identify the most critical or easiest-to-separate parts of the system and start by modularizing those. This approach reduces risk and allows teams to gradually assume ownership of clearly defined pieces of the system.

3. **Create Enabling Teams**: Utilize Enabling Teams to support other teams during the transition. These teams can offer expertise in modular design, domain-driven design, and other practices necessary for breaking down a Big Ball of Mud. They can also help mediate between teams to resolve disputes and ensure a smooth handover of responsibilities.

4. **Use Domain-Driven Design (DDD) Principles**: DDD can provide a framework for identifying bounded contexts within the larger domain, which can then inform the creation of subdomains. This method helps in creating clear boundaries and interfaces between parts of the system, making ownership clearer.

5. **Adopt a Platform Thinking Approach**: Develop a set of shared tools and services that all teams can use. This reduces the duplication of effort and the territoriality over shared code. A platform team can manage these shared resources, freeing up feature teams to focus on their specific subdomains.

6. **Facilitate Open Communication and Collaboration**: Encourage a culture of open communication and collaboration between teams. Regular cross-team meetings, shared documentation, and mutual goals can help align teams towards the larger vision rather than getting bogged down in ownership disputes.

7. **Implement Shared Governance**: Establish a governance model that involves representatives from all teams. This governance body can make decisions on cross-cutting concerns, shared code, and APIs, ensuring that all voices are heard and that decisions are made in the best interest of the organization as a whole.

8. **Celebrate Small Wins**: Recognize and celebrate progress along the way. Highlighting successful refactoring efforts, improved metrics, or enhanced team autonomy can build momentum and encourage continued collaboration and improvement.

9. **Use Metrics to Guide Improvement**: Implement metrics to measure the impact of changes on code quality, team productivity, and business outcomes. These metrics can help justify the transition efforts and guide future improvements.

Transitioning from a Big Ball of Mud to clear, manageable subdomains is a challenging but critical process for organizations looking to improve their software architecture and team efficiency. By focusing on incremental change, aligning around business capabilities, and fostering collaboration, teams can navigate this transition more smoothly and avoid getting stuck in counterproductive ownership arguments.

### User - 2024-03-28 15:03:57

What are business capabilities in this context?

### Assistant - 2024-03-28 15:04:33

In the context of software development and organizational structure, business capabilities refer to the specific abilities or capacities that a business possesses to achieve its goals and deliver value to its customers. These capabilities represent the combination of processes, technologies, and people that enable a company to perform essential functions and services. Essentially, business capabilities are high-level descriptions of what a business does, distinct from how it does it.

Here's a breakdown to better understand business capabilities in this context:

1. **High-Level Functions**: Business capabilities describe what a business does at a high level, such as "order management," "customer support," "product development," or "marketing." These capabilities are typically stable over time, even as the underlying processes and technologies change.

2. **Focus on Outcomes**: Unlike specific processes or technologies, business capabilities focus on outcomes and the value delivered to the business and its customers. For example, a capability like "market analysis" focuses on the outcome of understanding market trends and customer needs, regardless of the specific tools or methods used.

3. **Alignment with Strategy**: Business capabilities are often aligned with the strategic goals and objectives of the organization. They help in mapping out the necessary functions to achieve these goals, facilitating a clear understanding of where investments in technology, processes, and people are needed.

4. **Basis for Organizational Structure**: In the context of "Team Topologies" and other modern approaches to organizational design, businesses are encouraged to structure their teams around these capabilities. This alignment helps ensure that teams are focused on delivering specific business outcomes, promoting efficiency and reducing cross-functional dependencies.

5. **Framework for Technology Investment**: Understanding the business capabilities helps organizations decide where to invest in technology and development efforts. It aids in prioritizing projects and resources based on their impact on essential business functions.

6. **Tool for Identifying Bounded Contexts**: In software architecture, especially when applying Domain-Driven Design (DDD), business capabilities can help identify bounded contexts. These are specific areas of the business with coherent functionality and data requirements, around which software systems can be designed and developed.

By focusing on business capabilities, organizations can create a more adaptable and responsive structure, where teams are empowered to deliver value efficiently. This approach also supports a clearer division into subdomains and facilitates a smoother transition away from monolithic architectures or the "Big Ball of Mud" scenario by providing a stable foundation for organizing teams and technology around the key functions that drive business success.

### User - 2024-03-28 15:05:05

Review the core concepts of domain driven design. Assume I've read Eric Evans book but it's been awhile.

### Assistant - 2024-03-28 15:05:45

Certainly! Domain-Driven Design (DDD), as articulated by Eric Evans in his seminal book, is a software design approach focused on modeling complex software systems according to the domain they aim to represent and solve problems for. Here's a refresher on the core concepts of DDD:

### 1. **Ubiquitous Language**
- A common language used by developers, domain experts, and stakeholders throughout the project. This language should be based on the domain model and used consistently in both verbal communication and in the code.

### 2. **Domain Model**
- A conceptual model that captures the fundamental truths of the problem domain. It is the heart of DDD, where the complexity of the domain is addressed with a carefully crafted model that reflects the entities, their attributes, and relationships, as well as the business rules.

### 3. **Bounded Context**
- The boundary within which a particular domain model is defined and applicable. It is essential for dealing with large models and systems by dividing them into manageable segments, each with its own ubiquitous language and domain model.

### 4. **Entities**
- Objects that are not primarily defined by their attributes, but rather by a thread of continuity and identity. An entity has an ID that distinguishes it from other entities.

### 5. **Value Objects**
- Objects that are defined only by their attributes and do not have a conceptual identity. They are immutable and can be replaced wholesale if the data changes.

### 6. **Aggregates**
- A cluster of domain objects that can be treated as a single unit. An aggregate has a root and a boundary. The root is a single, specific entity contained in the aggregate. The boundary defines what is inside the aggregate and what is outside.

### 7. **Aggregate Root**
- The entity within the aggregate that is responsible for checking invariants and rules within the aggregate and acts as the only point of interaction for external objects.

### 8. **Repositories**
- Mechanisms for encapsulating storage, retrieval, and search behavior, which emulates a collection of objects of a certain type. Repositories provide a way to access aggregates or entities without requiring knowledge of the underlying database or storage mechanisms.

### 9. **Domain Events**
- Significant business events that trigger a change in the domain. These events are used to communicate between different parts of the domain model and can be used to trigger side effects in other parts of the system.

### 10. **Services**
- Operations that don’t naturally fit within the CRUD (Create, Read, Update, Delete) model of entities or value objects. Services can be domain services (handling domain logic that doesn't naturally fit into an entity or value object) or application services (handling application logic and workflows).

### 11. **Context Mapping**
- A strategy to manage and identify the relationships and boundaries between different bounded contexts in a system. It is crucial for understanding how different parts of the system interact and integrate with each other.

### 12. **Strategic Design**
- Refers to the higher-level planning of the system architecture, dealing with large-scale structures, bounded contexts, and the relationships between them. It includes decisions on how to partition the system into different bounded contexts.

### 13. **Tactical Design**
- Focuses on the finer details of modeling the domain within individual bounded contexts. It involves creating effective models using entities, value objects, aggregates, domain events, and applying patterns like Repository and Factory effectively.

Revisiting and applying these core DDD concepts can help in dealing with complex systems by focusing on the domain itself and fostering a deep connection and understanding between software practitioners and domain experts.

