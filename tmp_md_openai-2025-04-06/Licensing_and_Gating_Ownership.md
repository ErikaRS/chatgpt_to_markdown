# Licensing and Gating Ownership

Created: 2023-11-02 14:37:53
Last Updated: 2023-11-02 14:42:21

### User - 2023-11-02 14:37:53

Please suggest ways to make this more clear and concise without cutting out any of the information:

Some thought, both philosophical and pragmatic. 

Philosophically, Source should own Enterprise licensing and gating across all of our Products. Longer term, a Licensing and Gating (and maybe Billing) team should probably own Enterprise and non-enterprise licensing and gating. Why? Because even if there are separate implementations, the domain knowledge around licensing, gating, and billing would be shared. Plus, it would make it easier to make the user experience feel consistent. 

But for now, I want to focus on the pragmatic perspective. I think that from a pragmatic perspective, the Source team owns licensing and gating (L&G) that is controlled by a Sourcegraph instance (a.k.a. Code Search Enterprise in the diagram from the doc above). 

So the key pragmatic question for me is the same one @Erik Seliger raised: where will Cody Enterprise L&G be implemented?

As Erik notes, we shouldn't make Cody-only Enterprise customers incur the cost of running a Sourcegraph instance they aren't using. This implies that we'll need a separate service to enforce Cody L&G (the Cody Enterprise doc in the diagram Erik linked). 

If there is going to be a separate service, then I strongly believe that it should enforce Cody Enterprise L&G both for Cody-only Enterprise customers and Cody + Code Search Enterprise customers. On any other path lies inconsistency and madness. If Cody cannot always assume a Code Search Enterprise instance, Cody should never assume it. 

Or to put it another way, I suspect that from an implementation perspective, Cody + Code Search Enterprise L&G should be Cody Enterprise L&G running alongside Code Search L&G. (Whether that is visible to the customer or if we put some adapter in place to make them look like one is a separate question.) 

What does that mean for ownership? As Erik notes, a lot comes down to what that Cody Enterprise box really is[1]. What else is it supposed to do[2]? Does someone own it? @Ryan Phillips do you have any insights here?

[1] Side note: It's probably worth spending a moment on why this service differs from other things we have already. Unlike the Cody Gateway or the Accounts+PLG service, the Cody Enterprise service should be single-tenant. (The diagram indicates that it would still be Sourcegraph managed as a Cloud service, but given the past, from an eng perspective, I would build it so that it's capable of being self-hosted too.) 

