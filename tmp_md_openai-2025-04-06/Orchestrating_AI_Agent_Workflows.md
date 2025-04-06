# Orchestrating AI Agent Workflows

Created: 2025-01-10 17:09:33
Last Updated: 2025-01-10 17:09:52

### User - 2025-01-10 17:09:33

There are lots of definitions of what agent means with respect to AI. One useful definition is the one from anthropic. However, the definition strongly distinguishes egenic workflows where non-llm code is coordinating work which involves steps that have an llm from true authentic workflows which are more open-ended and call out to tools and context sources as needed. Whether or not that distinction proves to be useful in the long run, Bay point to a key aspect of what makes useful llm-based agents, as opposed to just doing prompt engineering with multiple rounds of back and forth. Forth. The key thing is that we let boring non-generative code do the boring non-generative stuff and we say the llm functionality for where the generative capabilities bring some concrete value. We don't actually need llms to solve problems like how many ours are in strawberry or how to do basic math. What we need is to be able to orchestrate plain old code with which can do these things really well generative capabilities that can do more ambiguous things like write code, edit files, compose a poem, or answer your help question. 

Given that prelude, compose a piece which explores this idea further. This will be posted on the blog of a developer tools company creating AI coding assistance and AI agents and the target audience will be both developers and potential customers. But the overall tone should be informative and exploratory not salesy. The piece should not explicitly reference flux style systems thinking, but should have these ideas underlying it's overall tone and conclusions.

### Tool (myfiles_browser) - 2025-01-10 17:09:50

*[tether_browsing_display content]*

### Tool (myfiles_browser) - 2025-01-10 17:09:50

All the files uploaded by the user have been fully loaded. Searching won't provide additional information.

### Assistant - 2025-01-10 17:09:50

---

### The Art of Orchestration: Making AI Agents Practical and Powerful  

The rise of AI agents has sparked both fascination and debate. At their core, these agents represent a new paradigm for software: programs capable of open-ended reasoning, drawing upon the strengths of generative AI while integrating seamlessly with more traditional, deterministic systems. But to create truly useful agents, developers must strike a careful balance between what is generative and what is procedural—between what AI is uniquely good at and what traditional software handles best.  

### What Makes an AI Agent Useful?  

A useful AI agent isn’t just about embedding a large language model (LLM) into your workflow. The real value lies in orchestrating workflows where the generative capabilities of LLMs complement existing, non-generative systems. The distinction here is crucial:  

1. **Egenic Workflows**: In these, non-LLM code takes the lead, coordinating and managing tasks while occasionally calling on LLMs for specific operations. For example, parsing input data might involve standard code, but generating a human-readable summary might be delegated to an LLM.  

2. **Authentic Workflows**: These workflows are more open-ended, allowing the agent to dynamically interact with tools, APIs, and data sources as needed. Instead of rigidly defined steps, the agent makes decisions in real-time about how to approach a problem.  

Both approaches have their place. But what sets AI agents apart from traditional applications—or even multi-round prompt engineering—is their ability to combine deterministic code and generative reasoning into a cohesive, productive system.  

### The Right Tools for the Right Tasks  

A common misstep in building AI agents is over-reliance on LLMs. While these models are incredibly powerful, they’re not always the best tool for the job. Tasks like basic arithmetic, parsing structured data, or performing CRUD operations are best left to procedural code. Such tasks benefit from the precision, reliability, and efficiency of deterministic algorithms.  

On the other hand, LLMs excel in areas that demand ambiguity handling, creative problem-solving, or human-like reasoning. Writing code, composing text, summarizing content, or answering open-ended questions are where generative AI shines. The challenge—and opportunity—lies in combining these strengths effectively.  

### Principles for Building Better AI Agents  

To design agents that are both practical and powerful, developers should consider the following principles:  

1. **Orchestrate, Don’t Overcomplicate**  
   The key to a successful agent is orchestration—using traditional code to handle structured, deterministic tasks and reserving LLM capabilities for situations where generative reasoning adds tangible value.  

   For example, in a coding assistant, non-LLM components might handle tasks like project file parsing or dependency resolution, while the LLM takes on tasks like suggesting implementation strategies or debugging logic in ambiguous scenarios.  

2. **Context is King**  
   A good agent doesn’t just generate; it understands the context of the problem it’s solving. By integrating external tools, APIs, and databases, an agent can extend its capabilities far beyond what the LLM alone can provide. For instance, an agent that integrates with Git can provide version-aware code suggestions rather than generic advice.  

3. **Iterate on Value**  
   When deciding what an agent should do, focus on areas where generative capabilities add measurable value. Avoid the temptation to force LLMs into roles they’re not suited for, such as solving deterministic problems or enforcing strict rules. Instead, prioritize workflows that benefit from creative or adaptive reasoning.  

4. **Keep the Feedback Loop Open**  
   Building an AI agent isn’t a one-and-done process. Deploy agents in real-world scenarios, gather feedback, and refine their orchestration and capabilities. Iteration is key to aligning the agent’s behavior with user needs.  

### Why Orchestration Matters  

At its heart, an AI agent is a symphony of components, each playing its part in harmony. LLMs contribute creativity and reasoning, while traditional software ensures reliability and precision. By designing systems that thoughtfully balance these strengths, developers can create agents that don’t just impress—they deliver real value to users.  

In the end, the future of AI agents isn’t about making LLMs do everything. It’s about making them do the right things, and orchestrating the rest.  

--- 



