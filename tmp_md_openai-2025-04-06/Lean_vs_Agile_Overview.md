# Lean vs Agile Overview

Created: 2024-10-12 07:02:36
Last Updated: 2024-10-12 07:18:13

### User - 2024-10-12 07:02:36

How does lean compare to agile in software development?

### Assistant - 2024-10-12 07:02:49



### Assistant - 2024-10-12 07:02:49

Lean and Agile are both methodologies aimed at improving efficiency and delivering value in software development, but they have different origins and focus areas.

### Lean:
- **Origin**: Lean comes from manufacturing, specifically Toyota's production system, and focuses on minimizing waste, improving quality, and maximizing customer value. Lean principles were later adapted to software development.
- **Focus**: Lean focuses heavily on optimizing the flow of work, reducing inefficiencies, and continuously improving processes. The goal is to deliver the right product as efficiently as possible.
- **Principles**: Lean emphasizes eliminating waste (anything that doesn’t add value to the customer), creating knowledge, delaying decisions (until you have enough information), delivering fast, and respecting people.
- **Application**: Lean is particularly concerned with maximizing value by streamlining every step of the process, improving speed, and reducing defects. It is used at both the strategic and operational levels of software development.

### Agile:
- **Origin**: Agile emerged from software development itself, formalized with the publication of the Agile Manifesto in 2001. It was created to help teams adapt quickly to changing requirements and deliver small increments of software continuously.
- **Focus**: Agile emphasizes flexibility, collaboration, and customer feedback. Teams work in short iterations (typically 1-4 weeks) to produce working software, which is reviewed by stakeholders for feedback and adjustments.
- **Principles**: Agile values individuals and interactions, working software, customer collaboration, and responding to change over following a rigid plan. It emphasizes adaptive planning, evolutionary development, early delivery, and continuous improvement.
- **Application**: Agile is most often applied at the project or team level, focusing on delivering value incrementally through iterative cycles and working closely with customers to adjust based on feedback.

### Key Differences:
1. **Scope of Application**:
   - Lean is broader and can be applied to the entire value stream and organization, not just at the team or project level.
   - Agile is more focused on project management and software development processes.

2. **Waste vs. Value**:
   - Lean focuses heavily on eliminating waste (non-value-added activities) from the process to improve efficiency.
   - Agile focuses more on delivering value incrementally and quickly, even if there may be inefficiencies in the process.

3. **Iteration vs. Flow**:
   - Agile works in iterations (sprints), with feedback loops at the end of each cycle to adapt the plan.
   - Lean focuses on continuous flow, aiming for a smooth, uninterrupted progression of work.

4. **Customer Feedback**:
   - Both methodologies emphasize customer feedback, but Agile incorporates it directly into the development cycles (at the end of each iteration), while Lean encourages customer feedback throughout the process but focuses on building the right thing efficiently.

### Similarities:
- **Continuous Improvement**: Both methodologies focus on improving the process continuously through feedback and adaptation.
- **Collaboration**: Both emphasize strong communication and collaboration within teams and with customers.
- **Value Delivery**: Both are concerned with delivering value to the customer, but Agile does it through rapid iteration and Lean through process efficiency.

In practice, many organizations combine elements of both, using Agile to drive the delivery of software and Lean to optimize broader workflows and reduce inefficiencies.

### User - 2024-10-12 07:04:07

Dive deeper into what lean software development looks like

### Assistant - 2024-10-12 07:04:42

Lean software development is an approach derived from Lean manufacturing principles, tailored to optimize software development processes by focusing on delivering maximum value to the customer while minimizing waste. Lean software development is typically structured around seven key principles, which guide how teams operate, make decisions, and improve processes. Here's a deeper dive into how Lean works in a software development environment:

### 1. **Eliminate Waste**
Waste in Lean software development refers to any activity that does not add value to the customer. In software development, there are several types of waste to consider:
   - **Partially Done Work**: Features or tasks that are started but not completed, which can lead to hidden costs, increased complexity, and delays.
   - **Extra Processes**: Activities such as unnecessary approvals, extensive documentation, or meetings that do not directly contribute to the development of valuable software.
   - **Extra Features**: Features that are not necessary but are included 'just in case,' leading to bloated systems that require maintenance.
   - **Delays**: Any bottleneck in the process that slows down the delivery of value, such as long feedback loops or waiting for resources.
   - **Hand-offs**: Every time work is handed off between teams or individuals, knowledge and efficiency can be lost, leading to miscommunication or errors.
   - **Task Switching**: Multitasking or switching between different tasks can reduce efficiency, as it disrupts flow and increases cognitive load.
   - **Defects**: Bugs or quality issues that result in rework, causing additional costs and delays.

