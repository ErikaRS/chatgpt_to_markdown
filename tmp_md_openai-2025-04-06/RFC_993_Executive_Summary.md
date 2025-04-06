# RFC 993 Executive Summary

Created: 2024-10-11 16:52:22
Last Updated: 2024-10-11 16:52:32

### User - 2024-10-11 16:52:22

I am the head of engineering. Give me a literal executive summary of this. But a technical one, befitting my being head of engineering. Also include a list of key questions I should think about while approving this

RFC 993: Zero-config M2M access management with SAMS Security Token Service (STS)
Editor: Joe Chen
Last updated: Oct 10, 2024
Status: Under review
Input providers: Core Services
Requested approvers (in no particular order, by EOD 2024-10-22): 
Security:
Vincent Ruijter
Core Services:
Eric Shamow (optional)
Robert Lin
James Cotter
Stakeholders:
Michael Lin (Cloud Ops)
Erik Seliger (MT Sourcegraph)
Matt Manela (optional, MT Sourcegraph)
Architecture Working Group:
André Eleuterio (optional)
Camden Cheek (optional)
Erika Rice Scherpelz (optional)
Julie Tibshirani (optional)
Louis Jarvis (optional)
Olaf Geirsson (optional)
LGTMs: DON’T BE SHY
Context
All of Sourcegraph managed services rely on SAMS Machine-to-machine (M2M) Authentication and Authorization for inter-service access management. OAuth 2 client credentials are created and distributed to each managed service for requesting short-lived access tokens. Each pair of client credentials consists of a client ID and a client secret, and (out of band) defines what token scopes are allowed to be requested then granted to those access tokens.

SAMS management API authenticates all requests via a randomly generated but static and cannot-be-rotated-without-stopping-the-world secret. More problematically, it is usually stored locally (in plaintext and very often in shell history) and in GitHub Actions secrets for self-serve GitHub Actions against SAMS (e.g. Create Sourcegraph Accounts user) that are mainly used by CE/TA/Support.

To streamline the machine-to-machine access tokens issuance, there is a widely-adopted solution built on top of OIDC called Security Token Service (STS) which has been supported by all major Cloud platforms (think GitHub.com, GCP, AWS, Microsoft Azure, Terraform Cloud). GitHub documentation provides a good high-level overview of how it works (in the context of GitHub.com; not a required read as this RFC will explain it in detail anyway), but the digest is: it operates based on trust relationships between identity provider and resource owners, and once the trust relationships are established, it is zero-config for the client services (i.e. no need for creating and managing client credentials for each service) to request short-lived access tokens. 
Problems
The (current) traditional approach for managing OAuth clients and corresponding credentials of different services imposes non-trivial management overheads on both client services and server-side (SAMS) with no optimization paths available:
Client services always need to go through the manual creation process of new clients, and go through the full lifecycle of OAuth client configuration management out-of-band.
Client services are always required to be connected with a secure persistent storage for storing client credentials.
Both above points make it particularly cumbersome for ephemeral/lean services to take the full advantage of SAMS ecosystem. Or avoid integrating with SAMS in the first place.
SAMS needs a lot of UI/UX work around OAuth client configuration management (which doesn’t exist right now). Also due to the fact that all integrations with SAMS are internal-only for the foreseeable future, and the effort required to make a good UI/UX around current management overhead doesn’t contribute to any of the core functionality (making OAuth flows and M2M work properly) when the primary user of the system is Sourcegraph itself.
Access tokens are scoped and short-lived with client credentials, client credentials are nonetheless another form of long-lived static secrets that requires extra care when it comes to secret rotation (i.e. while it is designed to be rotatable, actually rotating a client secret is still an exercise, and it can’t be done so frequently and automatically).
The static secret of SAMS management API is used and stored in many different places, including locally (in plaintext and very often in shell history), random Slack DMs, etc. More problematically,
There is currently no way to identify who made the API call from the request itself, and anyone who has the secret is authorized for making requests to all endpoints (including the ones that can be destructive and irreversible).
No built-in secret rotation support, and rotating the management API secret requires “downtime” of many moving parts (aka. Stop-the-world rotation).
For maximum security, we should rotate all of the client credentials and the management API secret every time a teammate leaves Sourcegraph, which isn’t practically feasible. That often leaves the “back-door” access after departure that entirely depends on people’s good faith.
Prioritization
The solution coming out of this RFC is directly affecting/eliminating the big client credentials management overhead for Multi-tenant Sourcegraph and its suboptimal local DX. Thus advocating for prioritizing the implementation of the proposed solution after MT Phase 2 but before MT V1/GA.
Proposal
Introducing SAMS STS, by being part of the STS ecosystem, we are able to unlock state-of-the-art, seamless and secure M2M integrations between Sourcegraph managed services and all other STS-capable platforms. And thanks to SAMS being an OIDC-compliant Identity Provider (IdP), this means not only integrations on STS-capable platforms can talk to Sourcegraph managed services via STS, but also Sourcegraph managed services can talk to those platforms via STS!

