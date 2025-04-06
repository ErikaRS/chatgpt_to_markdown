# Deployment Options Discussion

Created: 2024-05-28 14:58:05
Last Updated: 2024-05-28 15:12:35

### User - 2024-05-28 14:58:05

Summarize the argument of this message. Use copious bullet points and keep the original voice.
I could support this as a deployment option, but I want to push back against going this direction a bit, and there's a couple angles on why:

First, even if we have one deployment that supports both gateway functionality and what, in the thread with the three of us and @Olaf Geirsson I called user owned data at rest functionality, we definitely should not use dotcom for that. 

The problem with dotcom isn't it's reliability. (Well, it is, but like you said, we could invest in fixing that.) The fundamental problem is that having our open source code search instance which anyone in the known universe can create an account on be the same backend that handles things like enterprise licensing and PLG billing is a nightmare from a sec review / compliance perspective. Which means that if we keep relying on dotcom, we will either fail to meet the security needs of large enterprise customers or we'll have to build duplicate solutions for PLG and enterprise. 

So, at the very least, we need to solve that problem. I think we can solve that by having two deployments. An open source code search deployment of code search and a sourcegraph instance used for administration. 

But that has a couple of concerns I'm worried about.

Multi-tenant will be harder to build
I don't think today's sourcegraph instance is a good foundation to build multi-tenant on. I think we'll go faster if we build a multi-tenant sourcegraph from scratch.
Single-tenant isolation will be harder to prove
Today, many of our enterprise customers who are willing to use the gateway require a lot of reassurance that the gateway doesn't store any of their private data at rest. It only stores configuration information. If we merge the gateway into a service which is hosting user data, it will be harder to draw a boundary between when user data is retained vs when it's not. 

That said, this architecture would solve the problem of integrating gateway functionality for BYOK/BYOLLM/airgapped customers, which is one of the warts in, e.g., the LLM model configuration proposal. 

