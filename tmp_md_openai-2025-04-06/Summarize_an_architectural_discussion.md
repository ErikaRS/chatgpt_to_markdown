# Summarize an architectural discussion

Created: 2024-02-20 19:15:09
Last Updated: 2024-02-20 20:18:58

### User - 2024-02-20 19:15:09

Summarize the key points of this slack conversation. Utilize a design doc / RFC format with at least the following sections: 
Goal / Problem to solve
Constraints
Potential solutions

The slack conversation:


Thread
discuss-product


Daniel Marques
  7 days ago
Given our “new” direction of a single product and that by the end of the year we should be selling just one package, I wonder what that means for PLG.
Because we made a conscious decision of only making Cody the “plg product”.
Should that change?
Does it make sense to be a “single product company” but only offer part of it on a PLG experience?
I’m asking because the roadmap for PLG is to still focus on a Cody only path, and I wonder it that still makes sense.
cc: 
@kevin.chen
 
@csells
:eyes:
1





27 replies


csells
  7 days ago
that's one of many questions we're going to have to answer, Daniel
:high-five:
1



David Veszelovszki
  7 days ago
The last answer I heard to this question (I think it was two days ago) is that we intend the PLG experience to be Cody only.
If that answer is not really that definite, then it helps us (@plg-team) a lot to know more about the possibilities sooner than later because it affects our architectural decisions that are possible to change now but a lot more difficult to change later.
Context: we’ve built SSC (Self-Serve Cody) as a new service (temporarily coupled with SAMS), but if we expect to share a lot more functionality with the main product, this is still a reasonable point for us to merge it back to the monorepo and allow for deeper interactions with the main product. (Important note: this doesn’t mean making SSC rely on dotcom! Dotcom lives in the monorepo, but it’s a deployment of Sourcegraph that we don’t intend to rely on in any case. SSC would be a separate deployment even if it lived in the monorepo.)


Daniel Marques
  7 days ago
sooner than later because it affects our architectural decisions
Exactly. I know that Quinn mentioned that this should not represent an over-night change and should be taken iteratively but knowing the destination helps.
But if destination is not set yet, maybe it is on us Product + PLG to define where we want to go.
:this:
1
:plus1:
1



csells
  7 days ago
I encourage you to think about what it would mean for us to push Search functionality into our PLG product. Is there enough value there for customers to be worth the eng effort? What about the value of multi-repo context for PLG customers? Does that have enough value? Do we need the same architecture to implement both of these features for PLG customers? Does that provide enough value to make it worth the eng effort?
:this:
1



Connor O'Brien
  7 days ago
100% this 
@csells
 Let's not get caught up in what the products are or what it should be (knowing the destination). Instead, think about how we can bring code graph context into cody more. (edited) 
:plus1:
3



Rafal Gajdulewicz
  7 days ago
Not a certified :approved_stamp: Product opinion:
The way I understand this direction is that as we evolve Cody we will naturally need to use some of the features that are currently implemented in the “Code Search+Code Nav” part of the product.
As an example, if we start building Cody Web (or other “Cody outside of your IDE” features, like Cody in your PRs), we will want to make it reference your private code (ex. the code you used with Cody extension), so we will need a way to store it / process it, so (for optimal UX) we will want to show you what exact files were used by Cody, and at this point we will need a “mini-Code Search” inside of Cody PLG.
Now, a certified Eng opinion: I think of SSC as a “way for people to pay for Sourcegraph products (now Cody) and use those products as a team (coming soon)“, and because of that, I think we won’t need to “merge SSC with the rest of core product living in the monorepo” - SSC will likely not be implementing the new Cody features itself, but other features will rely on SSC to build Free/Pro or Single/Multi-user features. Note that this doesn’t require SSC to be coupled with the rest of the product, but (subjectively) it needs to expose an API / set of abstractions (user/team/subscription tier) that can be used to enable other features. (edited) 
:plus1:
2



csells
  7 days ago
thanks, 
@Rafal Gajdulewicz
. for my own education, can you share a doc that describes the SSC architecture today?









FYI, I captured this in the desired architecture scratchpad

Also send to discuss-product











### User - 2024-02-20 19:16:55

Now create a list of potential solutions focused on the different architectures that might be used

### User - 2024-02-20 19:20:25

What does the original slack thread tell you about the current architecture and the challenges of search for PLG?

### Assistant - 2024-02-20 19:21:02

The Slack conversation provides insight into the current architectural considerations and challenges related to integrating search functionality into the Product-Led Growth (PLG) product, specifically focusing on Cody. Here are the key points regarding the current architecture and the challenges of implementing search for PLG:

### Current Architecture
- **Self-Serve Cody (SSC)**: A new service that has been developed as temporarily coupled with SAMS (a service or system not further explained in the conversation but mentioned in the context of architectural decisions).
- **Monorepo Consideration**: The architecture currently considers whether to keep SSC as a separate service or merge it back into the monorepo to allow for deeper interactions with the main product. The main product and other services, like dotcom (a deployment of Sourcegraph), exist within this monorepo.
- **Separation from Dotcom**: Regardless of the decision to merge SSC into the monorepo, SSC is intended to be a separate deployment that does not rely on dotcom.

### Challenges
- **Decision on PLG Direction**: There's uncertainty about whether to expand the PLG experience beyond Cody, which affects architectural decisions, especially those that can be more easily made now than later.
- **Integration with Main Product Features**: The evolution of Cody might necessitate the use of features currently part of the "Code Search+Code Nav" segment of the product. This integration poses architectural challenges, especially in providing a seamless user experience (UX) that might require a "mini-Code Search" within Cody PLG.
- **Value Versus Effort**: There's a need to assess the value that additional functionalities (like search and multi-repo context) would bring to PLG customers against the engineering effort required to implement these features.
- **Architectural Flexibility**: The architecture must remain flexible to accommodate the potential need for Cody to interact more closely with other parts of the main product, without necessitating a full merge of SSC with the core product in the monorepo. The need for a well-defined API or set of abstractions to enable feature expansion without direct coupling is highlighted.

In summary, the Slack thread reveals a situation where the company is grappling with how best to evolve its product architecture to support its PLG strategy, specifically around integrating or expanding Cody's capabilities. The challenges revolve around making strategic decisions on the product direction, ensuring architectural flexibility, and balancing the value of new features against the complexity and effort required to implement them.