In practice, eliminating waste means regularly examining workflows, identifying inefficiencies, and improving processes. Lean software teams are encouraged to question whether each task or feature adds direct value to the end user and to eliminate anything that doesn't.

### 2. **Build Quality In**
Building quality into the product from the start, rather than relying on extensive testing at the end, is a core principle of Lean. In software development, this principle translates to:
   - **Test-Driven Development (TDD)**: Writing tests before writing code to ensure that the software behaves as expected from the start.
   - **Continuous Integration (CI)**: Regularly integrating code into a shared repository, where automated tests can quickly identify defects or integration issues.
   - **Pair Programming or Code Reviews**: Encouraging collaborative work and peer review to catch errors early and ensure that quality is upheld throughout the development process.
   - **Automated Testing**: Implementing unit, integration, and end-to-end tests that run automatically to quickly detect issues in new code.

By incorporating these practices, Lean software development aims to prevent defects and maintain a high level of quality as the software evolves.

### 3. **Create Knowledge**
In Lean software development, learning is a fundamental part of improving the system. The process of creating software is seen as an opportunity to create knowledge for both the development team and the organization:
   - **Short Feedback Loops**: Regular iterations and customer feedback allow teams to learn what works and what doesn’t, minimizing the risk of building the wrong thing.
   - **Documentation as Learning**: Instead of overloading teams with documentation upfront, Lean encourages creating 'just enough' documentation at the right times to support development. The focus is on learning through doing and adjusting based on that learning.
   - **Experiments and Prototypes**: Building small experiments or prototypes helps teams validate assumptions quickly and learn about the product's value, feasibility, and potential customer adoption.
   - **Knowledge Sharing**: Encouraging cross-functional teams to collaborate and share knowledge, so insights gained during development are not siloed within a single person or team.

### 4. **Defer Commitment**
In Lean, teams are encouraged to delay decisions until the last responsible moment. This principle, sometimes referred to as 'delayed decision-making,' ensures that teams make choices with the most complete and accurate information possible:
   - **Flexible Architecture**: Design systems to be adaptable, allowing teams to incorporate changes later without having to overhaul large portions of the codebase.
   - **Incremental Decision-Making**: Rather than committing to a full set of features upfront, development teams can make decisions incrementally, based on new information and changing customer needs.
   - **Keeping Options Open**: Teams focus on designing solutions that do not prematurely lock them into a specific implementation path, keeping future options open for changes or pivots.
   
This approach reduces the risk of building features that might not be needed or making technical decisions that become costly to reverse later.

### 5. **Deliver Fast**
Speed is crucial in Lean software development, not for its own sake but because fast delivery enables rapid feedback from users, which in turn helps guide the direction of the product:
   - **Short Iterations**: Similar to Agile, Lean promotes breaking work into small, manageable pieces and delivering them frequently, so feedback can be gathered and integrated quickly.
   - **Reduce Cycle Time**: Lean teams focus on reducing the time it takes to go from idea to deployment. This involves streamlining processes, reducing hand-offs, and removing bottlenecks.
   - **Small Batch Sizes**: Working in small batches (e.g., incremental feature development, frequent releases) helps teams deliver faster and catch issues early before they become too costly to fix.

This principle is about reducing delays in feedback and continuously improving by incorporating customer input as quickly as possible.

### 6. **Respect People**
Respecting people is central to Lean thinking. This applies to the development team, stakeholders, and customers:
   - **Empowered Teams**: Teams are given the autonomy to make decisions about their work. They are trusted to self-organize, collaborate, and figure out the best way to achieve their goals.
   - **Collaboration Over Control**: Instead of rigid management oversight, Lean encourages a culture of collaboration, where developers, designers, and other stakeholders work together to deliver the best possible product.
   - **Respect for Customer Needs**: In Lean, the customer’s needs are central to every decision. Teams must ensure they understand what the customer values and work to deliver that value efficiently.

