# Git Ignore

A **Git Ignore** file is a list of file names for Git to ignore and not track. It lives in a file named `.gitignore` in your repository. Its rules apply to all directories that are siblings of or children of the directory in which it sits.

Each line in the file is a pattern to match.
You can use `#` comments.

    # Ignore all files ending in .txt
    *.txt
    # Ignore all files or directories named notes anywhere
    notes
    # Ignore a file named root_notes in the repo root
    /root_notes

Files and directories that match will not show up when you run `git status` in your repository root.

------

The following is a good starting point for your own `.gitignore` file:

    # applies only to OS X
    .DS_Store
    # ignore the .gitignore file!
    .gitignore
    # directory where npm stores packages
    node_modules
    # compiled python files
    *.pyc
    # pre-parsed python
    __pycache__
    # Django default database
    db.sqlite3
    # PyCharm project directory
    .idea
