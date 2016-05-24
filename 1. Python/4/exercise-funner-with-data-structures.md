# Funner With Data Structures

## Objective

Building on our NFL teams exercise, we are going to take it to the next level by refactoring the program to handle different datasets, loaded from an external file.

_Note: This is a pair programming exercise. Work together!_

## Setup

1. One person in your pair should create a new **repo** called `data-finder` then add the other person in the pair as a collaborator. (We’re creating a new repo so you can better collaborate with your pairing partner.)
1. Clone the repo to your local machine. (Your pair partner should do the same.)
1. In the `data-finder` directory that was created when you cloned the repo, create a new file called `main.py`
1. Save [data.json](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/1.%20Python/solutions/data-finder/data.json?token=AAAQ0k1TdEbLQESpTgUEhlRgABnfI10Gks5XSzP9wA%3D%3D) to the `data-finder` directory as `data.json`

## New Requirements

-  Load your data from the `data.json` file using what we covered in [File I/O](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/4/file-io.md) and [JSON](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/4/json.md)
-  Notice that the data structure has categories at the top level
    -  Write your program in such a way that you could add additional categories and it would still work (e.g., ‘Comics’ in addition to or instead of ‘Food’, ‘Football’, and ‘Movies’)
- Notice that within each category there are `data` and `strings` dictionaries
    -  Use the `strings` dictionary for user prompts and output where you can (this allows for customization of the user interface to fit the data as well as the possibility of localizing the content for different languages)
- Start by prompting the user for the category they want to explore
- Have the program start over if the user enters input the program doesn’t understand
- Allow the user the option of starting again once an answer is found

## Advanced

- The requirements above specify to go all the way back to the beginning of the program if the user gives us unexpected input. A better user experience would be not to lose the input they’ve given us to that point (i.e. category, top-level key, etc.). Modify your program to jump them back to the appropriate place in the user flow without losing their previous valid input.
- The NFL dataset allowed us to assume that each item in the several lists was unique to the dataset. The new dataset includes some of the same ingredients in more than one dish as well as the same actor in more than one movie. Change your program to return a list of results when there are matches in multiple lists.
- Cover as much of your program with tests as possible. One technique that allows for this without cluttering up your function definitions is to put tests together in a `__test__` variable near the top of the file. You could also put your tests in an external file.
- Add your own dataset. Be creative!
