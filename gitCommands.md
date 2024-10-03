## git reset command to revert the last change
`git reset --soft HEAD~1`

## to show the branches graphically
`git log --graph --decorate`

## To view all the branches- both local and remote 
`git branch -a`

## To edit the most recent commit message, you can use the --amend option with the git commit command. 
`git commit --amend -m "new commit msg"`

### What is a Merge?
Merging is the process of combining the changes from one branch (usually a feature branch) into another branch (often main or master).
It keeps the history of both branches intact and creates a new merge commit when the two branches are joined.
### Types of Merge:
## Fast-Forward Merge:
If the target branch (e.g., main) has no new commits since the feature branch was created, Git can simply move the main branch pointer forward to the latest commit in the feature branch.
No new commit is created; it's as if the changes were made directly on main.
## Three-Way Merge (No-Fast-Forward Merge) or Recursive strategy:
This occurs when both the main branch and the feature branch have diverged, meaning they each have unique commits.
Git looks for the common ancestor of the two branches, combines the changes, and creates a merge commit that reflects the merging of the two branches.
A no-fast-forward merge creates a new merge commit to integrate changes from the source branch into the target branch. This merge commit has two parent commits, 
one from the target branch and one from the source branch, signifying that a merge operation occurred.
Use fast-forward merges for simpler, linear histories and no-fast-forward merges when you want to preserve the full history of the source branch and indicate when the merge occurred
### Git Rebase
### What is a Rebase?
Rebasing takes the commits from one branch (e.g., a feature branch) and reapplies them on top of another branch (e.g., main), as if the feature branch was based directly on the latest state of the target branch.
This results in a linear commit history, without merge commits.
### How Rebasing Works:
Git temporarily removes the commits from the current branch.
It then updates the current branch to match the target branch.
Finally, it replays the removed commits on top of the updated branch.

Rebase is generally discouraged for shared branches (like main or develop), 
because it changes commit history, which can cause issues for other contributors.
### The golden rule of git rebase is to never use it on public branches.