How does SAMS STS address all problems mentioned above?
For client services using STS, there is zero management overhead on the OAuth client because there will be no client secret.
Because there is no OAuth client to manage, there is no lifecycle of client configuration management.
Because there is no client secret, it eliminates the need to distribute and securely store client credentials.
Because integrating with SAMS becomes so effortless for services, it is much more convincing for all possible services to be part of the SAMS ecosystem and take full advantage of it.
Because there is no lifecycle of client configuration management anymore, the engineering resources can be better spent on making STS work better that directly contributes to the core workflow of every developer at Sourcegraph.
Not only client services have short-lived access tokens, they also have short-lived ID tokens issued by the respective STS-capable platform. Which by design, eliminates the need to rotate client secrets because they don't exist anymore.
An “ID token” is a time-bound proof of identity that itself can be used as a form of token.
SAMS management API is then able to accept SAMS (short-lived) access tokens issued via STS in combination with token scopes to practice the least privilege principle.
SAMS management API can be made to accept SAMS access tokens without STS but how to issue those access tokens to Sourcegraph teammates remains an unsolved problem.
For a similar reason, Cloud API currently rolls out its own authentication implementation and some hacks are required for things to work.
No more insecure secret sharing over DMs and local storage in plaintext (without a good reason).
Every access token is always associated with a principal (e.g. a user, a service account, a GitHub repository, or a workload identity, and much more) when used for making requests that allows us to do proper audit logging.
Again, by design, eliminates the need to rotate the management secret because it doesn't exist anymore.
Short-lived access tokens and no static client credentials by design, in combination with being able to identify the principal of the request, losing access to the Sourcegraph Google account effectively removes all the access privileges to our managed services.

What’s more, SAMS STS would also unlock a bunch of exciting use cases that weren’t possible (exactly how and more details will be explained in later sections):
CLIs like `sg` and `mi2` are able to make authenticated requests to any SAMS-integrated services directly without any configuration.
This would allow Cloud API to be part of SAMS ecosystem.
Sourcegraph teammates are able to use Entitle to grant time-bound access to high-privilege API endpoints in a self-serve manner.
Although the primary focus of STS is for (backchanneling) M2M communication, we have the option to take one step further to make it work for client services that provide OAuth flow to end users, so they can continue providing the “Sign in with Sourcegraph Accounts” experience without static client credentials.
This would avoid the needs of client credentials management for Multi-tenant Sourcegraph cloud instances.
This will be a minor addition to the overall STS implementation, see implementation plan.
Architecture overview
Below is an example architecture illustration of the STS ecosystem between SAMS, GCP, GitHub Actions and local dev.


