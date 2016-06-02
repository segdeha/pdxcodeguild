# Exercise: Compute Automated Readability Index

The automated readability index (ARI) is a simple formula for computing the U.S. grade level for a given block of text.

## Objective

Compute the ARI for some text loaded in from a file.

1. Create a new directory called `ari` in your code repo
1. Create a `main.py` file in the `ari` directory for your program
1. 
1. 
1. 

------

The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

In plain English, the score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up.

Scores correspond to the following ages and grad levels:

    Score	Age     Grade Level
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


