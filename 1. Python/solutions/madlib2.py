
input_plural_pronoun = input('Give me a plural pronoun: ')
input_one = input('Give me a noun: ')
input_two = input('Give me an adjective: ')
input_three = input('Give me a noun: ')

my_mad_lib = '''This is the {one} I am using. It is {two}, {two} text.

If you do not like my {three}, you can make your own.

{plural_pronoun} are the nicest people ever. {plural_pronoun} like pie.
'''

my_transformed_mad_lib = my_mad_lib.format(
    one=input_one,
    two=input_two,
    three=input_three,
    plural_pronoun=input_plural_pronoun
)

print(my_transformed_mad_lib)
