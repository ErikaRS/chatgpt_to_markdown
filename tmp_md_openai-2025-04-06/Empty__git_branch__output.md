# Empty `git branch` output

Created: 2024-05-15 08:17:06
Last Updated: 2024-05-15 08:17:15

### User - 2024-05-15 08:17:06

Does `git branch` show anything if nothing is checked in

### Assistant - 2024-05-15 08:17:14



### Assistant - 2024-05-15 08:17:14

The `git branch` command is used to list all the local branches in your repository. If you've initialized a new Git repository using `git init` but haven't yet created any branches or commits, `git branch` will not show any output because there are no branches to list.

However, even if you haven't explicitly created a branch, there's usually a default branch automatically created by Git, typically named `master` or `main`, depending on your Git configuration. This default branch will appear in the list once you make your first commit. Before making any commits, `git branch` might not list anything, but as soon as you make a commit, the default branch will be shown.