### 7. **Optimize the Whole**
Lean software development emphasizes optimizing the entire process, not just individual parts. This is about taking a systems-thinking approach, where teams focus on improving the flow of work across the entire value stream, from concept to delivery:
   - **Cross-Functional Teams**: Lean promotes cross-functional teams that can take a feature from idea to production without unnecessary hand-offs between different departments.
   - **Avoid Local Optimization**: Optimizing one part of the system (e.g., speeding up development without improving testing) might create bottlenecks elsewhere. Lean focuses on end-to-end optimization to deliver a smooth and efficient process.
   - **Continuous Improvement (Kaizen)**: Regularly analyzing processes and identifying areas for improvement is key. Teams look at metrics like cycle time, lead time, and quality metrics to ensure they are consistently optimizing the whole process.

By focusing on the entire value stream, Lean ensures that improvements in one area do not negatively impact others and that the process is always improving holistically.

### Lean Tools and Practices in Software Development:
- **Kanban Boards**: Visualizing work through a Kanban board helps teams see the flow of tasks, identify bottlenecks, and ensure continuous delivery.
- **Value Stream Mapping**: This tool helps teams analyze the flow of information and materials required to bring a product to the customer. It is used to identify waste and areas of improvement.
- **Pull Systems**: Work is 'pulled' into the process based on capacity rather than 'pushed' into the system based on arbitrary deadlines. This reduces overloading teams and ensures a steady, manageable flow of work.
- **Continuous Deployment/Delivery (CD)**: Automated deployment processes help ensure that new features or fixes can be delivered to users as soon as they are ready, reducing the time to market.

### In Summary:
Lean software development aims to maximize value by optimizing the flow of work, reducing waste, and delivering quickly. It is a highly customer-focused and process-efficient methodology that prioritizes flexibility, learning, and continuous improvement. In a Lean software development environment, the focus is on creating a smooth, waste-free process that allows teams to build the right product in the most efficient way possible.

### User - 2024-10-12 07:07:32

Dig more into value stream mapping. How does it work, especially for a software product

### Assistant - 2024-10-12 07:08:17

