## git reset command to revert the last change
`git reset --soft HEAD~1`

## to show the branches graphically
`git log --graph --decorate`

## To view all the branches- both local and remote 
`git branch -a`

## To edit the most recent commit message, you can use the --amend option with the git commit command. 
`git commit --amend -m "new commit msg"`
## Fast Forward
A "fast-forward merge" and a "no-fast-forward merge" are two different methods for integrating changes from one branch into another in Git. 
A fast-forward merge occurs when Git is able to move the branch pointer of the target branch (usually the branch you're merging into) to directly 
point to the same commit as the source branch (the branch you're merging from). In other words, there are no new commits created, and the history appears linear.

## Nff or Recursive strategy
A no-fast-forward merge creates a new merge commit to integrate changes from the source branch into the target branch. This merge commit has two parent commits, 
one from the target branch and one from the source branch, signifying that a merge operation occurred.

Use fast-forward merges for simpler, linear histories and no-fast-forward merges when you want to preserve the full history of the source branch and indicate when the merge occurred
