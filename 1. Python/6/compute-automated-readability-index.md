# Exercise: Compute Automated Readability Index

The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text.

------

## Automated Readability Index Formula

The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

In plain English, the score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up.

Scores correspond to the following ages and grad levels:

    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College

------

## Objective

Compute the ARI for some text loaded in from a file.

1. Create a new directory called `ari` in your code repo
1. Create a file called `main.py` file in the `ari` directory
1. Download the following files to your `ari` directory:
    - [geneology-of-morals.txt](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/1.%20Python/solutions/ari/geneology-of-morals.txt?token=AAAQ0iIWwUkVVY9qXnLdltRGDUI6TtjZks5XWdDdwA%3D%3D)
    - [gettysburg-address.txt](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/1.%20Python/solutions/ari/gettysburg-address.txt?token=AAAQ0n7jSNNNtENrA1c-WeAS3tvussbtks5XWdGGwA%3D%3D)
    - [jack-and-jill.txt](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/1.%20Python/solutions/ari/jack-and-jill.txt?token=AAAQ0g6lXHjuUsJxW2ZcFELjH72pHcXfks5XWdGewA%3D%3D)

When the user runs `main.py`, they should be presented with a menu of choices of the above files to choose from that looks something like the following:

    To compute its automated readability index,
    pick from one of the files below:

    1) geneology-of-morals.txt
    2) gettysburg-address.txt
    3) jack-and-jill.txt

    or

    q) Quit

The list of files should be generated from the files in the `ari` directory that have `.txt` for their extension.

After choosing one of the files, the output should look something like the following:

    --------------------------------------------------------

    The ARI for the file, gettysburg-address.txt, is 12.
    This corresponds to a 11th Grade level of difficulty
    that is suitable for an average person 16-17 years old.

    --------------------------------------------------------

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level:

    ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
