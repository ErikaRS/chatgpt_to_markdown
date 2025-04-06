# Context & Code Differentiators

Created: 2023-05-12 09:49:26
Last Updated: 2023-05-12 10:40:50

### User - 2023-05-12 09:49:26

I am writing a whitepaper about the strategic importance of context and a structured code graph for enterprise decision makers. The goal should be to provide a well founded case for why our offering is differentiated from other offerings. Below I include some initial notes. Generate an outline.

Some notes from Steve
I need a whitepaper. If you team could help build one that talks about our Context strategy and how it differentiates us, it would be amazingly useful at this juncture.
It’s for Sales and GTM, primarily. Whitepaper audience is the decision-makers at big enterprise companies. They tend to be interested in legal and security, so things like guardrails are especially interesting. Plugins, too.
Many of the decision-makers are also legal (if that’s relevant to you yet), and the rest are all Eng directors/VPs/Principals who have lots of questions about embeddings and context windows and such.
The goal is to convey clearly and convincingly what our approach and roadmap look like here, to the best of our ability, how we plan to scale up, what deployment offerings we’re working on, and mostly importantly, what our defensible differentiators are.

Some initial notes
Importance of context in general
Importance of the right context slicing: embeddings space works best when it encodes meaning and code has semantic structure
Importance of code structure for context beyond embeddings: finding dependencies and other relationships. Extracting the knowledge the compiler knows that isn't in the language semantics.
Non code context: even large companies struggle with searching their own knowledge base because it doesn't have the rich structure of linking of public data.
Non code context: tools, logs, going beyond static to dynamic
Smart GPT and the importance of promoting? Promoting vs context?


### Assistant - 2023-05-12 09:50:32

Outline:

I. Introduction
   A. Purpose and audience of the paper
   B. Brief overview of the whitepaper content

II. The Importance of Context in Enterprise Decision Making
   A. General importance of context
   B. Context slicing and its significance
   C. Role of context in encoding meaning and semantic structure

III. The Significance of Code Structure for Context
   A. The value of extracting knowledge from compiler
   B. Importance of finding dependencies and other relationships
   C. The challenge and solutions of encoding language semantics 

IV. The Role of Non-Code Context in Enterprise Operations
   A. The struggle of large companies with searching their own knowledge base
   B. The necessity of a rich structure of linking for public data
   C. Use of tools and logs to enhance non-code context
   D. The need to go beyond static to dynamic 

V. The Intersection of Smart GPT and Context
   A. Overview of Smart GPT
   B. Promoting vs context in Smart GPT
   C. How Smart GPT can enhance decision-making

VI. Our Unique Approach and Roadmap
   A. Overview of our context strategy
   B. Our approach to code structure and context
   C. Our deployment offerings and scaling plans

VII. Our Defensible Differentiators
   A. Explanation of our unique selling points
   B. The importance of guardrails and plugins
   C. How our offerings stand out from other market players
   D. Addressing potential questions from decision makers

VIII. Conclusion
   A. Recap of the strategic importance of context and structured code graph
   B. Final appeal to enterprise decision makers

IX. References
   A. Sources and citations

This outline can provide a structured flow to the whitepaper, beginning with an overview of the importance of context in enterprise decision-making, moving onto the significance of code structure, the role of non-code context, and the intersection of Smart GPT and context. It will then elaborate on our unique approach, our differentiators, and wrap up with a strong conclusion to make a compelling case for our offering.

### User - 2023-05-12 10:40:50

You are a technical decision maker at a large enterprise evaluating a coding assistant offering. This is an expensive offering and the competition in this space is fierce. The section below is meant to convince you that how context is chosen is a critical differentiator for a coding assistant. It is not meant to convince you that this company's context selection is the best, just that context can be a differentiator. What about this write up is convincing? Where is it lacking?

The writeup:

The value of context 
When assistive systems like Sourcegraph’s Cody use LLMs, they generally provide three broad pieces of information to the LLM in the prompt:
Preamble 
User input
Context

The preamble defines the task to be done or the general purpose of the query. Much of the emerging field of prompt engineering is about defining effective prompt preambles. (See this video on SmartGPT for an example of how this can get sophisticated). For example, a preamble may tell the LLM how to write an effective unit test.

User input is the information provided by the user that guides the specific output. For example, write a unit test for this code. 

Connecting these two is context. LLMs are good at answering questions about the data they are trained on. This generally does not include the code, documentation, tool output, etc., of a particular enterprise, and even if it did, with today’s models that information would quickly get stale. Providing context in the LLM query gives the LLM access to the most up to date, relevant information to provide a relevant answer to the query. In Cheating is All You Need, Sourcegraph’s Head of Engineering Steve Yegge compares context to the cheat sheet that students are sometimes allowed to bring to an exam. 

The quality of the provided context is critical. Even with increasing context window sizes, providing the right context is important. For one, with Enterprise code bases continuing to grow, even huge context windows are not enough to send anything. Even when sending everything is feasible, sending larger amounts of context increases query cost as well as data egress. The costs of not being selective can add up.

As a result of these factors, effective context selection will continue to be an important part of interacting with LLMs. And while the eventual likelihood of Enterprise ready, custom trained, quickly updated LLMs will change the role of context, the same techniques that go into generating good context will inform training those models of the future.

### Assistant - 2023-05-12 10:41:42

This write-up does a commendable job in emphasizing the importance of context in Large Language Models (LLMs), particularly in the field of code assistance. It successfully delineates the three broad pieces of information provided to LLMs and elaborates on how context connects the task and user input. It also underscores the challenges of increasing context window sizes and the cost implications of not being selective. The analogy of context to a cheat sheet is apt, making the concept easily relatable.

However, the write-up could be improved in a few areas:

1. **Specific examples**: While the text does a good job of explaining the role of context, it could be more convincing with specific examples of how choosing the right or wrong context can affect the outcome. Use cases or case studies would provide a clearer, more tangible understanding of the significance of context in practical applications.

2. **Technical Details**: As a technical decision-maker, I would appreciate more depth on how context selection works technically. This includes details on the algorithms or methodologies used for context selection, how they have evolved, and the limitations they currently face.

3. **Comparison with competitors**: Although the goal is not to highlight the company's superiority, it would be helpful to understand how different approaches to context selection might vary across the industry. This could help decision-makers see why context selection can indeed be a critical differentiator.

4. **Future implications**: The write-up mentions that the role of context will change with the emergence of Enterprise-ready, custom-trained, quickly updated LLMs. However, it doesn't elaborate on this. An explanation of how these future models might interact with context and how the techniques used today could inform future model training would be beneficial.

5. **Mitigation of Risks**: The write-up could address potential risks or drawbacks of context selection, and how these can be mitigated. This would provide a more balanced view and demonstrate that the company is aware of potential challenges and is proactively addressing them.