Value Stream Mapping (VSM) is a Lean tool used to visualize and analyze the flow of materials, information, and processes required to deliver a product or service to the customer. When applied to software development, VSM helps teams understand how value flows (or doesn't) through the development lifecycle, identifying areas of waste, bottlenecks, and opportunities for improvement.

Here's a deep dive into how Value Stream Mapping works in the context of a software product and how it can be applied:

### What is Value Stream Mapping in Software Development?

In software development, a **value stream** is the sequence of activities and processes that are required to design, develop, test, and deliver software to customers. The value stream includes both the activities that directly contribute to delivering value (like coding and testing) and those that don’t (like waiting for approvals or dealing with defects).

A **Value Stream Map** visually represents these activities, capturing:
- The flow of work (from idea to production)
- The flow of information (such as feedback loops or communications)
- The time taken for each activity
- The delays, bottlenecks, or inefficiencies that occur along the way

By mapping the current state of the value stream, teams can see how value is added (or lost) at each step and identify where waste occurs, which helps guide improvements.

### The Steps to Create a Value Stream Map

Here’s a step-by-step breakdown of how to create a Value Stream Map for a software product:

#### 1. **Define the Product or Service**
Start by identifying the software product or specific service you want to map. For example, this could be a new feature, an enhancement to an existing feature, or an entire product release process.

#### 2. **Identify the Value Stream’s Start and End Points**
Define the start and end points of the value stream. For software, the start point might be when a customer or product manager identifies a need or requirement, and the end point might be when the feature or product is deployed to production and in use by customers.

Example start and end points:
- **Start**: Idea generation or ticket creation (such as a feature request).
- **End**: Deployment to production and feedback from users or monitoring systems.

#### 3. **Map the Key Process Steps**
Identify all the major steps in the development process. This includes all the activities involved in going from idea to delivery. Typical steps in a software product’s value stream might include:
   - Requirements gathering
   - Design and architecture planning
   - Coding and development
   - Code review and testing (unit, integration, and acceptance tests)
   - Deployment preparation (e.g., creating deployment scripts)
   - Deployment to staging and production
   - Feedback (from users, QA, or automated monitoring systems)

For each step, it’s important to note both the **value-added activities** (those that directly contribute to delivering value) and **non-value-added activities** (waste, such as waiting for reviews or approvals).

#### 4. **Collect Data for Each Step**
To make the Value Stream Map useful, you need to gather data for each step in the process. Key metrics include:
   - **Cycle time**: The actual time spent working on a task.
   - **Lead time**: The total time from when a task is initiated to when it is completed, including waiting times.
   - **Waiting time**: Time spent waiting for approvals, feedback, or resources (e.g., waiting for code review or deployment).
   - **WIP (Work in Progress)**: The amount of work currently in progress at any given stage.
   - **Handoffs**: How many times the work is passed between teams or individuals.

This data gives insight into where delays, bottlenecks, or inefficiencies occur.

#### 5. **Visualize the Flow**
Using the data gathered, you can create a visual map that shows the flow of work and information through the process. This map should include:
   - **Process boxes**: Represent each major process step, along with its cycle time and lead time.
   - **Arrows**: Show the flow of work and information between steps.
   - **Delays**: Mark areas where waiting occurs (e.g., waiting for a review or approval).
   - **Handoffs**: Highlight areas where work is passed between teams or systems, as this can introduce delays or errors.

For software development, tools like sticky notes, whiteboards, or digital tools like Miro, Lucidchart, or even Jira can be used to create and visualize the map.

#### 6. **Identify Bottlenecks and Waste**
Once the map is complete, analyze it for inefficiencies or areas of waste. Common bottlenecks or waste in software development include:
   - Long wait times for code reviews or testing.
   - Handoffs between development, QA, and operations teams that cause delays.
   - Excessive work-in-progress, which leads to task switching and reduced focus.
   - Too many approvals required before moving work forward.
   - Time spent debugging or reworking due to defects.
   - Unnecessary features being built that don’t directly add customer value.

### Types of Waste Identified in a Value Stream Map (for Software Development)
The seven classic Lean wastes apply to software as well:
1. **Partially Done Work**: Unfinished features, unmerged branches, or tasks that are in progress but not yet delivered.
2. **Extra Features**: Building features that aren't required by the customer or product vision.
3. **Relearning**: Time spent re-exploring or re-solving a problem due to inadequate knowledge sharing or documentation.
4. **Task Switching**: Developers or teams constantly switching between tasks, leading to loss of focus.
5. **Waiting**: Idle time waiting for code reviews, approvals, or resources.
6. **Handoffs**: Delays and miscommunication introduced when work is transferred between different teams (e.g., from developers to testers).
7. **Defects**: Bugs or technical debt that require rework.

By identifying these wastes, teams can start planning improvements to streamline the value stream.

### 7. **Create the Future State Map**
Once you’ve identified inefficiencies in the current state map, the next step is to create a **future state map**. This is a map that visualizes an improved version of the value stream, where bottlenecks are removed, waste is minimized, and the flow of value is optimized. The goal is to:
   - Reduce delays and waiting times.
   - Automate or simplify repetitive manual tasks (e.g., automating testing and deployment processes).
   - Reduce handoffs and foster more collaboration between teams (e.g., by promoting cross-functional teams).
   - Limit WIP by using techniques like Kanban or limiting the number of concurrent tasks per developer.
   - Improve quality by adopting practices like continuous integration, test-driven development, and pair programming.

The future state map should reflect the ideal workflow that maximizes efficiency and delivers the most value in the shortest time.

### 8. **Implement Changes and Continuously Improve**
After mapping the future state, the next step is to start implementing changes. This often involves making incremental improvements, experimenting with new processes, and gathering feedback on the impact of these changes. Continuous improvement (or **Kaizen**) is a core Lean principle, so teams should continuously revisit their value stream and make adjustments as needed.

### Tools for Value Stream Mapping in Software Development
To create and manage a Value Stream Map, teams can use:
   - **Whiteboards and sticky notes** for quick and collaborative mapping sessions.
   - **Digital tools** like Miro, Lucidchart, or dedicated value stream mapping tools like **Plutora** or **Tasktop Viz** for more complex maps.
   - **Kanban Boards** to track the progress of tasks through various stages and identify bottlenecks in real-time.
   - **Jira or other issue-tracking systems** for collecting data about cycle times, lead times, and WIP.

### Value Stream Mapping Example in Software Development

Here’s a basic example for a software development process:

1. **Start**: Feature Request (Product Management or Customer Request)
   - Lead Time: 2 days (discussion and prioritization)
2. **Requirement Analysis & Design**: Development team designs the architecture and requirements.
   - Cycle Time: 4 days (planning, design docs, and initial approvals)
   - Waiting Time: 1 day (for product manager feedback)
3. **Development**: Coding the feature.
   - Cycle Time: 7 days (active coding)
   - Waiting Time: 2 days (waiting for code review)
4. **Testing**: Quality Assurance and automated testing.
   - Cycle Time: 3 days (testing)
   - Waiting Time: 1 day (environment setup)
5. **Deployment**: Deployment to production.
   - Cycle Time: 1 day (deployment process)
   - Waiting Time: 2 days (waiting for operations team approval)

In this example, the team identifies long waiting times between coding and review, and testing and deployment. By introducing automated testing and a more collaborative code review process, they can reduce those delays in the future state.

### Conclusion
Value Stream Mapping is a powerful tool for visualizing, analyzing, and improving software development processes. It helps teams identify where value is lost or delayed, and provides a structured approach to reducing waste, streamlining workflows, and delivering software faster and with higher quality. By focusing on optimizing the entire value stream, teams can increase both efficiency and customer satisfaction.

### User - 2024-10-12 07:14:04

How does value stream mapping compare to eventstorming?

### Assistant - 2024-10-12 07:14:41

Value Stream Mapping (VSM) and EventStorming are both techniques used to analyze and improve processes, but they come from different backgrounds and focus on different aspects of software development. Here's a comparison of the two methodologies:

### 1. **Purpose and Focus**

- **Value Stream Mapping (VSM)**:
  - **Purpose**: VSM is a Lean tool designed to visualize and optimize the entire flow of activities in a process, from the initial request (or idea) to the delivery of the final product.
  - **Focus**: VSM focuses on understanding and improving the efficiency of the whole system by identifying bottlenecks, delays, and areas of waste. It’s more concerned with the flow of value and time-based metrics (like cycle times and lead times) through each stage of the process.
  - **End Goal**: The ultimate goal of VSM is to improve the efficiency of delivering value to the customer by minimizing waste and optimizing the flow of work.

- **EventStorming**:
  - **Purpose**: EventStorming is a workshop-based technique designed for domain modeling, primarily within the context of Domain-Driven Design (DDD). It’s used to explore and understand complex business domains and workflows through the lens of domain events (significant business occurrences).
  - **Focus**: EventStorming focuses on uncovering and understanding the behavior of the system by mapping out events, commands, and aggregates (central entities in a system). It is more concerned with **understanding the business logic and domain complexity** rather than time-based flow or efficiency.
  - **End Goal**: The goal of EventStorming is to foster a shared understanding of the domain, identify pain points, and collaboratively design solutions that reflect the business processes accurately.

### 2. **Application Areas**

- **Value Stream Mapping (VSM)**:
  - **System Level**: VSM is generally used to analyze the entire end-to-end process, often spanning multiple teams, departments, or organizational units. It’s well-suited to both software and non-software contexts (e.g., manufacturing, service delivery).
  - **Macro-Level Focus**: VSM is used to improve high-level workflows, looking at how work flows through development, testing, deployment, and even operations.
  - **Best for**: Optimizing large-scale processes, identifying bottlenecks in the flow of work, and improving overall organizational efficiency.

- **EventStorming**:
  - **Domain Modeling**: EventStorming is often used during the design and planning phases of software development. It is focused on domain modeling, understanding how systems work in detail, and defining the core logic of a system based on domain events.
  - **Micro-Level Focus**: It is more focused on individual workflows or bounded contexts (specific areas within a system that are independently managed) and understanding how they interrelate.
  - **Best for**: Gaining insights into a business’s domain model, exploring complex systems, and collaborating across technical and non-technical teams to design or refactor systems.

### 3. **Methodology**

- **Value Stream Mapping (VSM)**:
  - **Visual Flow Map**: VSM uses a structured approach to map out every step in a process, measuring each step’s cycle time, lead time, and the delays between them. It typically includes activities like identifying handoffs, bottlenecks, and waste (e.g., waiting times or unnecessary approvals).
  - **Data-Driven**: VSM heavily relies on quantitative metrics such as cycle time (the time spent on each step) and lead time (the total time from start to finish), making it more focused on efficiency and productivity improvements.
  - **Participants**: Involves people from different teams or departments, often at a management or process owner level, to map out the end-to-end flow and understand how to optimize it.

- **EventStorming**:
  - **Freeform Exploration**: EventStorming uses sticky notes or other visual aids to represent domain events (key moments in the business), commands (actions that trigger events), and aggregates (core entities or decision points). The goal is to collaboratively explore the system's domain without predefining the process structure.
  - **Collaborative and Visual**: It’s a highly collaborative, creative, and exploratory technique, encouraging teams to think through the domain together and spot gaps in knowledge or unclear areas of the business.
  - **Participants**: Typically involves domain experts, software developers, product owners, and business stakeholders in a room to discuss how the system works, making it highly interactive.

### 4. **Outcome and Benefits**

- **Value Stream Mapping (VSM)**:
  - **Outcome**: A detailed map of the current process, highlighting inefficiencies and opportunities for improvement. The next step is to create a "future state" map, which represents the ideal, optimized process flow.
  - **Benefits**: Helps identify and eliminate waste, reduce delays, and improve the flow of value. It is especially useful for teams trying to reduce lead time or improve the overall efficiency of software delivery.

- **EventStorming**:
  - **Outcome**: A detailed domain model that visualizes the business events and workflows, enabling teams to understand the system's behavior and design better solutions. It helps teams reach a shared understanding of the business logic and the domain's key concepts.
  - **Benefits**: Helps clarify complex systems, bring business and technical stakeholders onto the same page, and ensure that the system is being built to reflect the true business requirements. It’s particularly effective for discovering edge cases or understanding where a system might break down due to incomplete requirements.

### 5. **Comparison of Focus Areas**

| Aspect                          | **Value Stream Mapping (VSM)**                    | **EventStorming**                            |
|----------------------------------|--------------------------------------------------|----------------------------------------------|
| **Primary Purpose**              | Optimize process efficiency and reduce waste      | Model and understand domain complexity       |
| **Key Focus**                    | End-to-end process flow and time-based metrics    | Business events, domain logic, and behaviors |
| **Level of Focus**               | Macro (entire process, organizational level)      | Micro (specific system or domain)            |
| **Output**                       | Current and future state process maps             | Detailed domain models with events and commands |
| **Participants**                 | Process owners, managers, cross-functional teams  | Developers, domain experts, business stakeholders |
| **Approach**                     | Data-driven, structured                          | Collaborative, exploratory                   |
| **Best Used For**                | Improving efficiency, identifying bottlenecks     | Gaining a shared understanding of domain models |
| **Types of Waste Identified**    | Bottlenecks, delays, unnecessary steps            | Missing events, unclear logic, domain complexity |

### When to Use Each?

- **Use VSM when**: 
  - You want to improve the overall efficiency of your software delivery process.
  - You need to reduce bottlenecks and eliminate waste in the flow of work.
  - Your focus is on optimizing an end-to-end process across multiple teams or departments.
  - You're looking to optimize cycle times, reduce lead times, or streamline the delivery pipeline.
  
- **Use EventStorming when**:
  - You're trying to understand a complex domain and improve your team’s shared understanding of it.
  - You’re designing or refactoring a system and need to explore domain events, business logic, and workflows.
  - You want to foster collaboration between technical and non-technical stakeholders to solve a business problem.
  - You need to model how the system should behave from the perspective of business events and interactions.

### Conclusion

While both Value Stream Mapping and EventStorming are valuable tools, they serve different purposes and are used at different stages of the software development lifecycle. VSM is about optimizing processes to improve efficiency, while EventStorming is about understanding and modeling complex domains to create better systems. Both approaches complement each other in an organization’s Lean or Agile transformation journey, as they focus on improving the flow of work (VSM) and ensuring that work reflects the right business logic and behavior (EventStorming).

### User - 2024-10-12 07:17:48

Give a concrete example of when in a software development one or the other is valuable

### Assistant - 2024-10-12 07:18:12

### **Example of Value Stream Mapping (VSM): Optimizing the Feature Development Process**

#### **Scenario**:
A software development team at a mid-sized tech company notices that despite meeting sprint commitments, their features are consistently delayed before reaching production. Stakeholders are frustrated with the long lead time from when a feature is requested to when it is delivered, even though individual developers are productive. The team decides to use **Value Stream Mapping** to identify and address inefficiencies.

#### **Steps Using VSM**:
1. **Define the Start and End Points**: 
   - **Start**: A new feature is requested and added to the product backlog.
   - **End**: The feature is deployed to production and used by customers.

2. **Map the Process**:
   - Requirements gathering and analysis (2 days)
   - Design (3 days)
   - Coding (5 days)
   - Code review (waiting 2 days)
   - Testing (waiting 3 days for QA environment setup, 2 days for actual testing)
   - Deployment (waiting 4 days for deployment window)

3. **Collect Data**:
   - Lead time: 20 days (total time from request to production)
   - Cycle time: 12 days (actual time spent working on the feature)
   - Waiting time: 8 days (time spent waiting for reviews, testing, and deployment)
   
4. **Identify Waste**:
   - Long wait times for code review and QA testing environments.
   - Delays in deployment windows due to scheduling with operations.

5. **Create a Future State Map**:
   - Automate environment provisioning to reduce testing wait times.
   - Implement a continuous integration and deployment pipeline to remove the bottleneck of manual deployments.
   - Reduce batch sizes in deployments to allow for smaller, more frequent releases.

6. **Result**:
   - Reduced lead time to 14 days by cutting down waiting times.
   - Improved cycle time with automated deployments and more efficient handoffs between teams.

#### **When VSM is Valuable**:
In this case, VSM was valuable because the team was looking to **optimize the entire end-to-end feature development process**, identify bottlenecks, and reduce inefficiencies (especially in handoffs and wait times). By visualizing the flow of work and collecting data on delays, the team was able to streamline their development pipeline and deliver features faster.

---

### **Example of EventStorming: Modeling a New Subscription Feature**

#### **Scenario**:
A product team is tasked with developing a new subscription billing feature for an e-commerce platform. The feature is complex, involving various business rules for different subscription tiers, promotions, and payment failures. The developers and product managers have a rough idea of the requirements but realize they need a deeper understanding of the business logic before starting development. They use **EventStorming** to explore the domain and clarify the feature's workflow.

#### **Steps Using EventStorming**:
1. **Gather the Right Stakeholders**:
   - Include product managers, domain experts from the finance team, software developers, and customer support to ensure all perspectives are represented.

2. **Map Out Domain Events**:
   - The team starts by mapping key **domain events** in the subscription workflow:
     - Customer subscribes.
     - Payment is processed.
     - Subscription is activated.
     - Payment fails.
     - Subscription renews.
     - Customer cancels the subscription.
     - Subscription expires.

3. **Identify Commands and Aggregates**:
   - **Commands**: Actions triggered by users or the system, such as "Process Payment" or "Cancel Subscription."
   - **Aggregates**: Key entities that manage the business logic, such as the **Subscription** and **Payment** aggregates.

4. **Explore Edge Cases**:
   - During the EventStorming session, the team uncovers critical scenarios they hadn’t fully considered, such as:
     - What happens when a customer changes subscription tiers mid-cycle?
     - What are the rules for promotional discounts when a payment fails?
     - How do we handle pro-rated refunds for canceled subscriptions?

5. **Collaborative Understanding**:
   - Through EventStorming, the team develops a shared understanding of how the subscription system should behave, identifying missing business rules and clarifying how different systems (e.g., the payment processor, customer support tools) need to interact.

6. **Result**:
   - The developers are now equipped with a clear domain model, complete with well-defined events, commands, and aggregates. The product manager and finance team have confidence that the system reflects the business requirements, and the team can move forward with implementation.

#### **When EventStorming is Valuable**:
EventStorming was valuable in this case because the team needed to **model a complex business domain** and ensure that everyone, from developers to domain experts, had a shared understanding of how the subscription system should work. By focusing on domain events and workflows, they could identify gaps, edge cases, and dependencies that might have been missed in a traditional requirements-gathering process.

---

### **Comparison of When to Use Each**:

- **Use Value Stream Mapping when**: 
  - You want to **optimize the flow** of work in your development or delivery pipeline.
  - You need to **reduce delays, bottlenecks, or inefficiencies** in the software delivery process.
  - Your focus is on **improving end-to-end efficiency**, from idea to production.
  - Example: Addressing inefficiencies in how features are delivered from planning to deployment.

- **Use EventStorming when**:
  - You need to **explore and clarify complex business logic or workflows** in a domain.
  - You're designing a system that requires deep collaboration between **business and technical teams** to ensure the correct behavior is implemented.
  - The goal is to **model domain events** and ensure a shared understanding of the system's behavior.
  - Example: Understanding how a new subscription billing system should behave with various rules, promotions, and failure conditions.

In summary, VSM is best for improving process efficiency across a flow of work, while EventStorming is best for understanding complex business processes and workflows at a granular, domain-specific level.

