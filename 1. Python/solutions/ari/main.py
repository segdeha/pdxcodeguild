"""Read in a file and output its automated readability index."""

from os import listdir
from math import ceil
from time import sleep

"""

Control flow:

1. Read names of files in the current directory that end in `.txt`
2. Present files to user as a numbered menu to choose from (or enter to quit)
3. Compute the ARI (https://en.wikipedia.org/wiki/Automated_readability_index)
4. Output the result
5. GOTO 2

"""

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


def compute_ari(contents):
    """Compute the automated readability index of a string.

    Expected scores validated at http://www.webpagefx.com/tools/read-able/

    1. One really long word (34 characters):

    >>> compute_ari('supercalifragilisticexpialidocious')
    140

    2. 7 short words, all 3 characters long:

    >>> compute_ari('bad men can try but not win')
    -3

    3. Sentence of 3 of the smallest possible words:

    >>> compute_ari('i o u')
    -15

    """

    # replace all newlines with spaces
    contents = ' '.join(contents.split("\n"))

    # find the sentences
    sentences = contents.split('. ')

    # find the words
    words = [word for sentence in sentences for word in sentence.split(' ') if word != '']

    # find the number of characters in each word
    characters = [len(word) for word in words]

    # calculate the ari
    return ceil((4.71 * (sum(characters) / len(words))) + (0.5 * (len(words) / len(sentences))) - 21.43)


def get_file_contents(name_of_file):
    """Return the contents of the given file as a string."""

    with open(name_of_file, 'r') as f:
        contents = f.read()
    return contents


def create_prompt(files):
    """Given a list of filenames, return a formatted prompt string."""

    menu_of_files = ''
    for i in range(len(files)):
        menu_of_files += """{menu_number}) {filename}\n""".format(
            filename=files[i],
            menu_number=(i + 1)
        )
    prompt = """
To compute its automated readability index,
pick from one of the files below:

{menu_of_files}
or

q) Quit
""".format(
        menu_of_files=menu_of_files
    )
    return prompt


def main():
    files = [f for f in listdir('.') if f.endswith('.txt')]
    error_message = '\nPlease input a number between 1 and {}.'.format(len(files) - 1)
    while True:
        print(create_prompt(files))
        choice = input()
        if choice == 'q' or choice == '':
            print('Goodbye!')
            break
        else:
            try:
                choice = int(choice)
            except ValueError:
                print(error_message)
                sleep(1)
                continue
            if 0 < choice <= len(files):
                filename = files[choice - 1]
                ari = compute_ari(get_file_contents(filename))
                ari_key = 14 if ari > 14 else ari
                print("""
--------------------------------------------------------

The ARI for the file, {filename}, is {ari}.
This corresponds to a {grade_level} level of difficulty
that is suitable for an average person {ages} years old.

--------------------------------------------------------""".format(
                    filename=filename,
                    ari=ari,
                    grade_level=ari_scale[ari_key]['grade_level'],
                    ages=ari_scale[ari_key]['ages']
                ))
                sleep(1)
                if 'y' == input('\nTry again? (y/n) '):
                    continue
                else:
                    break
            else:
                print(error_message)
                sleep(1)
            continue

if __name__ == '__main__':
    from doctest import testmod

    testmod()
    main()
