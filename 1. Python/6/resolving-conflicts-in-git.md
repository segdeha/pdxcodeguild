# Resolving Conflicts in Git

There will be times when you merge your work to master and git won’t know how to reconcile the differences between the files that have been changed.

This is normal! And it’s usually not terribly hard to fix the conflicts.

------

The basic workflow is as follows:

1. Merge the feature branch into master (if there are conflicts, git will tell you which files are affected)
1. Go into the affected files and choose which version of the code you want to keep (git will have both versions in the file with labels to show you which is your change and which is the original version)
1. Commit the changes

------

Example:

    git branch
    * master
      feature-xyz

    <commit some changes to dice.py>

    git checkout feature-xyz
    Switched to branch 'feature-xyz'

    git branch
    * feature-xyz
      master

    <commit more changes to dice.py>

    git checkout master
    git merge feature-xyz

    Auto-merging dice.py
    CONFLICT (content): Merge conflict in dice.py
    Automatic merge failed; fix conflicts and then commit the result.

In `dice.py`, you’ll see something like the following:

    <<<<<<< HEAD
    from random import randint


    =======
    >>>>>>> feature-xyz

The part from `<<<<<<< HEAD` to `=======` is the state of the file at the head of the current branch. The part from `=======` to `>>>>>>> feature-xyz` is the state of the file on the branch being merged.

In this case, we want to delete this whole block because we moved our `import` statement to the top of the file.

    git status
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)
    You have unmerged paths.
      (fix conflicts and run "git commit")
    
    Unmerged paths:
      (use "git add <file>..." to mark resolution)
    
    	both modified:   dice.py
    
    no changes added to commit (use "git add" and/or "git commit -a")

We have fixed the file and now need to tell git that the conflict has been resolved.

    git add dice.py
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)
    All conflicts fixed but you are still merging.
      (use "git commit" to conclude merge)
    
    Changes to be committed:
    
    	modified:   dice.py

The conflict has been resolved. All that’s left to do is commit the resolution.

    git commit -m "Fixed merge conflict in dice.py"
    [master 1530e40] Fixed merge conflict in dice.py

    git status
    On branch master
    Your branch is ahead of 'origin/master' by 3 commits.
      (use "git push" to publish your local commits)

------

Sources:

1. [Nice answer on Stack Overflow with some advanced merge conflict tips](http://stackoverflow.com/a/7589612/11577)