View and comment on Excalidraw
Illustration 1: GitHub Actions workflow access to Enterprise Portal APIs
When the workflow of the GitHub repository (github.com/sourcegraph/cody-analytics) starts, it requests an ID token from GitHub OIDC Provider using its GitHub Actions Workflow Identity (step 1.1).
The workflow then sends the ID token to the STS endpoint of SAMS OIDC Provider to exchange for an SAMS access token (step 1.2).
The workflow then sends the SAMS access token to Enterprise Portal APIs to perform intended operations (step 1.3).
Illustration 2: Sourcegraph Cloud instance access to Workspaces APIs
The workspace reconciler of a Sourcegraph Cloud instance first requests an ID token from Google OIDC Provider using its GKE Workload Identity (step 2.1).
The reconciler then sends the ID token to the STS endpoint of SAMS OIDC Provider to exchange for an SAMS access token (step 2.2).
The reconciler then sends the SAMS access token to Workspaces APIs to fetch information and report reconcile status (step 2.3).
Illustration 3: Local sg CLI access to Cloud API
The sg CLI first requests an ID token from Google OIDC Provider using teammate’s Google Account Identity (step 3.1).
The sg CLI then sends the ID tokens to the STS endpoint of SAMS OIDC Provider to exchange for an SAMS access token (step 3.2).
The sg CLI then sends the SAMS access token to Cloud API to perform intended operations (step 3.3).
Other notes
Not all possible paths and directions are included for brevity of the illustration.
Not all possible components/services within each platform are included for brevity of the illustration.
Principal of any STS-capable platforms can talk to any SAMS-integrated services, e.g.
GitHub Actions workflows <-> Workspaces APIs, Enterprise Portal APIs, Sourcegraph Cloud instance, etc.
CLI sg/mi2 <-> Workspaces APIs, Enterprise Portal APIs, Sourcegraph Cloud instance, Cloud Control Plane, etc.
Any of Workspaces APIs, Enterprise Portal APIs, Sourcegraph Cloud instance, Cloud Control Plane, etc.
 <-> any of Workspaces APIs, Enterprise Portal APIs, Sourcegraph Cloud instance, Cloud Control Plane, etc.
Other STS-capable platforms would work in similar ways, including but not limited to, Microsoft Azure, AWS, Terraform Cloud and many more.
What is the magic behind STS?
There isn’t any magic.
Step 0: Established an OIDC trust relationship between two STS-capable platforms
Every OIDC provider provides an OIDC discovery endpoint (`{ISSUER}/.well-known/openid-configuration`) to broadcast some basic facts about the provider. For example, below is a snapshot of what SAMS responds:


One of the fields in the discovery document is the `jwks_uri`, whose value is another URL for listing the public counterparts of all private signing keys that could be used for signing ID tokens issued by the given OIDC provider. For example, below is a snapshot of keys published by SAMS (no need to try to understand any of it, only need to know this exists):


Upon every OIDC-based user authentication, clients use this list of keys to verify the signature of the ID token they get back (to mitigate response hijacking). STS is basically reusing this verifiability of an ID token outside a user-facing authentication flow.

Then in every ID token, it contains who issued the token as the value of `iss`:
For SAMS, it is `https://accounts.sourcegraph.com`
For GitHub Actions, it is `https://token.actions.githubusercontent.com` 
For Google accounts, it is `https://accounts.google.com` or `accounts.google.com` 

Therefore, when we say an OIDC trust relationship is established between SAMS and GitHub Actions, it really just means that SAMS will verify all ID tokens issued by `https://token.actions.githubusercontent.com` using keys listed in its `jwks_uri`. Once verified, it will be accepted as a proof of identity thus issuing an SAMS access token.
Step 1: Define allowed scopes to be requested/granted by the specific resource
Every OAuth access token needs to be granted with some scopes because by design, an access token without any scope is effectively a void access token. For security measures and by the design of OAuth, what scopes are allowed to be requested by what resource (which are then granted to access tokens issued to them) must be predefined.

For example, to make Illustration 1: GitHub Actions workflow access to Enterprise Portal APIs work, we will allow GitHub Actions workflow of the repository `sourcegraph/cody-analytics` to request the scope `enterprise_portal::permission.subscription::write` for it to update customer admins of specific enterprise subscriptions.
Step 2: Exchange SAMS access token with ID token from respective OIDC provider
When, for example, the GitHub Actions workflow of the repository `sourcegraph/cody-analytics` starts, it uses GitHub Actions SDK to request an signed ID token (in JWT format), below is an base64-decoded example for a GitHub Actions workflow:
{
  "typ": "JWT",
  "alg": "RS256",
  "x5t": "example-thumbprint",
  "kid": "example-key-id"
}


