# Sourcegraph Prototypes Decision.

Created: 2023-03-28 16:39:56
Last Updated: 2023-03-28 16:40:30

### User - 2023-03-28 16:39:56

The goal of this meeting was to decide what prototypes to build. Summarize these notes:
Day 2 debrief notes
Things we can start working on in Q2 but not necessarily completed in Q2 (b/c we want ambitious ideas that reimagine Sourcegraph)
Re-imaging or iterations on current web app UI
JTBD relates to pluggability
Quinn: likes that it shows what it could do but you can still ask it things in a more open ended way
Could be panelized add-on / Cody improvements
Re: Kelli’s: Quinn: gets this. When you click on something, it’s really valuable to show all the stuff that Sourcegraph knows. But we don’t want more than 3% of users to get the first really detailed experience.
 Re: Alex’s: Quinn: Information is really important to have. Likes the idea of entry point that’s the problem to have. It feels like we’re dumping a ton of information. We should show you only what matters. Quinn: Really likes the element of this that makes it easy to take action. Fits well with things like batch changes. Rob: This could be a good area for structured plugins. Quinn: One concern about anchoring too much on a section of code is that some valuable information may be related to broader context like the service. Not everything ties to the repo file hierarhcy.
Re-imagining workflows
Quinn: This seems so cool. Let’s have an AI that monitors even more places like Twitter and Discord to detect issues. This is so much closer to the holy grail of what we want to get to. It would be interesting to take some of the issues we have now and see what you need to paste into GPT-4 to get the right solution. Then we can work backwards from there to automate. 
Quinn: Has way more technical risk than #1 but ultimately this is where we want to get
Making Sourcegraph easier to administer
Quinn: This is so cool. It’s like a whole new product that tries to help users work around errors. 
Rob: We can trial this internally by giving it to customer support people.
Beyang: Can we have cody help configure precise code intelligence? It’s so hard today.
Quinn: This seems like such an obvious win.
The feed. Notifications.
Beyang: It’s awesome. The feed could be really useful. It could help you understand what has changed. It’s so difficult to stay on top of changes. Sourcegraph code intelligence can figure out what you should care about.
Ryan: This is interesting b/c it moves to Cody being moved in a more proactive way. “You didn’t write tests for this.”
Ryan: We still need principles like “the human is in control”. In this case, that’s the PR process.
Rob: Also, an action button to enable it. 
Quinn: The last idea loops back to the first idea. In the first idea, you should focus on what’s relevant.
Where should we spend our attention tomorrow?
Beyang: Provide the scaffolding. Text based view with interactive widgets and the feed. Then think about the functionality in there. What is the content that is triggered? Where does it lead? The first sketch becomes the skeleton of the app. Then we think about how to get this into that scaffolding. What will really make the difference is the functionality within this skeleton. E.g., how do we integrate batch changes into this?
Rob/Erika: Overall, we’ll be more focused on the high level flow to validate what to invest in more.
Beyang: Specific moments: Wants to see one path you can take through this to get to a “wow” moment. Doesn’t necessarily need to be batch changes. It should be something that allows you to work 10x faster.
Quinn: Wants us to spend time on the first. Make the example of things people can do really relevant using Geoffrey’s idea of the speed.  Dig more deeply into the experience. E.g., someone fixes one things and then we proactively prompt them to make the same change to the 7 other repos where it should be made. 
Rob: Content should be super accurate and relevant to a particular person / use case. 
Quinn: We want to enable the user to probe the limits of what cody can do.
Quinn: On the error summaries and auto configuration: We should just do this! No need to prototype.
Re: Taylor’s: Quinn: The risk is in the technical implementation, not the UI. There isn’t really a UI. It’s the holy grail, but no one’s going to believe it right now. Feedback will be, “That’s great if it works.” We need to work up to it and prove it.  Let’s prototype this one if we’re choosing enough.
Re: 2nd one: Quinn: We do need to show all of the stuff that we know in some view, a la the debug or windows registry view. How much should we try to solve in the middle where we show a lot but not everything? It seems like we need to start with showing everything somewhere. If we explore this, the prompt is that people will be using this to debug why the AI is doing the wrong thing.
Re 2nd one: Beyang: Code should be aware of what you’re trying to do with the context of the current moment. “Clippy style” suggesting an action with high confidence. 
Re: 2nd one: Rob: This feels like a lot of the “fill in the gaps” exploration that we were discussing yesterday. 
Re: 2nd one: Beyang: Would love to see an end-to-end workflow that touching all of the key points. 
Beyang: Should have real prompts, not squiggly text. Text is the linchpin 
Re: 2nd one: Rob: The major one on this one is that we have to think end-to-end starting with this file moment
Quinn: Still wants to get all of the information we know about code dumped somewhere

### Assistant - 2023-03-28 16:40:10

The team discussed potential prototypes to work on in Q2 to reimagine Sourcegraph. The first idea focused on reimagining the current web app UI with iterations that relate to pluggability, such as panelized add-on and Cody improvements. The team also discussed reimagining workflows and developing an AI that monitors more platforms, like Twitter and Discord, to detect issues. They also talked about making Sourcegraph easier to administer by creating a new product that helps users work around errors. Lastly, they discussed creating a feed with notifications that can help users stay on top of changes and integrate batch changes into the workflow. The team decided to focus on creating a text-based view with interactive widgets and the feed and to think about the functionality that triggers the content and where it leads. They aim to create a prototype that enables users to work 10x faster while being super accurate and relevant to the user's specific needs. The team also discussed showing all the stuff Sourcegraph knows, and they aim to develop an end-to-end workflow that touches all of the key points.

### User - 2023-03-28 16:40:30

List each prototype idea separately

### Assistant - 2023-03-28 16:41:01

1. Re-imaging or iterations on current web app UI with a focus on Job-to-be-done (JTBD) relating to pluggability. The idea is to create a panelized add-on with Cody improvements that shows what Sourcegraph can do but still allows users to ask questions in a more open-ended way. The concern is that too much information can overwhelm users, so only relevant information should be shown. This idea could also be a good area for structured plugins.

2. Re-imagining workflows by using AI to monitor more places like Twitter and Discord to detect issues. The goal is to automate issue detection and resolution by using GPT-4 to generate solutions to problems. While this idea has more technical risk than the first idea, it is closer to the ultimate goal of creating a more proactive and automated Sourcegraph.

3. Making Sourcegraph easier to administer by creating a new product that helps users work around errors. This idea could be trialed internally by giving it to customer support people. Additionally, Cody could be used to help configure precise code intelligence, which is currently difficult to do.

4. Creating a feed with notifications that helps users stay on top of changes. Sourcegraph code intelligence can figure out what users should care about, and the feed could be used to proactively prompt users to make changes. The focus should be on what is relevant to users, and users should still be in control of the PR process.

5. A prototype idea related to Taylor's proposal, which has more technical risk in the implementation rather than the UI. The idea is to create a prototype to show that it works, but feedback may be skeptical until it is proven. 

6. The second idea related to re-imagining the web app UI involves creating a view that shows everything Sourcegraph knows. The challenge is to strike a balance between showing too much and not enough information. The prototype should aim to suggest an action with high confidence and be aware of the context of the current moment. An end-to-end workflow that touches all key points could be useful in exploring this idea further.

