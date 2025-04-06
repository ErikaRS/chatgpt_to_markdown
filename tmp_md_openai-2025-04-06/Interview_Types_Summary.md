# Interview Types Summary

Created: 2024-10-04 13:31:31
Last Updated: 2024-10-04 15:44:08

### User - 2024-10-04 13:31:31

Here is one interview document. List out the types of interviews identified in this doc using a title and 1 sentence summary.

Our Hiring Managers work with their assigned Recruiter to create an optimal interview plan for their role. We strive to create a fair and equitable interview process for all candidates and have built out structured types of interviews to best suit the type of role you are looking to fill.

The Source of Truth for all interviews is Greenhouse. If you would like to make a change, please send a message to your Recruiter via the private Slack channel.

[Private interview documentation](https://github.com/sourcegraph/interviews/tree/master/engineering/software-engineer)

### Types of Interviews

### Architecture

[Internal Documentation - Backend Systems](https://github.com/sourcegraph/interviews/blob/master/engineering/software-engineer/architecture/backend-systems/backend-systems.md)

[Internal Documentation - Source/Repo management](https://github.com/sourcegraph/interviews/blob/master/engineering/software-engineer/architecture/repo-management/README.md)

- **Interviewers:** two members of the team they are interviewing for
- **Duration:** 60-minutes
- **How the candidate will prepare:** They will discuss how they would design a new system from scratch. You will work with them in this collaborative session to think about and design the system together, looking for their natural intuition about building systems and problem-solving as you throw various wrenches into the system. The interview consists of open-ended questions, allowing them to describe your mental model of designing a new system from scratch - you’ll want to understand the decisions they are making when designing system architectures. You will ask clarifying questions as the requirements for the system are purposefully ambiguous.
- **What to look for:**
    - How do they identify and resolve ambiguity?
    - How do they make tradeoffs?
    - How do they communicate their proposal?
    - What is it like to work with them on a problem they haven’t seen before?
    - What is their intuition about solutions that are likely to yield good results?
- We expect them to be designing systems that often need to meet conflicting or ambiguous requirements. For engineers in these roles, a significant part of their journey in Sourcegraph is going to be designing new or improving existing systems to fit these new requirements.

### Technical Interview: General

- **Interviewers:** two members of the team they are interviewing for
- **Duration:** 45-minutes
- **How the candidate will prepare:** during this stage in the interview process, we will get an understanding of the technical depth of your experience and how you would contribute to our engineering culture. We will ask you about your past work and accomplishments in depth, how you worked with others, decisions you made, and what you’d do differently today.

### Code Walkthrough

- **Interviewers:** two members of the team they are interviewing for
- **Length:** 45-minutes (5 minutes of introductions, 30-minute walkthrough, 10 minutes of questions about working at Sourcegraph.)
- **How the candidate will prepare:** For this interview, the candidate will drive a walkthrough of either a personal project or library of their choice. Be ready for them to screen share the library in question via the IDE or editor of choice.
- **What to look for:** We want to find engineers who are:
    - Good communicators.
    - Can tailor the technical depth and scope of a conversation dependent on the audience.
    - Can effectively teach and share their knowledge.
- **During the interview:** You will guide the candidate to areas of the code that seem ripe for discussion. You may ask the candidate to zoom in or out of layers of abstraction (into/out of functions, classes, and packages) in order to help you build a shared understanding of the code under review. You may ask to explain how particular parts of the code under review work. The level of explanation will vary (but will not be a mystery): you may ask how high-level components interact, or you may ask how an individual function works in detail. Try to ask both! You should ask follow-up questions about performance, usage ergonomics, code complexity, and ideas for improvements. You should also ask clarifying questions about how the code under review reacts to certain input or usage conditions. You can ask the candidate to explain potential trade-offs given different hypothetical design constraints (what in the code would need to change).

### Pairing Exercise

- **Interviewers:** two engineers on the team they are interviewing for. All pairing sessions should include a third engineer in the room as an observer. As such, they can stay muted for the bulk of the interview. Having another person in the room provides a more complete picture of the candidate and helps to reduce bias. All candidates applying for the same position should pair on the same exercise with the same people. Important: If the engineer leading the interview has not led a pairing interview with the chosen exercise before, they must do a dry run with the hiring manager first. This is to ensure that any wrinkles are ironed out before we meet with a candidate.
- **Length:** 60-minutes
- **How the candidate will prepare:** We ask candidates to spend an hour pairing with an engineer on the team they are applying to. The pairing exercise is not used for technical evaluation. The assumption is that any candidate who gets to this stage meets the technical requirements for the job in question.
- **What to look for:** At a high level, this is what we are evaluating our candidates for:
    - Clear explanations of ideas and decisions.
    - Frequent communication while pairing.
    - Keeping the other engineer in the loop while driving.
    - Flexibility in considering other ideas and approaches, and in making changes to the code.
    - Ability to break down a problem and decide on an approach as a pair.
    - Healthy responses to feedback.
- **Before the interview:** The engineer leading the pairing exercise should choose a task to work on from [this list](https://docs.google.com/document/d/1CRrR9ujgTesi3ZDVNSRcUo3ZFAAaPBt5nY7enHGkwTg/edit). An ideal exercise should:
    - be easy to explain
    - be language agnostic, so the candidate can use whatever language/tools they are most comfortable with
    - require no specialized knowledge
    - take 30-60 minutes to complete
    - have multiple ways to extend it: more features, add tests, etc.
- **During the interview**: Having ways to extend the exercise is important if you finish the exercise before the interview is over. Finishing the exercise is not a goal; the goal is to pair for as much of the interview as possible since that provides the signal we are looking for. (This implies not finishing the exercise.) For the engineer leading this interview: Pair as if you are working with a colleague, not evaluating a candidate. Work together. Offer help if the candidate gets stuck. It’s totally fine if a candidate doesn’t know something or wants to look something up. In short: if it’s cool for a teammate to do, it’s cool for the candidate to do. Finally, save the last 10 minutes of the interview for any Q&A the candidate might have. (No need to finish up that last task; just stop coding.) For the engineer observing: Pay close attention to the items, we are looking for, listed above. Don’t get sucked into the exercise itself, or offer ideas/solutions/feedback. The observer should be as invisible as possible outside of the initial introductions and the final 10 minutes.

### Pair Coding Skills

- **Interviewers:** two members of the team they are interviewing for
- **Duration:** 60-minutes
- **Details:** You will pair with the candidate to work on an API Client implementation. The goal is to work on the problem together like you would with a fellow engineer. You should use this interview to determine the candidate’s coding ability and technical communication.

### Complex Problem Deep Dive

- **Interviewers:** two members of the team they are interviewing for
- **Duration:** 60-minutes
- **Details:** You will discuss the most complex problem the candidate has solved with code or the most complex codebases they have worked with.

### Frontend live-coding exercise interview

- **Interviewers:** two members of the team they are interviewing for
- **Duration:** 60-minutes
- **Details:** This is a live interview to assess the candidate's approach to Code and the UI/UX. One interviewer will lead the interview and one interviewer will shadow. The exercise currently requires the candidate to have a CodeSandbox account and a Figma account.
- **Before the interview** [Instruction](https://github.com/sourcegraph/interviews/edit/master/engineering/coding/commit-header/README.html)
- Note: The instructions are for both 60min and 90min. In this case it is a 60min interview.
- **What to look for:**
How did the candidate approach the code? Think about CSS, React, error handling, tests. If there was anything they struggled with, did they communicate their intentions well?
How did the candidate approach the UI/UX. Did they generally follow what the design specified? Did they consider loading and error states? Did they consider accessibility?
Follow up questions based on the candidates implementation

### Delivery: Pairing Exercise

- **Interviewers:** one engineer on the Delivery team
- **Length:** 60-minutes
- **Details:** This interview consists of two activities that are designed to understand how the candidate works within a collaborative technical environment. The interviewer will play the role of a customer and provide information to the candidate so they can effectively troubleshoot a problem with an application running in Kubernetes, then collaborate with the candidate to add a new feature to the deployment.
- **What to look for:** At a high level, this is what we are evaluating our candidates for:
    - How the candidate approaches troubleshooting - where do they get stuck, what avenues do they explore?
    - Clear explanations of ideas and decisions.
    - Frequent communication while pairing.
    - Keeping the other engineer in the loop while driving.
    - Healthy responses to feedback.
- **Before the interview:** The engineer leading the pairing exercise should carefully review the full interview instructions [here](https://docs.google.com/document/d/1Gn7oF4N8okjWdUJL_csNAeDpq3IbMSGuu0kvZqA6dC8/edit?usp=sharing) - this is a collaborative interview and will need to provide some information detailed in the prompt. The engineer should also set up a local Kubernetes cluster and deploy the broken manifest from the first activity so they can be prepared to run troubleshooting commands provided by the candidate.

### Assistant - 2024-10-04 13:31:43



### Assistant - 2024-10-04 13:31:43

### Types of Interviews

1. **Architecture Interview**
   - Candidates design a new system from scratch, discussing their approach and problem-solving with interviewers, focusing on resolving ambiguity and making trade-offs in system architecture.

2. **Technical Interview: General**
   - This interview explores the candidate's technical depth and experience, focusing on past projects, decision-making, and how they work with others.

3. **Code Walkthrough**
   - Candidates present and discuss a personal project or library, demonstrating communication skills, the ability to navigate layers of abstraction, and problem-solving in real-time.

4. **Pairing Exercise**
   - A collaborative exercise where candidates work with an engineer on a coding task, emphasizing communication, flexibility, and teamwork rather than technical evaluation.

5. **Pair Coding Skills**
   - Candidates pair with an engineer to implement an API client, with a focus on coding ability and technical communication during the problem-solving process.

6. **Complex Problem Deep Dive**
   - The candidate discusses a complex problem they have solved or a challenging codebase they have worked with, revealing their technical depth and problem-solving approach.

7. **Frontend Live-Coding Exercise**
   - A live coding session focused on front-end development, assessing the candidate's coding approach, UI/UX design considerations, and problem-solving skills, particularly with CSS, React, and accessibility.

8. **Delivery: Pairing Exercise**
   - A collaborative troubleshooting and feature-adding session in a Kubernetes environment, assessing the candidate’s troubleshooting process, communication, and adaptability.

### User - 2024-10-04 13:32:52

Here is another interview document. Do the same for this.

The purpose of this handbook page is to help candidates prepare for each step of the interview. This section of the handbook documents the hiring process for roles on the engineering team.

We know that interviewing can be stressful, so we want to provide you with as much information as possible to help you feel prepared!

What is the day-to-day engineering experience at Sourcegraph?

- We’re often reading code we haven’t written.
- We’re functioning in an asynchronous environment where clear communication is key.
- We need to help our team understand areas where we are the domain expert.

What do we want to be true about these interviews?

- Allow you as the candidate to focus on an area that you are comfortable in.
- Allow a dialogue that simulates a technical discussion between your potential future peers.
- Use these discussions as a proxy for technical aptitude and programming skills.
- Have a time-efficient process for yourself and Sourcegraph.

We want to find engineers who are:

- Team-oriented.
- Good communicators.
- Can tailor the technical depth and scope of a conversation dependent on the audience.
- Can effectively teach and share their knowledge.

For coding interviews, use of coding assistants is both encouraged and expected. Cody preferred!

### Standard Interview Process

- (30m) [Types of interviews & sample questions](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21)
- (30m-60m) [Types of interviews & sample questions](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21)
- (60m) [Types of interviews & sample questions](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21)
- Team Interview
    - (45-60m) Technical Interview (examples below)
    - (45-60m) Technical Interview (examples below)
    - (60m) [Types of interviews & sample questions](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21) with 1 Product Manager + 1 Designer
- (30m) [Types of interviews & sample questions](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21)
- (30m) [Types of interviews & sample questions](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21)
- References check
- Offer

# Types of Technical Interviews

### Hiring Manager Intro

- **Interviewers:** the hiring manager
- **Duration:** 15-minutes.
- **Details:** During this stage in the interview process, the hiring manager will introduce themself, get to know you, and answer any questions. This stage is meant to be informative for both us and the candidate.

### Architecture

- **Interviewers:** two members of the team you are interviewing for
- **Duration:** 60-minutes
- **How to prepare:** Two engineers from the team will work with you by verbally discussing how you would design a new system from scratch. We will work with you in this collaborative session to think about and design the system together, looking for your natural intuition about building systems and problem-solving as we throw various wrenches into the system. The interview consists of open-ended questions, allowing you to describe your mental model of designing a new system from scratch - we want to understand the decisions you are making when designing system architectures. We expect you to ask clarifying questions as the requirements for the system are purposefully ambiguous. We expect you to be designing systems that often need to meet conflicting or ambiguous requirements. For engineers in these roles, a significant part of their journey in Sourcegraph is going to be designing new or improving existing systems to fit these new requirements. Being open-ended allows us to dive into multiple different problem areas, based on your responses, skills, and abilities. It allows a bidirectional conversation, which lets us identify the strengths and weaknesses in the design you propose. For coding interviews, use of coding assistants is both encouraged and expected.

### Technical Screen / Resume Deep Dive

- **Interviewers:** A hiring manager or a member of the team for which you're interviewing
- **Duration:** 30-60 minutes
- **Details:** A Sourcegraph teammate or the hiring manager will ask technical and behavioral based questions about your skills, values, and work history in order to gauge whether they're aligned with the requirements of the role. The goal of the interview is to:
    1. Get an understanding of your technical depth and how you would contribute to and/or collaborate with our engineering team
    2. Take a [deep dive](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21) into your background from past to present with the goal of uncovering the motivation behind your decision making, strengths, weaknesses, and accomplishments in past roles.
    3. Get a high level understanding of how your views and experiences align with [our values](../../../../company-info-and-process/values/index.html).

The interviewer will leave time at the end to answer any questions that you have. This stage is meant to be conversational and informative for both you and us.

### Technical Interview

- **Interviewers:** two members of the engineering department
- **Duration:** 45-minutes.
- **Details:** During this stage in the interview process, we will get an understanding of the technical depth of your experience and how you would contribute to our engineering culture. We will ask you about your past work and accomplishments in depth, how you worked with others, decisions you made, and what you’d do differently today.

### Code Walkthrough

- **Interviewers:** two engineers on the team you are interviewing for
- **Length:** 45-minutes
- **How to prepare:** For this interview, you’ll drive a walkthrough of either a personal project or library of your choice. Be ready to screen share the library in question via your IDE or editor of choice. The following are sample ideas; the most important thing is you choose something that you are comfortable and familiar with. Walkthroughs can be done in any language, we do have a preference if possible that they are close to the domain you’d be working in. If you’re choosing a library, feel free to show us its usage contextually within other projects (these may be your personal projects too) and what problems you’ve solved with it historically.
    - For a full-stack position, you may choose a library that you’ve used heavily, for example [DateJs](https://github.com/datejs/Datejs) or [Redux](https://github.com/reduxjs/redux). With a smaller library like DateJs you can walk us through its usage in other projects, what problems you’ve solved, how you’d approach testing it. With Redux perhaps you want to dive into the internals and compare its technical proposition versus other solutions.
    - For a backend position, you may choose a library that you’ve used heavily, for example [Mux](https://github.com/gorilla/mux) or [Ristretto](https://github.com/dgraph-io/ristretto). As an example, with Mux you could compare what problems it solves or introduces versus the Go standard library. As an example for Ristretto perhaps you’d highlight its usage in other projects and some of the underlying caching mechanisms.
    - With whatever you choose to walk us through, if you’re stuck where to start, choose a test case or how the project/library is initialized. We’ll take it from there!
    - During the interview, we will guide you to areas of the code that seem ripe for discussion. We may ask you to zoom in or out of layers of abstraction (into/out of functions, classes, and packages) in order to help us build a shared understanding of the code under review. You will be asked to explain how particular parts of the code under review work.
    - The level of explanation will vary (but will not be a mystery): we may ask how high-level components interact, or we may ask how an individual function works in detail. We will try to ask both!
    - We will ask follow-up questions about performance, usage ergonomics, code complexity, and ideas for improvements. We’ll also ask clarifying questions about how the code under review reacts to certain input or usage conditions. You will be asked to explain potential trade-offs given different hypothetical design constraints (what in the code would need to change).

### Pairing Exercise

- **Interviewers:** 1-2 engineers on the team you are interviewing for
- **Length:** 60-minutes
- **How to prepare:** We ask candidates to spend an hour pairing with an engineer on the team they are applying to. Please be prepared to lead the pairing in the editor and language of your choice. For coding interviews, use of coding assistants is both encouraged and expected.

### Software Engineer - Cloud Ops Pairing Exercise

- **Interviewers:** two engineers on the team you are interviewing for
- **Length:** 60-minutes
- **How to prepare:** Please read **[this prompt](https://docs.google.com/document/d/1dLxtSlu9nHJMKle1L_9iZXIjrTzARhKiR6oC4Ar5CrQ/edit).**

### Software Engineer - Cloud Ops Exercise Walkthrough & System Design

- **Interviewers:** two engineers on the team you are interviewing for
- **Length:** 45-minutes
- **How to prepare:** During the interview, please be prepared to use the screen-sharing feature on Zoom to share a window with your take-home exercise open. We recommend reviewing [required OS permissions](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0064868) for Zoom client ahead of the interview.

### Coding Skills

- **Interviewers:** two members of the team you are interviewing for
- **Length:** 60-minutes
- **How to prepare:** An engineer from the team will pair with you to work on an API Client implementation. The goal is to work on the problem together like you would with a fellow engineer. We plan to use this interview to determine your coding ability and technical communication. For coding interviews, use of coding assistants is both encouraged and expected. Cody preferred

### Complex Problem Deep Dive

- **Interviewers:** two members of the team you are interviewing for
- **Length:** 60-minutes
- **How to prepare:** We will discuss the the most complex problems you have solved with code, or the most complex codebases you have worked on.

### Frontend live-coding exercise interview

- **Interviewers:** two frontend engineers from the Sourcegraph team
- **Duration:** 60-minutes
- **Details:** This is a live interview to assess your approach to Code and to the UI/UX design. One interviewer will lead the interview and one interviewer will shadow. The exercise will use CodeSandbox and Figma, and will be done in React. If you prefer not to use your accounts we have it set up so you don't have to.
- **Preparation:** Not Mandatory, since we can set up the exercise without it - Create (free) accounts on https://www.figma.com/ and https://codesandbox.io/.

### Release / Tooling Engineer Take-Home Assignment Walkthrough

- **Interviewers:** two engineers from the Sourcegraph team
- **Duration:** 60-minutes
- **Details:** Two engineers will have you walk them through your take-home exercise. Please be prepared to discuss your results and answer any follow up questions that they have.

### Delivery: Pairing Exercise

- **Interviewers:** one engineer on the Delivery team
- **Length:** 60-minutes
- **Details:** This interview consists of two activities that are designed to understand how you work within a collaborative technical environment. They are representative of the types of activities that are found in the day-to-day of the Delivery team.
    
    During the pairing session, we will ask you to troubleshoot an issue a customer reported when they deployed an application to Kubernetes. Next, you will extend the deployment to accommodate a feature request in a collaborative pairing session environment. The deployment manifest used for both scenarios is referenced below.
    
    Expert Kubernetes knowledge is not a requirement! We place focus on your ability to troubleshoot and collaborate with teammates.
    
- **How to prepare:**
This exercise is designed to explore your approach to troubleshooting and does not require any advance preparation. You may wish to set up a test Kubernetes cluster and run the application yourself. This step is not required but can be useful during both stages of the interview. Options for a local cluster include: [kind](https://kind.sigs.k8s.io/), [k3d](https://github.com/rancher/k3d) or [minikube](https://minikube.sigs.k8s.io/docs/start/).
    
    The application used for this exercise is below:
    
    deployment.yaml
    
    ```yaml
    apiVersion: apps/v1kind: Deploymentmetadata:  name: webserverspec:  replicas: 1  selector:    matchLabels:      app: www-server  template:    metadata:      labels:        app: www-server    spec:      containers:        - name: webserver          image: docker.io/library/nginx:alpine          imagePullPolicy: 'IfNotPresent'          ports:            - name: http              containerPort: 80              protocol: TCP          livenessProbe:            httpGet:              path: /              port: http          readinessProbe:            httpGet:              path: /              port: http          resources: {}
    ```
    

## Security Interviews

### Application security walkthrough

- **Interviewers:** two Security Engineers
- **Duration:** 45-minutes
- **How to prepare:** This describes the walkthrough stage of the application security interview
process, which is used instead of a take home exercise.

**The day-to-day experience of an application security engineer**

At Sourcegraph, application security engineers:

- Are often reading code that they haven't written.
- Are functioning in an asynchronous environment where clear communication is key.
- Are assisting other members of Sourcegraph's team in understanding complex
security-related issues, and developing creative solutions to those issues.

**The aims of this interview**

- Allow you as a candidate to focus on an area that you are comfortable in.
- Allows a dialogue that simulates a technical discussion between you and your
future peers.
- Use the discussion as a proxy for assessing your application security skills
- Have a time-efficient process for yourself and Sourcegraph.

**We want to find engineers who are:**

- Good communicators.
- Confident in identifying application security weaknesses that stem from
a variety of sources.
- Creative and pragmatic about finding solutions to these issues.
- Able to advocate for better security practices across the organization.

**The process**

During the interview, you will guide us through a project or library of your
choice.

It is important that you choose a project or a library that you are comfortable
with. You don't have to choose a project with known vulnerabilities – we're more
interested in understanding your thought process and the way you would work your
way through an application during a security assessment. If you aren't sure about
the application you wish to use, the [Sourcegraph](https://github.com/sourcegraph/sourcegraph)
platform might be a good choice!

- Interview length: 45 minutes
    - 5 minutes of introductions
    - 30 minute walkthrough
    - 10 minutes of questions that you have for us about working at Sourcegraph

Be prepared to share your screen and walk us through the code.

For the interview, we will expect you to carry out an application security
assessment of the project's code. We do not expect you to carry out any live
testing against the project. Instead, by examining code, we would like to work
through:

- The purpose of the project and any logic-based security concerns that might
arise
- Technical security concerns, for example those deriving from the OWASP Top 10
- The use of dependencies within the project and how you would assess them
for security issues
- Tooling or processes you would put in place to assess the application on an
ongoing basis

We do not have to assess every part of the application during the call – it is
preferable to focus on a single area of functionality and cover it from a
variety of security perspectives. If there are areas that we are particularly
interested in, we might ask you to dive further into them and assess how
specific aspects of functionality might work.

For any security concerns identified we are also interested in knowing how you
would solve them, both in the immediate case and on an ongoing basis. How would
you automatically catch vulnerabilities which might be introduced in the future?
How would you ensure that developers are aware of the potential risks when they
are working on this piece of code?

### Security Operations Case Study

- **Interviewers:** two Security Engineers
- **Duration:** 45-minutes
- **How to prepare:** The aim of this exercise is to gauge your general, non-AppSec security skills, in areas that a junior security engineer might be exposed to on a regular basis. This case study covers generic phishing attempts and discusses how you would identify and protect against them.

## AI/ML Interviews

### Hiring Manager Screen / ML Breadth

- **Interviewers:** Head of AI
- **Duration:** 60-minutes
- **How to prepare:** During this stage in the interview process, the Hiring Manager will introduce themself, get to know you, share details on the AI team and answer any initial questions you may have. They will then discuss few science questions around end to end ML formulation, modeling, deployment & experimentation to gauge your experience in productionizing ML systems in the industry.

### Technical Background

- **Interviewers:** Beyang Liu, co-founder and CTO
- **Duration:** 45-minutes
- **How to prepare:** During this interview, we will focus on systems you've built and dive into your views on machine learning and its potential. Please come prepared to share your vision for AI/ML at Sourcegraph.

### Technical Deep Dive

- **Interviewers:** two engineers
- **Duration:** 45-minutes
- **How to prepare:** The goal of the technical deep dive interview is to assess both theoretical understanding and practical application skills in machine learning. This interview will focus on ranking specific ML knowledge (e.g. models, loss functions, experimentation) as well as orchestration tools and strategies for developing end to end ML systems in production.

### Pairing Exercise

- **Interviewers:** Beyang Liu, CTO/Co-founder
- **Duration:** 30-minute kick-off session + up to 2 hours to work on your own:
    - The first 15 minutes will be live, where we'll ensure that the dev environment is setup.
    - For the next 15 minutes, as you get started on the project, the interviewer will be actively online to answer any questions that you have via Slack.
    - Then, the expectation is that you finish the project within 2 hours.
- **How to prepare:** Please complete these steps prior to the interview:
    - Create [sourcegraph.com](http://sourcegraph.com/) account and an access token for it, so you can start using Cody in VSCode
    - Have a working VS Code installation on your local machine
    - git clone the Sourcegraph Cody repository: https://github.com/sourcegraph/cody
    - Try to get as far as you can setting up the Cody dev environment: https://github.com/sourcegraph/cody/blob/main/vscode/CONTRIBUTING.md
    - If you get stuck, we will go over it on the meeting
    - During the meeting, you'll get invited by the interviewer to a shared Slack channel in which you can ask questions
- **Details:** In the 15min setup call, we'll make sure your development environment is correctly setup. You can ask questions about it too.
    
    Then we'll ask you to add a hypothetical feature to Cody.
    
    You can ask questions in a shared Slack chat for 15 minutes after your meeting.
    
    When you are finished, please share your final results as a pull request in the Slack channel.
    

### AI Coding Exercise

This exercise is designed to provide us a snapshot of your approach to designing and implementing AI-based systems. It covers a range of the essential skills such as problem selection, design and architecture of AI systems, understanding and selecting appropriate metrics, working with large datasets, and implementing scalable solutions.

Your task is to create a framework for evaluating a critical aspect of Cody's response quality. Cody, which you are free to download and try, assists developers by conversing about their code, generating code, and offering completions. The specific aspect of Cody response quality you focus on is up to you.

Here are the main phases of the exercise:

**Design the Evaluation:** Define the objectives and evaluation rubric, and decide on what factors you're seeking to measure. Choose a dataset, or design one by creatively reusing resources like commit history, the code graph, bug databases, documentation, etc. Finally, decide on effective metrics.

**Implementation:** Create a prototype of the framework that is as close as possible to a production-level solution, demonstrating good coding practices, error handling, and efficiency. We encourage you to use a data parallel framework you're comfortable with, ensuring the solution is scalable to large benchmarks and automated evaluations. If your framework needs to invoke Cody, use a mock or a stub at that point. Example JSON of a Cody response “completion” is included below.

While crafting your solution, consider the following:

- How the system handles large-scale data
- How it ensures reliable and consistent results across different runs
- How the system could be extended for different types of evaluations in the future
- How the system could be integrated with other systems/processes

We will provide you with a modest budget for cloud compute services if needed to exercise your prototype. Please remember not to use equipment, proprietary tools or designs that you can’t share with Sourcegraph.

In order to evaluate all candidates fairly, we request you to limit the time spent on this exercise to a few hours. If there are areas you wish to improve but couldn't due to time constraints, feel free to discuss potential improvements during the follow-up interview.

Finally, you'll walk us through your solution in a 45-minute review session. Begin with a high-level overview of your approach and then delve into specific technical details by screen sharing your code live.

## Leadership Interview Process

### Hiring Manager Intro

- **Interviewers:** Erika Rice Scherpelz, Head of Engineering
- **Duration:** 15-minutes.
- **Details:** During this stage in the interview process, Erika will introduce herself, get to know you, and answer any final questions you may have. She will also follow up on interviews conducted throughout the interview process.

### Interview with Beyang Liu

- **Interviewers:** Beyang Liu, co-founder and CTO
- **Duration:** 60-minutes.
- **Details:** During this stage in the interview process, Beyang will dig into your leadership skills and get an understanding of how you'd run the team.

### Peer Interview

- **Interviewers:** Two Engineering Managers
- **Duration:** 60-minutes.
- **Details:** The purpose of this interview is to assess whether the candidate’s leadership style will align with our expectations and add value to our team.

### Technical Interview

- **Interviewers:** Two engineers on the team/org they would manage
- **Duration:** 45-60-minutes.
- **Details:** The purpose of this interview is to assess whether the candidate has the necessary technical depth to effectively lead a high quality engineering team.

### Cross-functional Team Collaboration

- **Interviewers:** Two cross-functional peers
- **Duration:** 30-60-minutes.
- **Details:** This interview will be focused on domain knowledge, functionally-specific depth, and breadth. The purpose of this interview is to assess whether the candidate will work well with teammates outside of engineering to achieve what is in the best interest of Sourcegraph and our customers.

### Assistant - 2024-10-04 13:33:25



### Assistant - 2024-10-04 13:33:25

### Types of Interviews

1. **Hiring Manager Intro**
   - A 15-minute introductory interview with the hiring manager to get to know the candidate and answer initial questions, providing an informative start to the process.

2. **Architecture Interview**
   - A 60-minute collaborative session with two engineers, focusing on designing a new system from scratch, discussing decisions, ambiguity, and trade-offs in system architecture.

3. **Technical Screen / Resume Deep Dive**
   - A 30-60 minute deep dive into the candidate's technical background, skills, and values to assess alignment with the role and company values.

4. **Technical Interview**
   - A 45-minute interview to assess the candidate’s technical experience, contributions to engineering culture, and past work.

5. **Code Walkthrough**
   - A 45-minute session where the candidate drives a walkthrough of a personal project or library, explaining their coding approach, problem-solving, and code structure.

6. **Pairing Exercise**
   - A 60-minute collaborative coding session where the candidate pairs with an engineer to solve problems, emphasizing communication and teamwork.

7. **Software Engineer - Cloud Ops Pairing Exercise**
   - A 60-minute pairing exercise specific to cloud operations, focusing on troubleshooting and collaboration within Kubernetes environments.

8. **Software Engineer - Cloud Ops Exercise Walkthrough & System Design**
   - A 45-minute walkthrough of a cloud ops take-home exercise, diving into system design and implementation details.

9. **Coding Skills Interview**
   - A 60-minute pairing session to evaluate the candidate’s coding skills and technical communication, specifically around implementing an API client.

10. **Complex Problem Deep Dive**
    - A 60-minute discussion where the candidate explains the most complex problems they have solved or challenging codebases they have worked with.

11. **Frontend Live-Coding Exercise**
    - A 60-minute live coding session using CodeSandbox and Figma to assess frontend coding skills and attention to UI/UX design.

12. **Release / Tooling Engineer Take-Home Assignment Walkthrough**
    - A 60-minute walkthrough of a take-home assignment for a release or tooling engineer role, focusing on the candidate’s problem-solving and solution design.

13. **Delivery: Pairing Exercise**
    - A 60-minute interview focused on troubleshooting and collaborating on a Kubernetes deployment issue, followed by a feature extension, to assess the candidate’s ability to work in a team.

14. **Application Security Walkthrough**
    - A 45-minute session where the candidate walks through a project or library, focusing on identifying security concerns and discussing solutions.

15. **Security Operations Case Study**
    - A 45-minute case study focusing on general security skills, such as identifying and preventing phishing attacks.

16. **AI/ML Hiring Manager Screen / ML Breadth**
    - A 60-minute interview where the head of AI explores the candidate’s breadth of experience in ML system formulation, deployment, and experimentation.

17. **AI/ML Technical Background Interview**
    - A 45-minute discussion with the CTO to explore the candidate’s vision for machine learning and systems they have built.

18. **AI/ML Technical Deep Dive**
    - A 45-minute deep dive into the candidate's specific ML knowledge and experience with end-to-end ML system development.

19. **AI/ML Pairing Exercise**
    - A 30-minute live setup session followed by up to 2 hours of individual work on adding a feature to Cody, Sourcegraph’s AI system, with Slack support during the project.

20. **AI Coding Exercise**
    - A project where the candidate designs and implements a framework to evaluate Cody’s response quality, focusing on designing metrics, handling data, and ensuring scalability.

21. **Leadership Interview - Hiring Manager Intro**
    - A 15-minute interview with the head of engineering to get to know the candidate and follow up on prior interviews.

22. **Leadership Interview with CTO**
    - A 60-minute interview with the CTO to explore the candidate’s leadership approach and how they would run the engineering team.

23. **Peer Interview**
    - A 60-minute interview with two engineering managers to assess the candidate's leadership style and alignment with the team’s expectations.

24. **Leadership Technical Interview**
    - A 45-60 minute interview with engineers from the team to evaluate the candidate’s technical depth and ability to lead a high-quality engineering team.

25. **Cross-functional Team Collaboration Interview**
    - A 30-60 minute interview with cross-functional peers to assess the candidate’s ability to collaborate across teams for the benefit of Sourcegraph and its customers.

### User - 2024-10-04 13:34:46

Consolidate the two lists into one, combining redundant interviews both within and across the lists. 

### Assistant - 2024-10-04 13:35:24

### Consolidated Types of Interviews

1. **Hiring Manager Intro**
   - A 15-minute introductory interview with the hiring manager to get to know the candidate, answer initial questions, and provide an overview of the role and process.

2. **Architecture Interview**
   - A 60-minute collaborative session with two engineers, where the candidate designs a new system from scratch, focusing on ambiguity, trade-offs, and system architecture decisions.

3. **Technical Screen / Resume Deep Dive**
   - A 30-60 minute interview to explore the candidate’s technical background, values, and work history, assessing alignment with the role and company values.

4. **Technical Interview**
   - A 45-60 minute interview to assess the candidate’s technical depth, contributions to engineering culture, past work, and how they collaborate and make decisions.

5. **Code Walkthrough**
   - A 45-minute interview where the candidate presents and walks through a personal project or library, focusing on their approach to code structure, problem-solving, and technical communication.

6. **Pairing Exercise**
   - A 60-minute collaborative coding session where the candidate pairs with an engineer, focusing on teamwork, communication, and problem-solving. For coding interviews, the use of coding assistants is encouraged.

7. **Pair Coding Skills Interview**
   - A 60-minute pairing session to work on an API client implementation, used to assess the candidate’s coding ability and technical communication skills.

8. **Complex Problem Deep Dive**
   - A 60-minute discussion where the candidate explains the most complex problems they have solved or challenging codebases they have worked with.

9. **Frontend Live-Coding Exercise**
   - A 60-minute live coding session using CodeSandbox and Figma (in React) to assess frontend coding skills, attention to UI/UX design, and handling of various design and accessibility concerns.

10. **Delivery: Pairing Exercise**
    - A 60-minute collaborative troubleshooting session in a Kubernetes environment, followed by extending a deployment feature, to evaluate the candidate’s troubleshooting and teamwork skills.

11. **Cloud Ops Pairing Exercise**
    - A 60-minute pairing session specific to cloud operations, focusing on troubleshooting and collaboration within Kubernetes environments.

12. **Cloud Ops Exercise Walkthrough & System Design**
    - A 45-minute walkthrough of a take-home cloud ops exercise, focusing on system design and problem-solving.

13. **Release / Tooling Engineer Take-Home Assignment Walkthrough**
    - A 60-minute interview where the candidate walks through their take-home assignment, discussing the solution and answering follow-up questions.

14. **Application Security Walkthrough**
    - A 45-minute session where the candidate performs an application security assessment on a chosen project, focusing on identifying and addressing security concerns.

15. **Security Operations Case Study**
    - A 45-minute case study discussing general security issues, such as phishing attacks, to gauge non-application-specific security skills.

16. **AI/ML Hiring Manager Screen / ML Breadth**
    - A 60-minute interview with the head of AI, exploring the candidate’s experience with end-to-end ML system formulation, deployment, and experimentation.

17. **AI/ML Technical Background Interview**
    - A 45-minute interview with the CTO, focusing on the candidate’s experience with machine learning systems and their vision for ML at Sourcegraph.

18. **AI/ML Technical Deep Dive**
    - A 45-minute deep dive into the candidate's knowledge of machine learning, including models, orchestration tools, and end-to-end system development.

19. **AI/ML Pairing Exercise**
    - A 30-minute live setup session followed by up to 2 hours of individual work, where the candidate implements a feature for Cody, with Slack support during the project.

20. **AI Coding Exercise**
    - A coding task where the candidate designs a framework to evaluate Cody's response quality, focusing on problem selection, scalability, and metrics for AI systems.

21. **Leadership Interview with CTO**
    - A 60-minute interview with the CTO to assess the candidate’s leadership skills, technical depth, and their approach to leading engineering teams.

22. **Peer Leadership Interview**
    - A 60-minute interview with two engineering managers to evaluate the candidate’s leadership style and fit with the team.

23. **Cross-functional Team Collaboration Interview**
    - A 30-60 minute interview with cross-functional peers, focusing on the candidate’s ability to collaborate across departments for the benefit of the company and its customers.

24. **Leadership Technical Interview**
    - A 45-60 minute technical interview with engineers from the team to assess the candidate’s technical depth and ability to lead a high-quality engineering team.

### User - 2024-10-04 13:37:08

Given the descriptions in the shared docs, write up a description of the following interviews. The descriptions should be appropriate for replacing the existing descriptions, with a focus on being clear, concise, and actionable. 
- Architecture Interview
- Technical Interview
- Complex Problem Deep Dive

### Assistant - 2024-10-04 13:37:23

### Architecture Interview
The Architecture Interview is a 60-minute collaborative session where you will work with two engineers to design a new system from scratch. The goal is to evaluate how you approach system design under ambiguous requirements. You will be asked open-ended questions to discuss your mental model of system architecture, trade-offs you make, and how you resolve conflicting needs. The interview is meant to simulate a technical discussion with future peers, so expect to ask clarifying questions and adjust your design as new constraints are introduced. Coding assistants are encouraged to be used during this interview.

### Technical Interview
The Technical Interview is a 45-60 minute session designed to assess your technical depth and contributions to engineering culture. You will discuss your past work, focusing on technical decisions, problem-solving, and how you collaborate with others. Expect to dive into specific projects, explain the rationale behind your choices, and reflect on what you might do differently today. This interview is an opportunity to demonstrate both your technical expertise and how you approach teamwork within an engineering environment.

### Complex Problem Deep Dive
In the Complex Problem Deep Dive, you will have 60 minutes to discuss the most challenging technical problem you’ve solved or the most complex codebases you've worked with. The focus is on understanding your thought process, the technical obstacles you encountered, and how you approached solving them. You’ll explain your problem-solving strategies, trade-offs made, and lessons learned from the experience. This interview allows us to see how you tackle difficult problems and handle complexity in real-world situations.

### User - 2024-10-04 13:41:33

Add more detail, breaking these down by 
- **Interviewers:** 
- **Duration:** 
- **How the candidate will prepare:** 
- **What to look for:**

### Assistant - 2024-10-04 13:41:58

### Architecture Interview

- **Interviewers:** Two engineers from the team you are interviewing for.
- **Duration:** 60 minutes.
- **How the candidate will prepare:** The candidate should be ready to design a system from scratch. There is no specific preparation required, but the candidate should be comfortable thinking through architecture in real-time, resolving ambiguities, and making trade-offs. Familiarity with system design principles and the ability to handle open-ended scenarios will be helpful.
- **What to look for:** Evaluate the candidate's approach to system design under ambiguous requirements. Look for their ability to ask clarifying questions, think through trade-offs, and handle conflicting requirements. Observe how well they communicate their thought process and collaborate in a peer-like environment. Pay attention to how they react to new constraints and whether they display intuition about scalable, robust solutions. Coding assistants are encouraged, and interviewers should be attentive to how candidates leverage them.

---

### Technical Interview

- **Interviewers:** Two engineers from the engineering team.
- **Duration:** 45-60 minutes.
- **How the candidate will prepare:** The candidate should be ready to discuss their past technical work in detail. This includes being prepared to explain the rationale behind their technical decisions, how they collaborated with others, and how their work contributed to project or product success. The candidate may also be asked to reflect on what they would do differently in hindsight.
- **What to look for:** The interviewers should evaluate the candidate’s depth of technical expertise, especially in areas relevant to the role. Look for strong examples of decision-making, teamwork, and problem-solving in the candidate's prior work. Assess how the candidate reflects on past projects, including what they learned and how they have improved their approaches. Communication skills, the ability to adapt to feedback, and alignment with engineering best practices should also be key considerations.

---

### Complex Problem Deep Dive

- **Interviewers:** Two engineers from the team you are interviewing for.
- **Duration:** 60 minutes.
- **How the candidate will prepare:** The candidate should come prepared to discuss one or more highly complex technical challenges they have worked on. This can include projects with intricate codebases, problems involving significant technical obstacles, or innovative solutions to difficult issues. The candidate should be ready to explain their approach in depth, including their decision-making process and the trade-offs they encountered.
- **What to look for:** Interviewers should focus on understanding the candidate’s approach to solving highly complex problems. Look for their ability to articulate the technical challenges they faced, how they approached solving them, and the strategies they employed to overcome obstacles. Evaluate the candidate's problem-solving skills, including how they handle ambiguity and complexity, and how they balance short-term fixes with long-term solutions. Look for insight into how they manage technical trade-offs and what they learned from the experience. The goal is to assess their ability to navigate and resolve deeply challenging technical issues.

### User - 2024-10-04 13:42:23

Combine the Technical Interview and Complex Problem Deep Drive

### Assistant - 2024-10-04 13:42:37

### Technical Interview & Complex Problem Deep Dive

- **Interviewers:** Two engineers from the team you are interviewing for.
- **Duration:** 60 minutes.
- **How the candidate will prepare:** The candidate should be prepared to discuss their past technical projects in depth, focusing on both general technical experiences and the most complex problems they have encountered. This includes reflecting on technical decisions, collaboration with team members, and the strategies used to tackle difficult challenges. They should be ready to explain how they handled technical trade-offs, solved ambiguous problems, and navigated complex codebases or systems.
- **What to look for:** Interviewers should assess the candidate’s technical expertise, problem-solving approach, and depth of experience with complex systems or challenges. Look for clear examples of how the candidate navigated intricate technical issues, made critical decisions, and worked with others to find solutions. Evaluate their ability to articulate the complexity of the problems they faced, the trade-offs they managed, and the long-term impact of their solutions. This interview also aims to assess how candidates think under pressure, collaborate, and adapt their approach when faced with novel or ambiguous challenges. Communication skills and reflective insights on past work are key indicators of success.

### User - 2024-10-04 13:48:27

Make the "what to look for" a bulleted list and come up with a title that isn't just a conjunction of the previous titles but instead concisely and directly describes the purpose of the interview

### Assistant - 2024-10-04 13:49:02

### Technical Depth and Problem-Solving Interview

- **Interviewers:** Two engineers from the team you are interviewing for.
- **Duration:** 60 minutes.
- **How the candidate will prepare:** The candidate should be prepared to discuss their past technical projects, focusing on both general technical experiences and the most complex problems they’ve encountered. This includes explaining technical decisions, collaboration with team members, and how they addressed difficult challenges. Be ready to dive into specifics about technical trade-offs and solutions in complex or ambiguous scenarios.

- **What to look for:**
   - Ability to articulate the complexity of past technical challenges.
   - Clear examples of navigating and solving intricate technical problems.
   - Decision-making process when balancing trade-offs and constraints.
   - Collaboration skills and how they worked with others to solve challenges.
   - Reflective insights on what they learned and how they would approach problems differently in the future.
   - Communication skills and how they explain complex ideas or technical concepts. 
   - Adaptability and creativity when faced with ambiguity or novel challenges.

### User - 2024-10-04 13:51:07

Make this technical problem solving and combine it with the resume deep dive. 

### Technical Screen / Resume Deep Dive

- **Interviewers:** A hiring manager or a member of the team for which you're interviewing
- **Duration:** 30-60 minutes
- **Details:** A Sourcegraph teammate or the hiring manager will ask technical and behavioral based questions about your skills, values, and work history in order to gauge whether they're aligned with the requirements of the role. The goal of the interview is to:
    1. Get an understanding of your technical depth and how you would contribute to and/or collaborate with our engineering team
    2. Take a [deep dive](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21) into your background from past to present with the goal of uncovering the motivation behind your decision making, strengths, weaknesses, and accomplishments in past roles.
    3. Get a high level understanding of how your views and experiences align with [our values](../../../../company-info-and-process/values/index.html).

The interviewer will leave time at the end to answer any questions that you have. This stage is meant to be conversational and informative for both you and us.

### Assistant - 2024-10-04 13:51:18

### Technical Problem Solving & Resume Deep Dive

- **Interviewers:** A hiring manager or two engineers from the team you are interviewing for.
- **Duration:** 60 minutes.
- **How the candidate will prepare:** The candidate should be ready to discuss their work history, focusing on both technical accomplishments and the most complex problems they have solved. This includes being prepared to explain the decisions they made, the trade-offs they managed, and how they collaborated with others. The candidate should also reflect on their technical growth over time and how their experiences align with the role and company values.

- **What to look for:**
   - Depth of technical expertise in relevant areas.
   - Examples of complex problem-solving and decision-making.
   - Ability to articulate challenges, technical trade-offs, and solutions.
   - Insights into past roles, including strengths, weaknesses, and areas of growth.
   - Clear explanation of how their technical experience and approach would contribute to the team.
   - Alignment with company values, particularly in how they approach teamwork and problem-solving.
   - Communication skills and ability to convey complex ideas clearly and concisely.

### User - 2024-10-04 15:29:01

Suggest some "What to look for" questions for the take home interview described below. It's okay if it has overlap with the other interview types

### Take-home Assignments

- **Interviewers:** 1-2 members of the team the candidate is interviewing for
- **Length:** 24 hours for the assignment, 45 minute walkthrough
- **Details:** The candidate will be given a take-home exercise and 24 hours to complete it. This will be followed by 45 minute walkthrough where the candidate shares their screen and walks the interviewers through their solution. The interviewers will ask questions to assess the candidate’s problem solving approach and the quality of their solution.

Additional notes:
    - The candidate can use the language and tools they are most comfortable with.
    - The use of coding assistants is both encouraged and expected.
    - The candidate can lookup additional information which helps them solve the problem.
    - The candidate should set up the [required OS permissions](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0064868) for Zoom client ahead of the interview.
- **What to look for:**
    -

### Assistant - 2024-10-04 15:29:16

### What to Look For in the Take-home Assignment Walkthrough

- **Understanding of the problem:**
   - Does the candidate demonstrate a clear understanding of the problem requirements?
   - Can they articulate the challenges they faced and how they approached solving them?

- **Approach to problem-solving:**
   - How did the candidate break down the problem into manageable pieces?
   - Did they choose an effective and efficient solution, or discuss why they chose a particular approach over alternatives?
   - How did they handle trade-offs in their solution, such as between performance and simplicity?

- **Technical decision-making:**
   - How did they select the tools, libraries, or frameworks they used?
   - Can they explain why certain technologies or design patterns were chosen and how they fit into the solution?

- **Code quality:**
   - Is the code well-structured, readable, and maintainable?
   - How did the candidate handle testing and error handling in their code?

- **Adaptability:**
   - How did the candidate use external resources (e.g., coding assistants, documentation) to overcome challenges or fill in gaps in knowledge?
   - Are they able to discuss areas of the solution they would improve with more time?

- **Communication skills:**
   - Can the candidate clearly explain their code, decisions, and thought process during the walkthrough?
   - Are they able to respond thoughtfully to feedback or questions about their approach?

- **Flexibility and creativity:**
   - Did the candidate come up with creative solutions to challenging parts of the exercise?
   - Are they open to considering other ways the problem could have been solved during the discussion?

These questions aim to evaluate both the technical quality of the candidate's work and their ability to communicate their approach effectively, as well as their problem-solving skills under a realistic scenario.

### User - 2024-10-04 15:30:42

Flatten this into a list of just the questions and use the minimal number which provides good coverage

### Assistant - 2024-10-04 15:30:50

### What to Look For in the Take-home Assignment Walkthrough

1. Does the candidate demonstrate a clear understanding of the problem and its requirements?
2. How did the candidate approach breaking down and solving the problem?
3. Can the candidate explain their technical decisions and the reasoning behind their tool or technology choices?
4. Is the code well-structured, readable, and maintainable?
5. How did the candidate handle trade-offs between performance, simplicity, or other constraints?
6. How did the candidate use external resources to overcome challenges?
7. Can the candidate clearly explain their code and respond thoughtfully to questions or feedback?
8. Are there areas of the solution the candidate would improve with more time?

### User - 2024-10-04 15:43:17

Review the quality of this set of interviews for assessing the candidate's technical skills. Point out potential gaps as well as which parts are particularly valuable. Note that there are separate interviews dedicated to assessing collaboration and communications skills as well as values fit

### Technical Screen / Resume Deep Dive

- **Interviewers:** A hiring manager or a member of the team for which you're interviewing
- **Duration:** 30-60 minutes
- **Details:** The interviewer will take a [deep dive](https://www.notion.so/Types-of-interviews-sample-questions-f279f080583d49ee9f2c60e30c8cb1f7?pvs=21) into the candidate’s background from past to present with the goal of uncovering the motivation behind decision making, strengths, weaknesses, and accomplishments in past roles. The interviewer will ask questions about the candidate’s work history, focusing both on technical accomplishments and behavioral questions about skills, values, and experience. The interviewer will ask the candidate to reflect on their technical growth over time. The interviewer will ask questions which assess how the candidate’s experience aligns with the role and Sourcegraph’s values. The interviewer will leave time to answer questions that the candidate has. This stage is meant to be conversational and informative for both the candidate and Sourcegraph.
- **What to look for:**
    - Does the candidate explain the decisions they made and the trade-offs they managed?
    - Has the candidate solved complex problems?
    - How did they collaborated with others?
    - Does the candidate demonstrate technical depth in relevant areas?
    - What does the candidate bring to our engineering culture?
    - Has the candidate demonstrated growth and insight into their past, including strengths, weaknesses, and areas of growth?
    - Is the candidate aligned with our values, especially around teamwork and problem-solving?
    - Are they able to communicate complex ideas clearly and concisely?

### Pairing Exercise

- **Interviewers:** 1-2 engineers on the team they are interviewing for
    - Candidates for the same position should pair on the same exercise with the same interviewers.
    - Engineers must do a dry run with the hiring manager or someone experienced with this interview before their first pairing exercise.
- **Length:** 45 minutes
- **Details:** The candidate pairs with an engineer on the team they are applying to. The candidate should be prepared to lead the pairing in the editor and language of their choice. The interviewer will choose an exercise that is:
    - easy to explain
    - language agnostic
    - requires no special knowledge
    - be expanded in multiple ways if there’s additional time (add features, tests, etc.)
    - can be solved within the allotted time, leaving time for introductions and candidate questions
    
    Additional notes
    
    - The interviewer should ask the candidate to stop coding when it’s time for Q&A. Finishing the exercise is not the goal. The goal is to get as much signal as possible.
    - The interviewer should work as a colleague, offering help if the candidate gets stuck.
    - Candidates are encouraged to look things up as they would when programming normally.
    - The candidate can use the language and tools they are most comfortable with.
    - The use of coding assistants is both encouraged and expected.
    - If there are two interviewers, one should be the observer and avoid getting involved in the exercise. They should be as invisible as possible outside of introductions and Q&A.
- **What to look for:**
    - Does the candidate provide clear explanations of their ideas and decisions?
    - Does the candidate maintain frequent communication?
    - Does the candidate keep their partner informed while driving the coding process?
    - Is the candidate flexible in considering alternative ideas and approaches while changing code?
    - Does the candidate at breaking down the problem and collaboratively decide on an approach?
    - How does the candidate approaches troubleshooting - where do they get stuck, what avenues do they explore?
    - Does the candidate respond to feedback in a constructive and professional manner?
    - Did the candidate demonstrate the relevant domain specific skills?
- **Additional resources:**
    - [Question ideas](https://github.com/sourcegraph/interviews/tree/main/engineering/) (internal)
    - [Cloud Ops Pairing Exercise](https://docs.google.com/document/d/1dLxtSlu9nHJMKle1L_9iZXIjrTzARhKiR6oC4Ar5CrQ/edit#heading=h.7o8as8byqwl1) (public)
    - [Release Pairing Interview](https://docs.google.com/document/d/1Gn7oF4N8okjWdUJL_csNAeDpq3IbMSGuu0kvZqA6dC8/edit) (internal)
        - Note that in the Release pairing interview, the interviewer takes on the role of a customer rather than a colleague. The candidate will be asked to troubleshoot an issue a customer reported when they deployed an application to Kubernetes. They will then extend the deployment to accommodate a feature request.
        - **Before the interview:**
            - The interviewer should set up a local Kubernetes cluster and the initial state described in the doc above. The interviewer should be prepared to run the commands provided by the candidate.
            - The candidate may optionally set up a test Kubernetes cluster and run the application themselves. Options for a local cluster include: [kind](https://kind.sigs.k8s.io/), [k3d](https://github.com/rancher/k3d) or [minikube](https://minikube.sigs.k8s.io/docs/start/).
            - 
            
            The application used for this exercise is below:
            
            deployment.yaml
            
            ```yaml
            apiVersion: apps/v1kind: Deploymentmetadata:  name: webserverspec:  replicas: 1  selector:    matchLabels:      app: www-server  template:    metadata:      labels:        app: www-server    spec:      containers:        - name: webserver          image: docker.io/library/nginx:alpine          imagePullPolicy: 'IfNotPresent'          ports:            - name: http              containerPort: 80              protocol: TCP          livenessProbe:            httpGet:              path: /              port: http          readinessProbe:            httpGet:              path: /              port: http          resources: {}
            ```
            
    - [Frontend pairing exercise](https://github.com/sourcegraph/interviews/tree/main/engineering/coding/commit-header) (internal, requires 60 or 90 minutes; needs revision since we no longer use CodeSandbox)

### System Design

- **Interviewers:** 1-2 members of the team the candidate is interviewing for
- **Duration:** 45 minutes
- **Details:** The candidate should be ready to design a system with conflicting or ambiguous requirements from scratch. The interviewer will choose a question appropriate for the target level. ask open-ended questions and work with the candidate collaboratively to design the system. The interviewer will ask clarifying questions to understand the decisions they make when designing system architectures. There is no specific candidate preparation required, but the candidate should be comfortable thinking through architecture in real-time, resolving ambiguities, and making trade-offs. Familiarity with system design principles and the ability to handle open-ended scenarios will be helpful. 

Additional notes:
    - The interviewer should stop digging when it’s time for Q&A. Finishing the exercise is not the goal. The goal is to get as much signal as possible.
    - The interviewer should work as a colleague, offering help if the candidate gets stuck.
    - The candidate can use the language and tools they are most comfortable with.
    - The use of coding assistants is both encouraged and expected.
- **What to look for:**
    - How does the candidate identify and resolve ambiguity?
    - How do they make tradeoffs?
    - How do they communicate their proposal?
    - What is it like to work with them on a problem they haven’t seen before?
    - What is their intuition about solutions that are likely to yield good results?
- **Additional resources:**
    - [Internal Documentation - Backend Systems](https://github.com/sourcegraph/interviews/blob/master/engineering/software-engineer/architecture/backend-systems/backend-systems.md)
    - [Internal Documentation - Source/Repo management](https://github.com/sourcegraph/interviews/blob/master/engineering/software-engineer/architecture/repo-management/README.md)

### Take-home Assignments

- Note: Currently, only the Cloud Ops and Release teams have take-home assignments.
- **Interviewers:** 1-2 members of the team the candidate is interviewing for
- **Length:** 24 hours for the assignment, 45 minute walkthrough
- **Details:** The candidate will be given a take-home exercise and 24 hours to complete it. This will be followed by 45 minute walkthrough where the candidate shares their screen and walks the interviewers through their solution. The interviewers will ask questions to assess the candidate’s problem solving approach and the quality of their solution. They will also ask questions about next steps if the candidate were to continue working on the question. 

Additional notes:
    - The candidate can use the language and tools they are most comfortable with.
    - The use of coding assistants is both encouraged and expected.
    - The candidate can lookup additional information which helps them solve the problem.
    - The candidate should set up the [required OS permissions](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0064868) for Zoom client ahead of the interview.
- **What to look for:**
    - Does the candidate demonstrate a clear understanding of the problem and its requirements?
    - How did the candidate break down and solve the problem? Can they clearly explain their code and answer questions about it?
    - Can the candidate explain their technical decisions and the reasoning behind them?
    - Is the code well-structured, readable, maintainable, and tested?
    - How did the candidate handle trade-offs between performance, simplicity, or other constraints?
    - Does the candidate have an understanding of where they would improve things with more time?

### Assistant - 2024-10-04 15:44:07

### Review of Technical Interview Set

#### Strengths:
1. **Comprehensive Assessment of Technical Skills:**
   - The combination of **Take-home Assignments**, **Pairing Exercises**, **System Design**, and the **Technical Screen/Resume Deep Dive** covers a broad range of technical skills, ensuring that candidates demonstrate not only their coding ability but also their architecture and problem-solving skills in diverse scenarios.
   
2. **Flexibility and Realism:**
   - Allowing candidates to use their preferred tools and languages, and encouraging the use of coding assistants, ensures that the interview closely mimics real-world work environments. This provides a realistic view of how candidates perform under conditions similar to their day-to-day work.

3. **Problem-Solving Focus:**
   - The **Take-home Assignments** and **Pairing Exercises** emphasize problem-solving under time constraints, providing insight into how candidates handle practical challenges, adapt to unfamiliar problems, and use external resources to enhance their solutions.

4. **System Design Emphasis:**
   - The **System Design** interview focuses on a candidate’s ability to tackle high-level architectural problems, addressing ambiguity and trade-offs, which are critical skills for mid- to senior-level engineering roles. This allows interviewers to assess how candidates approach open-ended problems and make strategic decisions.

#### Potential Gaps:

1. **Limited Coverage of Deep Technical Proficiency:**
   - While **System Design** and **Pairing Exercises** test high-level design and coding skills, there may be a gap in assessing deep technical expertise in areas such as algorithms, data structures, or advanced optimization techniques. While these may not be critical for every role, they are essential for candidates applying for specialized or highly technical roles. 
   
   - **Suggestion:** Incorporate a dedicated technical deep dive into specific areas (e.g., algorithms, performance optimization) for roles requiring deep technical knowledge.

2. **Overlapping Focus:**
   - There is some redundancy between the **Technical Screen/Resume Deep Dive** and the **Take-home Assignments/Walkthroughs**, especially regarding how candidates break down problems, explain their solutions, and reflect on trade-offs. While both components are valuable, they cover similar territory in slightly different formats.
   
   - **Suggestion:** Sharpen the focus of each interview. For example, emphasize strategic thinking and architectural insights in the **System Design**, while focusing on hands-on coding and implementation in the **Take-home Assignment**.

3. **Incomplete Coverage of Edge Cases and Code Robustness:**
   - The **Pairing Exercise** and **Take-home Assignment** don't explicitly address how candidates handle edge cases, testing, and error handling, which are critical for writing production-level code.
   
   - **Suggestion:** Include questions during the **Pairing Exercise** or **Take-home Walkthrough** that probe how candidates anticipate and handle edge cases, performance bottlenecks, and testing strategies to ensure robustness and scalability.

4. **Limited Real-Time Problem Solving:**
   - The **Take-home Assignments** allow candidates to solve problems on their own time, which is beneficial for giving them space to demonstrate their best work. However, this might mask how they handle pressure and real-time problem-solving.
   
   - **Suggestion:** Balance the take-home exercises with live coding challenges or real-time problem-solving scenarios to assess how candidates perform under time constraints and adapt when things don’t go according to plan.

#### Particularly Valuable Aspects:

1. **System Design Interview:**
   - The **System Design** interview is critical for evaluating a candidate’s ability to tackle complex, high-level architecture challenges. This is especially important for senior engineers or those working on large-scale systems where trade-offs, ambiguity, and strategic decision-making are key.

2. **Take-home Assignments:**
   - The **Take-home Assignment** gives candidates the opportunity to demonstrate their skills in a more natural setting. This can provide deeper insights into how they work independently, make technical decisions, and produce clean, maintainable code over time, which is often more revealing than short live coding exercises.

3. **Pairing Exercise:**
   - The **Pairing Exercise** provides a collaborative setting where candidates’ coding ability, communication, and troubleshooting skills can be observed in real time. It offers a good balance between technical evaluation and assessing how well the candidate can work with a team.

### Conclusion:

This set of interviews does a good job of covering technical skills at both the high and practical levels, while maintaining flexibility and realism. However, there are opportunities to fill gaps in deep technical assessments, handling of edge cases, and testing real-time problem-solving under pressure. Ensuring that each component has a distinct and focused objective will make the overall process more robust while minimizing overlap.

