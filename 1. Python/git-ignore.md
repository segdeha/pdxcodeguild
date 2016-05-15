# Git Ignore

A **Git Ignore** file is a list of file names for Git to ignore and not track. It lives in a file named `.gitignore` in your repository. Its rules apply to all directories that are siblings of or children of the directory in which it sits.

Each line in the file is a pattern to match.
You can use `#` comments.

    *.txt # Ignore all files ending in .txt
    notes # Ignore all files or directories named notes anywhere
    /root_notes # Ignore a file named root_notes in the repo root

Files and directories that match will not show up when you run `git status` in your repository root.

------

The following is a good starting point for your own `.gitignore` file:

    .DS_Store # applies only to OS X
    .gitignore # ignore the .gitignore file!
    node_modules # directory where npm stores packages
    *.pyc # compiled python files
    __pycache__ # pre-parsed python
    db.sqlite3 # Django default database
