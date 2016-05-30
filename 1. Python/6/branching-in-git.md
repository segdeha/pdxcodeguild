# Branching in Git

Branches are one of the most powerful features of git. They’re what enable experimentation and parallel workflows within a complicated codebase.

Up to now, we’ve been working exclusively on the “master” branch. Master is the default branch when you set up a new project. Many development teams use master to represent the working version of the code.

In other words, new features and bug fixes happen on branches and are merged into master when the team is confident the new code is working and is not going to break existing functionality.

------

## Create a New Branch

Creating a new branch in git is as easy as doing the following:

    git branch <new-branch-name>

This creates a new branch that exactly mirrors the _currently checked-out_ branch. In other words, if you want a copy of `master`, make sure you have `master` checked out before you create the new branch.

------

## Create a New Branch from a Specific Commit

You can also create a new branch based on the history as it was at a particular commit by specifying the commit hash when you create the branch.

Example:

    git branch <new-branch-name> <sha1-hash>

Another options is to specify that you want to create a branch from a certain number of commits back in the history.

Example:

    git branch <new-branch-name> HEAD~<n>

------

## Switching Between Branches

At any time, you can see what branches exist by doing the following:

    git branch

To change to another branch, you do the following:

    git checkout <existing-branch-name>

You can also create a branch and switch to it in one operation.

Example:

    git checkout -b <new-branch-name>

------

## Merging Branches

A typical workflow is to do work on a branch (bug fix, new feature, refactor), send the branch to colleagues for a code review, then merge the code into the master branch.

When your work is ready to merge, you can do that by doing the following:

    git checkout <branch-to-be-merged>
    git merge master

_Note: Technically, you can merge from any branch to any other branch. It can get confusing fast, so my recommendation is to have everyone on the team merging back to master unless there’s a really good reason to do otherwise._

------

## Deleting Branches

As long as all work on the branch has been merged into master, you can delete your feature branches by doing the following:

    git branch -d <existing-merged-branch-name>

If your branch contains commits that you don’t want to merge back to master (e.g., you did some experimentation but it didn’t work out as you’d hoped), you can force git to delete the branch by using the `-D` option.

Example:

    git branch -D <existing-unmerged-branch-name>