{
  "jti": "example-id",
  "sub": "repo:sourcegraph/cody-analytics",
  "aud": "https://github.com/sourcegraph",
  "ref": "refs/heads/main",
  "sha": "example-sha",
  "repository": "sourcegraph/cody-analytics",
  "repository_owner": "sourcegraph",
  "actor_id": "12",
  "repository_visibility": "private",
  "repository_id": "74",
  "repository_owner_id": "65",
  "run_id": "example-run-id",
  "run_number": "10",
  "run_attempt": "2",
  "runner_environment": "github-hosted"
  "actor": "octocat",
  "workflow": "example-workflow",
  "head_ref": "",
  "base_ref": "",
  "event_name": "workflow_dispatch",
  "ref_type": "branch",
  "job_workflow_ref": "sourcegraph/cody-analytics/.github/workflows/oidc.yml@refs/heads/main",
  "iss": "https://token.actions.githubusercontent.com",
  "nbf": 1632492967,
  "exp": 1632493867,
  "iat": 1632493567
}


It comes in two parts (single string when base64-encoded):
The top part is the signing metadata, including what type, algorithm and key it was used to sign the ID token.
The bottom part is the actual ID token, where it includes the identifier of the principal (`sub`), which repository/resource it is (`repo`), who issued the ID token (`iss`), and when this ID token is no longer valid even if the signature matches (`exp`).

The workflow then sends this signed ID token as-is along with requested scopes to SAMS STS endpoint. Once the SAMS STS handler verifies the validity of the given ID token, and confirms the requested scopes are allowed by the given resource, an SAMS access token with requested scopes granted is then issued.

This is the end of STS flow, the remaining sections are here for completeness.
Step 3: Send requests to the target service with SAMS access token
Now the workflow has an SAMS access token, plug it into the “Authorization: Bearer {token}” header, then make requests to Enterprise Portal APIs.
Step 4: Target service performs authorization check with the given SAMS access token
Upon receiving any requests on the Enterprise Portal side, it sends the access token as-is to SAMS token introspection endpoint to validate that:
Whether or not this access token is valid and not expired
What are the scopes granted to this access token

If all looks good, then proceed with processing the actual request.
Design decisions
The SAMS STS endpoint will live at https://accounts.sourcegraph.com/sts.
Typically, platforms use the `sts` subdomain for the STS endpoint (e.g. `sts.googleapis.com`, `sts.amazonaws.com`), but SAMS is already living in a subdomain and MSP convention is to use different subdomains for differents services, having SAMS STS endpoint living at a path makes more sense.
There will be a shared special OAuth client where all STS-issued access tokens belong to, whose client ID is `sams_cid_sts`, and effectively no client secret (so no one can use it like a regular OAuth client).
For security measures, this special client is not automatically allowed to request all of the available token scopes defined in SAMS, and any scope has to be manually granted (in the client configuration). Thus it controls the “upper-bound” of what scopes that STS-issued access tokens can grant.
Note that just because this special client has a scope, doesn't mean any STS-issued access token will be able to request that scope. It all depends on the (further) allowed scopes of the requesting resource. Furthermore, the resource may choose to request a subset of allowed scopes at the time of access token issuance.
Also see Why a shared OAuth client? Is it less secure?
Every resource (e.g. a GitHub Actions Workflow of a repository, a Google account, a GCP/GKE workload) and their allowed scopes are managed using ReBAC in SAMS via the MSP IAM framework.
To support client services that need to present user-facing OAuth authentication flows (CORE-84):
The special OAuth client will support using signed ID tokens as a form of authentication for Authorize Code Flow.
Similar to allowed scopes, every resource will have their allowed redirect URIs managed using ReBAC in SAMS via the MSP IAM framework.
API design
SAMS STS endpoint
Although there is no standard protocol defined for STS, there is the RFC 8693: OAuth 2.0 Token Exchange whose request and response format is compatible with the idea of STS, which is also what GCP uses for its STS endpoint.

Below is an example of a request can be sent to the SAMS STS endpoint in exchange for an SAMS access token:
POST https://accounts.sourcegraph.com/sts/v1/token
{
  "grantType": "urn:ietf:params:oauth:grant-type:token-exchange",
  "scope": "openid email profile enterprise_portal::permission.subscription::write",
  "requestedTokenType": "urn:ietf:params:oauth:token-type:access_token",
  "subjectToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6xxx.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20yyy.zzz",
  "subjectTokenType": "urn:ietf:params:oauth:token-type:jwt"
}


