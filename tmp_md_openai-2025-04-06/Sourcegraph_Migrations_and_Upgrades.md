# Sourcegraph Migrations and Upgrades

Created: 2024-12-18 17:25:57
Last Updated: 2024-12-18 17:26:27

### User

*[user_editable_context content]*

### User - 2024-12-18 17:25:57

Extract the information about migrations and upgrades and version numbers from this conversation

Erika RS
  5:06 PM
Thank you! I really appreciate it. I usually wouldn't waste your time explaining things to me, but in this case, I feel like it may materially impact my ability to follow up successfully


Warren
  5:14 PM
Here goes:
Sourcegraph the app only knows about specific lists of migrations to run on minor versions. For patch versions we just run whatever migrations exist at the time Sourcegraph is put together from the migrations in our migration box. This means you can always add a new migration when you're trying out new things
When you want to start sourcegraph you just run all the migrations in the box. But, there are other types of migrations -- OOB migrations which we have to apply in the background. Those need to know what some set of migrations you had in the box were at the time you want them to start, and where they need to finish being applied by before carrying on with later schema migrations. Maybe think like a passing lane. They can run along side for awhile when oncoming traffic wont mess things up, but eventually the passing lane needs to end.
So we need a map that knows when to start and stop these OOB migrations if we're going to cross multiple minor versions of the database. We build that map new on each minor release.
All in all this means that when we're changing our Sourcegraph we can make as many changes as we want and the default startup will just apply migrations, this always works between patches or a single minor version difference, but to go across the minor version we need you to manually move the db between the minor versions so that we can ensure any of the OOB migrations are applied
5:14
Hard to reduce to 5 year old
5:16
Two sentences:
Sourcegraph has a machine and a machine spirit.
The machine spirit takes awhile to connect to the body, so if you change the body too quickly the machine spirit might not easily attach back to it
(edited)
5:16
damn one more (edited) 
5:17
The machine spirit can only see sourcegraph bones, which are minor version numbers
(edited)
5:20
The TL;DR from a business operations standpoint is that the way we're doing it righ now enables us to apply migrations the same way across many deployment types, and also support easy management of development environments in relation to static versions. To change that we'd need to make pretty big architectural changes to Sourcegraph as a whole


Erika RS
  5:35 PM
Thanks! I still don't deeply get it, but this helps.
5:36
One more question (which you can ignore until tomorrow since I'm literally finishing work after I send this message): does the dependence on minor releases depend on the release number (e.g., migrations between any 5.5 series are easy even if we were to cut from main somewhere in the middle of it) or it is dependent on patch vs cutting from main (e.g., cutting from main is going to cause problems whether we call it 5.5, 5.6, or Frank)?


Warren
  8:20 PM
So the dependence is really on the minor version being incremented. It doesn't matter what branch we cut from, and when we say we're defining a minor version doesnt really matter. The code that actually applies migrations cares a lot about going across two minor versions. So if we're on v5.5 now anyone one in v5.4 can easily jump to v5.5 (any patch from and to) but as soon as we cut a minor v5.6 to get there customer must do either two upgrades in sequence (down up) or run our migrator upgrade procedure
8:20
I think that answers the question
8:21
Tthis really all makes so much more sense once you have a handle on how Sourcegraph manages version as an app :sweat_smile:
8:21
Theres just this one really important go embed that everything else falls from
8:23
but the decision to make a minor version or a patch is actually arbitrary for the most part in terms of the actual sett of migrations (from main or a release branch), the important part is that the minor releases are breaking points that help to synchronize two necessarily different data migration processes






### Assistant - 2024-12-18 17:26:15



### Assistant - 2024-12-18 17:26:15

### Extracted Information about Migrations, Upgrades, and Version Numbers

1. **Migration Types:**
   - **Schema Migrations:** Applied at startup using all migrations in the migration box for a given Sourcegraph version. This applies automatically for patches or a single minor version difference.
   - **Out-of-Band (OOB) Migrations:** Run in the background and depend on knowing the starting and stopping points for migrations across minor versions. These require careful mapping to ensure they are correctly applied in sequence.

2. **Version Dependency:**
   - Minor version upgrades require a manual process to ensure proper application of OOB migrations.
   - Patch version upgrades are straightforward, as all migrations are bundled and applied at startup.
   - The code for applying migrations is sensitive to upgrades spanning more than one minor version (e.g., skipping directly from v5.4 to v5.6 is not supported without intermediate steps).

3. **Upgrade Process:**
   - To cross multiple minor versions:
     - Perform sequential upgrades (e.g., v5.4 → v5.5 → v5.6).
     - Alternatively, use a "migrator upgrade procedure" provided by Sourcegraph.

4. **Version Number Relevance:**
   - The numbering (e.g., v5.5, v5.6) and whether a version is cut from the main branch or a release branch does not inherently matter.
   - The minor version boundary is significant because it serves as a synchronization point for schema migrations and OOB migrations.

5. **Operational Impact:**
   - The current setup supports uniform migration handling across different deployment types and simplifies managing development environments tied to static versions.
   - Significant architectural changes would be required to alter this approach.

6. **Simplified Explanation:**
   - Sourcegraph versions consist of two key elements:
     - "The machine" (the app logic and database structure).
     - "The machine spirit" (migrations and synchronization logic).
   - Rapid or large jumps in versioning (across minor versions) disrupt the alignment between these elements, requiring careful handling.

