# Thinking Like a Programmer: Advanced Debugging

Use the following three ideas to help you debug stubborn issues in your code.

They might seem to make problems become longer and more complex, but **I cannot stress strongly enough** that these techniques will help you get unstuck.

## Be Aggressively Reductionist

Break every problem down into a hierarchy of _sub-problems_ until you’re at a level where the solution exists. Each of these little solutions should be _separate functions_ with explicit inputs and outputs.

- Solve the inner-most sub-problems first
- Work step-by-step up hierarchies
- Use your previous solutions as you work up

In other words, solve the “item-level” problem before the “list-level” problem.

E.g., assume you need to pick all of the years out of a list of dates. First, solve how to pick out the year from a single date and put that in a function. Then solve converting a list of dates to a list of years using the function you just wrote.

In other words, try not to put both list-level and item-level work in the same function.

Not great example:

    def get_list_of_initials_from_full_names(full_names):
        initials_list = []
        for full_name in full_names:
            first_last = full_name.split()
            initials = ''.join([name[0] for name in first_last])
            initials_list.append(initials)
        return initials_list
    
    get_list_of_initials_from_full_names(['Ada Lovelace', 'Radia Perlman'])
    
    # Returns ['AL', 'RP']

Instead, work on the item-level solution first, then use it at the list-level.

Better example:

    def get_initials_from_full_name(full_name):
        """Take a full name (e.g., 'Ada Lovelace') and
        return the initials as a string (e.g., 'AL')."""
        first_last = full_name.split()
        return ''.join([name[0] for name in first_last])
    
    def get_list_of_initials_from_full_names(full_names):
        """Take a list of names (e.g., ['Ada Lovelace',
        'Radia Perlman']) and return a list of initials
        (e.g., ['AL', 'RP'])."""
        return [
            get_initials_from_full_name(full_name)
            for full_name
            in full_names
        ]
    
    get_list_of_initials_from_full_names(['Ada Lovelace', 'Radia Perlman'])
    
    # Returns ['AL', 'RP']

## Double-Check Your Mental Model

Data is invisible unless you print it. _Print out_ the result of each individual operation to double check it is returning what you expect.

_Note: In some cases (e.g., if the problem is more about control flow than values), it’s more useful to use the debugger in PyCharm to step through the program._

- Double check that operators and library functions are behaving as you expect
- Double check _inputs,_ not just outputs; you can’t get the right answer if you’re starting with junk
- Do this on an operation-by-operation basis
- Avoid long strings of operations; assign to variables after each step to print

Is the following correct?

    def calculate_weighted_gpa(grades=[]):
        """Calculate GPA on a 4.3 scale,
        weighted by credit hours"""
        return sum(
            grade['grade']
            for grade
            in grades
        ) / len(grades)
    
    calculate_weighted_gpa(grades=[
        {
            'class': 'Calculus',
            'grade': 2.7,
            'credits': 3
        },
        {
            'class': 'History',
            'grade': 3.3,
            'credits': 2
        }
    ])
    
    # Returns 3.0



Break out each part and inspect individually.

    def calculate_weighted_gpa(grades=[]):
        """Calculate GPA on a 4.3 scale,
        weighted by credit hours"""
        
        total_grade_points = sum(grade['grade'] for grade in grades)
        # total_grade_points == 6.0
        
        number_of_classes = len(grades)
        # number_of_classes == 2
        
        return total_grade_points / number_of_classes

    calculate_weighted_gpa(grades=[
        {
            'class': 'Calculus',
            'grade': 2.7,
            'credits': 3
        },
        {
            'class': 'History',
            'grade': 3.3,
            'credits': 2
        }
    ])
    
    # Returns 3.0

Correct solution:

    def calculate_weighted_gpa(grades=[]):
        """Calculate GPA on a 4.3 scale, weighted by credit hours"""
        
        total_grade_points = sum(
            grade['grade'] * grade['credits']
            for grade
            in grades
        )
        # total_grade_points == 14.700000000000001
        
        number_of_credits = sum(
            grade['credits']
            for grade
            in grades
        )
        # number_of_credits == 5
        
        return total_grade_points / number_of_credits
    
    calculate_weighted_gpa(grades=[
        {
            'class': 'Calculus',
            'grade': 2.7,
            'credits': 3
        },
        {
            'class': 'History',
            'grade': 3.3,
            'credits': 2
        }
    ])
    
    # Returns 2.9400000000000004

## Test Isolated Pieces

Test each sub-problem (or instruction in a sub-problem) _in isolation._

- Manually run and print out results of each sub-problem (easy, since each is a separate function)
- Use input “literals” to test; avoid having to type in setup

Instead of running your whole program…

    input_str = input('Type a pig latin sentence: ')
    print(convert_sentence_to_pig_latin(input_str))

Test each part on it’s own first…

    print(convert_word_to_pig_latin('cat'))
    print(convert_word_to_pig_latin('apple'))

Then work up to testing the whole program

    print(convert_sentence_to_pig_latin('the cat jumps'))