Request fields definition:
grantType
string

Required. The grant type. As of this RFC, it must be urn:ietf:params:oauth:grant-type:token-exchange, which indicates a token exchange.
scope
string

Required. The OAuth 2.0 scopes to include on the resulting access token, formatted as a list of space-delimited, case-sensitive strings.
requestedTokenType
string

Required. An identifier for the type of requested security token. As of this RFC, it must be urn:ietf:params:oauth:token-type:access_token.
subjectToken
string

Required. The JWT-format signed ID token.
subjectTokenType
string

Required. An identifier that indicates the type of the security token in the subjectToken parameter. As of this RFC, it must be urn:ietf:params:oauth:token-type:jwt.


Below is an example a response can be responded by the SAMS STS endpoint:
{
  "access_token": "sams_at_HrJujj4KW1jcv_g-bVn2AENZaBhqDN2mAkTEMyxIX3k.7dYpa8XqHy0Jdfq4jr...",
  "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
  "token_type": "bearer",
  "expires_in": 3600
}


Response fields definition:
access_token
string

The SAMS access token.
issued_token_type
string

The token type. Always matches the value of requestedTokenType from the request.
token_type
string

The type of access token. Always has the value bearer.
expires_in
integer

The amount of time, in seconds, between the time when the access token was issued and the time when the access token will expire.


In the STS handler, it determines which STS platform to verify the ID token via `iss` field and what resource identifier to use depending on the STS platform:
`email` for Google accounts
`repo` for GitHub Actions (we still have the option to be more granular/use other fields in the future, e.g. branch, environment)

To be future-compatible, here is the scheme for how a fully qualified resource identifier is composed of `platform|resource type|resource ID`, e.g.:
`google|email|cody-analytics-sa@cody-analytics-svc-5cfd.iam`, `google|email|joe@sourcegraph.com` 
`github|repo|github.com/sourcegraph/cody-analytics` 

Picked `|` as the delimiter because it is a fairly rare character to be used as part of a system-generated ID string. Auth0 uses it for recording external identities, for example.

This does mean that to support new STS platforms, code changes are required (which is fine and we get pull request approval flow as a line of defense since the insecurity of the trust relationship invalidates everything else). In the future, we may be able to make them configurable, i.e. the issuer URL and what fields from ID token to use as resource ID.
SAMS Management API for CRUD allowed scopes and redirect URIs of resources
Management API should take advantage of this time of big change to fully transition to use ConnectRPC, in par with the MSP API convection.

service ManagementService {
  // GetSecureTokenServiceResource returns the given Security Token Service resource.
  rpc GetSecureTokenServiceResource(GetSecureTokenServiceResourceRequest) returns (GetSecureTokenServiceResourceResponse) {
    option idempotency_level = NO_SIDE_EFFECTS;
    option (sams_required_scopes) = "sams::management.security_token_service::read";
  }
  // UpdateSecureTokenServiceResource updates the given Security Token Service resource.
  rpc UpdateSecureTokenServiceResource(UpdateSecureTokenServiceResourceRequest) returns (UpdateSecureTokenServiceResourceResponse) {
    option idempotency_level = IDEMPOTENT;
    option (sams_required_scopes) = "sams::management.security_token_service::write";
  }
}

message SecurityTokenServiceResource {
  // The fully qualified resource identifier, e.g.
  // - "google|email|cody-analytics-sa@cody-analytics-svc-5cfd.iam"
  // - `github|repo|github.com/sourcegraph/cody-analytics`
  string id = 1;
  // The list of allowed scopes.
  repeated string scopes = 2;
  // The list of allowed redirect URIs.
  repeated string redirect_uris = 3;
}

message GetSecurityTokenServiceResourceRequest {
  // Query specifies the lookup strategy for this get request.
  oneof query {
    // Look up a resource using its fully qualified resource identifier.
    string id = 1;
  }
}

message GetSecurityTokenServiceResourceResponse {
  SecureTokenServiceResource resource = 1;
}

