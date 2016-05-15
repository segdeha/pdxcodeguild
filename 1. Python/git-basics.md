# Git Basics

[Git](https://git-scm.com) is a widely-used and great source control system.

Git calls the directory it’s tracking all changes in a **repository**.

Git stores timestamped snapshots of the state of the repo called **commits**:

    commit 6aeba8f3f2c386e4dc97fd3e0b8fbfee8d751ac5
    Author: David Selassie <david@pdxcodeguild.com>
    Date:   Tue Mar 29 16:29:27 2016 -0700

Each commit has a globally unique **hash,** an author, a timestamp, a description of what changed, and a **parent** commit. Each commit stores the exact changes made to the files from the last commit.

Commits build on top of each other to form a **history,** the full record of all snapshots of a project:

    Time --->
    C1 - C2 - C3 - C4
                    |
                    HEAD

The most recent commit is called the `HEAD`.

Git gives you a suite of command line tools. All commands below are run from within the repository directory.

------

## Making a Directory a Repo

To turn the current working directory into a Git repo and have Git track all changes in it:

    git init

This will make an invisible `.git` directory. Don’t touch anything in it or delete it. It contains the repo’s history.

------

## Committing Changes

Committing is the process of saving changes in the working directory.

    git add my_awesome_file.txt
    git commit -m "My awesome commit"

### Commit Messages

If you forget to add `-m` when you commit, you might be thrown into a terminal text editor called Vim that’s very confusing.
Don’t panic. Press escape. Type `:q!`. Press enter.

That should quit the editor and you can run `git commit` again and not forget the `-m "MESSAGE"`.

You can [change the default editor for commit messages](https://help.github.com/articles/associating-text-editors-with-git/) to something more friendly, even Atom!

------

## Status

If you’re ever not sure what’s going on, run:

    git status

This will give you a summary of all the files Git knows about and whether they’ve changed, been staged, or haven’t been added in any commits yet.

------

## Viewing Changes

You can see the difference between the last commit and your working directory using the `diff` command.

    git diff

------

## Viewing History

You can get a list of your commit history using the `log` command.

    git log

------

## Basic Workflow

If you’re the only person working on a repo just on your computer, you can use the following, simple workflow:

1. Make changes to the working directory using your editor
1. Stage those changes in the index using `git add .`
1. Commit the staged changes in the index to your local history using `git commit -m "MESSAGE"`

------

## Advanced Workflow

Later in the class we will learn about pushing code to remote repositories to enable collaboration.