[2] Some made-up examples of other things it could do: 
Enterprise specific Cody analytics (I don't know how these work today. Do they use dotcom? Piggyback on the Sourcegraph instance? Something else?)
Take on some of the tracking functionality that the Gateway currently does, but in a single tenant way? Or take on the "route to LLMs / embeddings service" capabilities? That's starting to sound big. 

### Assistant - 2023-11-02 14:38:03

Consider streamlining your text to focus on the essentials of the argument, the current state of affairs, and the strategic questions raised. Here's a revised version:

Philosophically, centralizing ownership of Enterprise licensing and gating across all products to Source is ideal for domain knowledge continuity and user experience consistency. In the future, a dedicated Licensing and Gating team should oversee both Enterprise and non-Enterprise functions, possibly including Billing.

Pragmatically, the Source team currently manages licensing and gating, specifically through a Sourcegraph instance, as noted in the Code Search Enterprise documentation. The immediate concern, highlighted by @Erik Seliger, is the implementation site for Cody Enterprise's licensing and gating.

Erik points out the inefficiency of requiring Cody-only Enterprise customers to operate a Sourcegraph instance they don't use. Hence, a standalone service for Cody's licensing and gating seems necessary. To avoid discrepancies and complications, this service should handle both Cody-only and combined Cody and Code Search Enterprise customers. Ideally, the implementation should ensure Cody operates independently, whether or not a Code Search Enterprise instance is present.

Ownership questions hinge on the intended functions of the Cody Enterprise service. Unlike Cody Gateway or Accounts+PLG service, it needs to be a single-tenant service, potentially self-hosted, and managed as a Sourcegraph cloud service. It could also incorporate Enterprise-specific analytics and some current Gateway tracking functions, suggesting a significant scope for the service.

@Ryan Phillips, your insights on the ownership and broader capabilities of the Cody Enterprise service are particularly valuable in this context.

### User - 2023-11-02 14:42:10

Here's an edited version. Please critique it again, but this time just say ways that it could be improved. Don't provide a modified draft.

Draft:
Philosophically, Source should own Enterprise licensing and gating across all of our products. Longer term, a Licensing and Gating (and maybe Billing) team should probably own Enterprise and non-enterprise licensing and gating. Why? Because even if there are separate implementations, the domain knowledge around licensing, gating, and billing would be shared. 

Pragmatically, the Source team owns licensing and gating (L&G) that is controlled by a Sourcegraph instance (a.k.a. Code Search Enterprise in the diagram from the doc above). That means a key question — which @Erik Seliger already raised — is: where will Cody Enterprise L&G be implemented?

As Erik notes, we shouldn't make Cody-only Enterprise customers run a Sourcegraph instance they aren't using. This implies that we'll need a separate service for Cody L&G ("Cody Enterprise" in the diagram Erik linked). 

If there is a separate service, then I strongly believe that it should enforce Cody Enterprise L&G both for Cody-only and Cody + Code Search Enterprise customers. On any other path lies inconsistency and madness. From an implementation perspective, Cody + Code Search Enterprise L&G should be Cody Enterprise L&G running alongside Code Search L&G. (Whether that is visible to the customer or if we put some adapter in place to make them look like one is a separate question.) 

What does that mean for ownership? As Erik notes, a lot comes down to what that Cody Enterprise box really is[1]. What else is it supposed to do[2]? Does someone own it? @Ryan Phillips do you have any insights here?

[1] Side note: It's probably worth spending a moment on why this service differs from other things we have already. Unlike the Cody Gateway or the Accounts+PLG service, the Cody Enterprise service should be single-tenant. (The diagram indicates that it would still be Sourcegraph managed as a Cloud service, but given the past, from an eng perspective, I would build it so that it's capable of being self-hosted too.) 

[2] Some made-up examples of other things it could do: 
Enterprise specific Cody analytics (I don't know how these work today. Do they use dotcom? Piggyback on the Sourcegraph instance? Something else?)
Take on some of the tracking functionality that the Gateway currently does, but in a single tenant way? Or take on the "route to LLMs / embeddings service" capabilities? That's starting to sound big. 

### Assistant - 2023-11-02 14:42:21

This draft provides a clearer perspective on the strategic direction for licensing and gating, yet there are ways to improve its clarity and impact:

1. **Clarifying Questions and Assertions**: Some questions and statements could be more directly linked to their implications. For instance, when asking where Cody Enterprise L&G will be implemented, immediately follow with the implications of possible answers to clarify why the question matters.

2. **Consolidate References**: References to Erik Seliger's points are scattered throughout the text. Consolidate these references to streamline the narrative and reinforce the arguments without repetition.

3. **Clarify Acronyms and References**: The first mention of "L&G" is clear, but subsequent uses assume familiarity. Reiterate what "L&G" stands for occasionally to maintain clarity, especially when introducing complex ideas.

4. **Explain Context**: Some context is assumed, like the role of Sourcegraph and its relationship to Cody. A brief explanation would enhance understanding, especially for those not intimately familiar with the current setup.

5. **Eliminate Ambiguity**: Phrases like "that's starting to sound big" are subjective. Clarify these by specifying what "big" means in this context—is it about scope, resource allocation, or complexity?

6. **Direct Call to Action**: When soliciting insights, such as from Ryan Phillips, specify the type of insights you are looking for. This encourages a more focused response.

7. **Use of Footnotes**: While footnotes [1] and [2] provide additional information, their current placement disrupts the flow. Consider integrating this information into the body of the text where it is directly relevant.

8. **Speculation on Capabilities**: When speculating about potential capabilities, it would be helpful to prioritize or categorize them (e.g., must-have vs. nice-to-have) to guide the discussion on what the Cody Enterprise service should entail.

By addressing these points, the draft could convey its strategic message more effectively.