message UpdateSecurityTokenServiceResourceRequest {
  // The following fields are used to identify the resource to update:
  //  - id
  // Multiple fields are treated as AND-concatenated.
  SecurityTokenServiceResource resource = 1;

  // The list of fields to update, fields are specified relative to the SecurityTokenServiceResource.
  // Updatable fields are:
  //  - scopes
  //  - redirect_uris
  google.protobuf.FieldMask update_mask = 2;
}


The above RPCs require to introduce following new token scopes (also see SAMS token scope specification):
`sams::management.security_token_service::read`
`sams::management.security_token_service::write`
`sams::management.security_token_service::delete`
And others for existing endpoints as appropriate
IAM model design
model
 schema 1.1


# Represented by the fully qualified resource identifier.
type resource


# A group of resources.
type resource_group
 relations
   define role_member: [resource]


# Represented by the OAuth token scope.
type scope
 relations
   define role_resource: [resource, resource_group#role_member]
   define permission_allow: role_resource


# Represented by the OAuth redirect URI.
type redirect_uri
 relations
   define role_resource: [resource, resource_group#role_member]
   define permission_allow: role_resource


For security measures (prevent unforeseen syntax injection) and to avoid syntax conflict with OpenFGA, all scopes, redirect URIs and fully qualified resource identifiers are SHA256-ed (only) within OpenFGA storage.

For DX consideration for Sourcegraph teammates:
We can create a `resource_group:cd7c13b2dba6c0802f8c8c2cd5232085e65b42f416649de74629162b65ebfacf` which includes every Sourcegraph teammate:
“cd7c13b2dba6c0802f8c8c2cd5232085e65b42f416649de74629162b65ebfacf” is SHA256 of “rg_sourcegraph_employees”
The term “employees” is not entirely accurate, but to be aligned with the terminologies used in Bamboo HR and how SAMS sync employees from it.
SAMS already has a periodic background syncer to sync Sourcegraph teammates from Bamboo HR, which can also be used to maintain the membership of this resource group.
Then we “grant” common scopes and redirect URIs to the resource group instead, e.g. in Zanzibar notation:
scope:a780fc8d532ce48dc62ac7d2027bf9b07f036b7f5ec1824a882d89c35d183887#role_resource@resource_group:cd7c13b2dba6c0802f8c8c2cd5232085e65b42f416649de74629162b65ebfacf (“scope:openid”)
redirect_uri:7ece45af9b708bf2e90ce16da1d2f9abce7dcc759031f20b1151884a2d9996a1#role_resource@resource_group:cd7c13b2dba6c0802f8c8c2cd5232085e65b42f416649de74629162b65ebfacf (“redirect_uri:https://sourcegraph.test:3443/auth/callback”)
CLI-as-UI design
Adds a new subcommand `sg sams sts`, which is an alias of `sg sams security-token-service`:
sg sams sts scopes <resource> +[<scope>,...] 
Incrementally add new allowed scope(s) to the resource
sg sams sts scopes <resource> -[<scope>, …] 
Decementially remove existing allowed scope(s) from the resource
sg sams sts scopes <resource> =[<scope>, …] 
Force-replace all of the allowed scopes of a resource
sg sams sts redirect_uris <resource> +[<redirect_uri>,...] 
Incrementally add new allowed redirect URI(s) to the resource
sg sams sts redirect_uris <resource> -[<redirect_uri>, …] 
Decementially remove existing allowed redirect URI(s) from the resource
sg sams sts redirect_uris <resource> =[<redirect_uri>, …] 
Force-replace all of the allowed redirect URIs of a resource
FAQs
Why a shared OAuth client? Is it less secure?
A shared OAuth client is inevitable because which OAuth client to issue the access tokens is not customizable in a way that the value is also being signed as part of the ID token JWT. Then theoretically a miscous user can simply fake which OAuth client the resource belongs to that can circumvent any enforcement we put in.

Therefore, it is better to put security measures not in terms of OAuth clients, but the actual scopes a resource is allowed to request. For the exact same reason, we have ultimate control of allowed scopes for every resource that makes the shared client approach no less secure in any way compared to different OAuth clients for different sets of resources.
How do I get an ID token in local dev for my Google account?
Run `gcloud auth print-identity-token`, then you can copy it to CyberChef for exploration (WARNING: malicious users can use this token to impersonate you!).

Or (thanks to Vincent Ruijter):

gcloud auth print-identity-token | base64 -d | hexdump -C

Does this mean services running on my local dev can have direct M2M communication to managed services via my Google account identity?
Yes.

Say few engineers are developing Cody Analytics locally and the service needs to talk to Enterprise Portal dev (enterprise-portal.sgdev.org). Instead of creating a shared SAMS client in SAMS-dev (accounts.sgdev.org) as we are doing right now, all of these engineers will be able to have their local Cody Analytics service talk to Enterprise Portal dev out-of-the-box (assuming `gcloud auth application-default` was done once). That’s because the service logic (once updated) will use the ID token of each engineer’s Google account to automatically exchange for a usable SAMS access token.
When I use my Sourcegraph Google account making M2M requests from my laptop, who am I?
Technically speaking, you’re acting as a client service because you would get client-level SAMS access tokens. You need to obtain user-level SAMS access tokens to represent a SAMS user, which is not possible without going through a user-facing authentication flow (we do not yet support impersonation).
Implementation plan
Phase 1: Core STS implementation (18-20 days)
(5 days) Implement SAMS management API v2 server-side logic with the above-defined protobuf schema
(5 days) Implement SAMS STS endpoint handler
This may require some clever logic injection that work nicely with the ory/fosite package
Updated Authorize Code Flow using signed ID token as the client secret
(2 days) Update SAMS SDK for STS-related client-side logic
(2 days) Implement proposed `sg sams sts` subcommand
This includes setting the special resource group for Sourcegraph teammates so people can actually use this command.
(1 day) Create a new Notion page for documentation
(3-5 days) Pentesting
Phase 2: Core STS integrations (5 days)
(2 days) Implement reusable GitHub Actions for interacting with SAMS management API v2 via STS
(2 days) Update existing clients using SAMS management API v1
(1 day) Delete SAMS management API v1 endpoint and its server-side logic
Phase 3: Migrate eligible services to use STS (10-15 days)
All steps can be executed in parallel.

(5 days) Update all eligible SAMS-integrated services to use STS
Cody Analytics
Enterprise Portal
Workspaces
Sourcegraph.com
MT Sourcegraph instances
(5 days) Update the Cloud API and `sg eph` to use STS (thus become SAMS-integrated)
(5 days, optional) Update the Cloud Control Panel and `mi2` to use STS (thus become SAMS-integrated)
Phase 4: Entitle-integrated scope grant for Sourcegraph teammates (2 days)
Assuming Streamlined role assignment via SAMS and Entitle is fully implemented.

(2 days) Register Entitle-able scopes (to SAMS itself)
Implementation notes
This section is purely a list of notes for implementers, understanding it requires deep knowledge of how SAMS works internally, reviewers feel free to skip.

In `idp_session`, we need an extra field to annotate the resource that initiates the token issuance session since now the `client_id` column is useless (all the same for STS-initiated token issuance sessions). Propose to use the `sub` field of the object stored in the `claims` column (currently empty for client-level access tokens, and only user-level access tokens has SAMS account ID as the value of the `sub` field).
Also in `idp_session` and the `claims` column, for tracking/auditing purposes, propose to add an extra field `sub_token` to store the ID token portion extracted from the `subjectToken` (of an STS request, leaving out the header and signature part so this value can’t be reused as an access token anymore).
During token introspection of Clients API, the server needs to return information about the resource that requested the access token since now the `ClientID` field is useless (all the same for STS-issued access tokens). Propose a new field named `Subject`.
For the special `sams_cid_sts`, we just create the client with the default random secret but never tell anyone what that is, so effectively, no one could use it as if it doesn't exist. Using real empty value as secret is not safe, as it leaves the hole that it might be successfully authenticated when a micaluis user actually passes in an empty value.
Success criteria
Strengthen our security measures for our managed production services by making the implementation of inter-service zero-trust communications table stakes.
All eligible SAMS-integrated are able to migrate to use STS and no more use of statically-and-shared OAuth client secrets.
“Eligible” refers to services that run on a STS-capable platform, e.g. GitHub Actions, GCP. 
Eliminate the overhead of pre-configured secrets for Sourcegraph teammates integrating and testing against (dev-version) managed services from local dev.
References
Enabling keyless authentication from GitHub Actions (Google Cloud)
https://github.com/google-github-actions/auth - A GitHub Action for authenticating to Google Cloud
Configuring OpenID Connect in cloud providers (GitHub)
Understanding token exchange in OAuth/OIDC (Logto)
Appendix
OpenFGA tests to verify listing scopes of a user via a userset works
model_file: ./sts_iam_model.fga

tuples:
  - user: resource:joe
    relation: role_member
    object: resource_group:rg_sourcegraph_employees
  - user: resource:robert
    relation: role_member
    object: resource_group:rg_sourcegraph_employees

  - user: resource_group:rg_sourcegraph_employees#role_member
    relation: role_resource
    object: scope:openid
  - user: resource:joe
    relation: role_resource
    object: scope:email

tests:
  - name: list scopes of a resource
    list_objects:
      - user: resource:joe
        type: scope
        assertions:
          role_resource:
            - scope:openid
            - scope:email




### Assistant - 2024-10-11 16:52:31



### Assistant - 2024-10-11 16:52:31

Here’s a technical executive summary of RFC 993:

**RFC 993: Zero-config M2M access management with SAMS Security Token Service (STS)**

**Overview**: 
This RFC proposes the introduction of a Security Token Service (STS) for SAMS, Sourcegraph's managed services machine-to-machine (M2M) Authentication and Authorization mechanism. It aims to replace the traditional OAuth client credentials approach with a zero-config, secure, and scalable solution using short-lived access tokens, similar to cloud providers like AWS, Azure, and Google Cloud.

**Current Problems**:
- **High Management Overhead**: Manual creation and lifecycle management of OAuth clients.
- **Static Secrets**: Static client credentials are cumbersome to rotate, leading to security vulnerabilities.
- **Insecure Storage**: Credentials stored in plaintext across various environments.
- **Security Gaps**: Shared static API keys, lack of audit capabilities, and impractical rotation requirements create security loopholes.

**Proposal**:
- **STS-based Integration**: Leveraging OIDC standards, the STS will eliminate the need for managing static client credentials, replacing them with short-lived access tokens tied to identity providers.
- **Zero-config**: STS operates with zero configuration for client services, removing the need for OAuth client creation and secure storage.
- **Enhanced Security**: Short-lived access tokens with well-defined scopes, auditability, and automatic trust establishment for supported platforms like GCP, GitHub, and Azure.

**Architecture**:
The proposed architecture involves using ID tokens issued by trusted platforms (e.g., GitHub Actions, Google Cloud) to exchange for SAMS access tokens via the SAMS STS endpoint. This will standardize and secure inter-service communication while simplifying integration.

**Benefits**:
- Reduces OAuth credential management overhead.
- Enhances security by eliminating static credentials.
- Introduces proper audit logging and compliance with the principle of least privilege.
- Simplifies onboarding of new services and developers for secure M2M access.

**Implementation Plan**:
- Implement STS endpoint, management APIs, and necessary STS-related command-line tools.
- Update existing integrations to leverage the STS.
- Allow time-bound self-serve access to privileged APIs via tools like Entitle.
- Implement phased rollout across services with minimal downtime.

---

**Key Questions for Approval**:
1. **Security Implications**: Does the proposed STS approach sufficiently mitigate the risks associated with current OAuth static secrets? Are there any overlooked attack vectors?
2. **Adoption Barriers**: Will the transition from OAuth to STS create challenges for existing integrations? What is the level of effort involved for services to adopt STS?
3. **Backward Compatibility**: How will existing clients and systems be supported during and after the migration? Is there a rollback plan if issues arise?
4. **Operational Overhead**: Will the new system significantly reduce operational complexity? How will this be reflected in developer workflows, particularly for local development and CI/CD environments?
5. **Implementation Timeline**: Is the proposed phased timeline (total 35-42 days) feasible given existing priorities? Do we need to reprioritize resources to avoid impacting key initiatives?

Would you like further detail on any specific part of this RFC or the implementation strategy?