So, counterproposal! Here's the architecture I'd like to work toward:
We have three things which:
Today's single-tenant sourcegraph. Eventually, I'd like this to go away, but since we can't throw it away and shouldn't build tomorrow on it, we have to keep it working. 
A new multi-tenant backend which can contain at-rest user data and it's derivatives
Support services, which are all of the sourcegraph hosted things non-airgaped customers will need to use Cody/Code Search
(And, as I said on the Olaf thread: we should have a more coherent story around airgaped, but I'm willing to push that off a little)

This does mean we will still have some complexity around between service communication and authentication, but I think it will directly translate to an ability to close deals faster, so I think it's worth it, especially if we support a monolithic deployment mode. 

### Assistant - 2024-05-28 14:58:15



### Assistant - 2024-05-28 14:58:15

- Support deployment option but want to push back against it.
- Concerns about using dotcom for deployment:
  - Issues with dotcom reliability (although fixable with investment).
  - Main issue: security and compliance nightmare.
    - Open source code search instance accessible to anyone should not share the same backend with enterprise licensing and PLG billing.
    - Potential security compliance failures for large enterprises.
    - Need to build duplicate solutions for PLG and enterprise if relying on dotcom.
- Suggests solving this by having two separate deployments:
  - An open source code search deployment.
  - A Sourcegraph instance for administration.
- Concerns about this approach:
  - Multi-tenant will be harder to build:
    - Current Sourcegraph instance isn't a good foundation for multi-tenant.
    - Building a multi-tenant Sourcegraph from scratch would be faster.
  - Single-tenant isolation will be harder to prove:
    - Enterprise customers need reassurance that the gateway doesn’t store private data.
    - Merging the gateway with a service hosting user data complicates data retention boundaries.
- Acknowledges that the proposed architecture solves integration issues for BYOK/BYOLLM/airgapped customers.
- Counterproposal:
  - Maintain three components:
    - Today’s single-tenant Sourcegraph (eventually phased out but kept functional for now).
    - A new multi-tenant backend containing at-rest user data and derivatives.
    - Support services for Sourcegraph hosted needs for non-airgapped customers using Cody/Code Search.
  - Coherent strategy for airgapped customers can be delayed slightly.
- Accepts some complexity in service communication and authentication as it can accelerate deal closures.
- Advocates for supporting a monolithic deployment mode.

### User - 2024-05-28 14:58:54

Now rephrase the original to be more concise and focused, using the outline to double check that no key points were left out. 

### Assistant - 2024-05-28 14:59:03

I can support this deployment option but want to push back for a few reasons:

First, combining gateway functionality and user-owned data at rest should not use dotcom. The issue isn't dotcom's reliability (which can be fixed), but security. Using the same backend for open-source code search and enterprise licensing/PLG billing creates security and compliance problems. This would either fail to meet enterprise security needs or require duplicate solutions for PLG and enterprise.

We need two deployments: an open-source code search and a Sourcegraph instance for administration. However, this approach has concerns:

- Multi-tenant build: Current Sourcegraph isn't ideal for multi-tenant. Starting from scratch would be faster.
- Single-tenant isolation: Enterprise customers need assurance that the gateway doesn't store private data. Merging the gateway with user data services complicates this.

This architecture could solve integration issues for BYOK/BYOLLM/airgapped customers.

Counterproposal:
- Maintain three components:
  1. Today’s single-tenant Sourcegraph (phased out eventually but kept functional).
  2. New multi-tenant backend with at-rest user data and derivatives.
  3. Support services for non-airgapped customers using Cody/Code Search.

A coherent strategy for airgapped customers can be delayed slightly.

Accepting some complexity in service communication and authentication is worthwhile for faster deal closures, especially if we support a monolithic deployment mode.

### User - 2024-05-28 15:12:19

What points from the original/outline are missing from this version? 
Moving back to using sourcegraph as a monolith and, in particular, building  any more on dotcom worries me. So I'd love to propose an alternative.

Stop building on dotcom
In my view, reliability isn't the main problem with dotcom. It's data security issues which are inherent in how we use it. Anyone in the known universe can create an account on dotcom — the same backend which handles enterprise licensing, PLG billing, and until recently things like accounts and telemetry. This is already a pain from a compliance perspective, and doing more on dotcom will make it worse. 

So, alternative part 1: Decouple dotcom. Create two deployments: an open source code search deployment and a deployment which just had the administrative bits and is only accessible by authorized sourcegraph employees. 

I would be comfortable moving the Gateway into the administrative bits deployment. I am not comfortable moving the Gateway into today's dotcom, and I think that doing so would require to revisit security reviews with all of our existing Cody enterprise customers. 

Stop building on the current monolith
Building on today's monolith also slows us down. E.g., any database changes we make have potential repercussions in upgrades and unexpected side effects that require extensive testing, often manual. So I don't think building on the monolith is the right solution here for long term velocity. Also, sg/sg has a lot of single-tenant assumptions built in, and building a multi-tenant solution on it will be fundamentally insecure.

Another thing I want to build for is being able to close deals quickly and have an architecture that makes security reviews fast. Doing that will be much easier if we keep deployments which host user-data at rest 

So, alternative part 2: Build toward the architecture in the picture here where we have: 
Today's single-tenant sourcegraph. Eventually, I'd like this to go away, but since we can't throw it away and shouldn't build tomorrow on it, we have to keep it working. 
A new multi-tenant backend which can contain at-rest user data and it's derivatives
The administrative bits (support services) which contain the functionality that is needed both single- and multi-tenant instances and doesn't contain at-rest user owned data

We would still have to deal with authentication across the user-data-at-rest deployment and the administrative-bits deployment, so maybe at least for development, we can combine their deployment. However, I think doing so in production is going to cause problems that will ultimately slow us down even if it increases developer velocity. 

Thoughts? 

### Assistant - 2024-05-28 15:12:35

Here are the missing points from the original/outline that need to be included:

- The explicit preference to move away from building on dotcom and the current monolith.
- Detailed reasons for why dotcom is problematic:
  - Data security issues due to its open nature.
  - Compliance challenges.
- Proposal to decouple dotcom into two separate deployments:
  - Open source code search deployment.
  - Administrative bits deployment, accessible only by authorized Sourcegraph employees.
- Specific concern about moving the Gateway into today's dotcom, requiring revisits of security reviews with existing Cody enterprise customers.
- The inefficiencies of building on the current monolith:
  - Database changes causing potential issues.
  - Single-tenant assumptions making a multi-tenant solution fundamentally insecure.
- The aim to close deals quickly and facilitate fast security reviews.
- Proposal for a new architecture:
  - Today's single-tenant Sourcegraph (kept functional but eventually phased out).
  - A new multi-tenant backend with at-rest user data and its derivatives.
  - Administrative bits (support services) for both single- and multi-tenant instances without at-rest user-owned data.
- The potential need to combine deployments during development to address authentication challenges, but keeping them separate in production to avoid long-term issues.

Here is the revised, concise version including these points:

I support the deployment option but want to push back for a few reasons:

Moving back to using Sourcegraph as a monolith and building more on dotcom worries me. The main issue with dotcom isn't reliability but data security. Anyone can create an account on dotcom, which handles enterprise licensing, PLG billing, and until recently, accounts and telemetry. This creates compliance issues, and expanding dotcom's use would worsen them.

**Alternative Part 1: Decouple dotcom**
- Create two deployments: an open-source code search and an administrative deployment accessible only by authorized Sourcegraph employees.
- I’m comfortable moving the Gateway into the administrative deployment but not into dotcom, as it would require revisiting security reviews with existing Cody enterprise customers.

Building on the current monolith also slows us down due to potential database change repercussions and single-tenant assumptions making a multi-tenant solution insecure.

**Alternative Part 2: New Architecture**
- Maintain three components:
  - Today’s single-tenant Sourcegraph (kept functional but eventually phased out).
  - A new multi-tenant backend with at-rest user data and its derivatives.
  - Administrative bits (support services) needed for both single- and multi-tenant instances, without at-rest user-owned data.

Combining deployments during development may address authentication challenges, but keeping them separate in production avoids long-term issues and ultimately slows us down. This new architecture aims to close deals quickly and facilitate fast security reviews, supporting a monolithic deployment mode. Thoughts?

