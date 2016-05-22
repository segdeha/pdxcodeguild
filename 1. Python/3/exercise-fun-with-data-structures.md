# Fun With Data Structures

## Objective

Prompt the user with something like the following:

    Enter the name of either a conference or team:

If the user enters the name of a conference (either ‘AFC’ or ‘NFC’), prompt them for a division (‘East’, ‘North’, ‘South’, or ‘West’) and print out the names of the corresponding teams.

If the user enters the name of a team, print out the corresponding conference and division (e.g., if the user enters ‘Seattle Seahawks’, print ‘NFC West’).

If the user enters input that doesn’t match your data, prompt them again.

1. Open Atom or PyCharm
1. Create a file named `nflteams.py`
1. Think through the problem in terms of the following:
    1. Setup
    1. Input
    1. Transform
    1. Output
1. Stub out functions to handle small, discrete parts of the larger problem
    - Bonus: For your pure functions, write doctests to ensure they work as expected

------

## Key Concepts

- Data structures
- Comparison operators

## Data

You will need to put the following data into a data structure that allows you to access it using the input you expect from the user:

    AFC
        East
            Buffalo Bills
            Miami Dolphins
            New England Patriots
            New York Jets
        North
            Baltimore Ravens
            Cincinnati Bengals
            Cleveland Browns
            Pittsburgh Steelers
        South
            Houston Texans
            Indianapolis Colts
            Jacksonville Jaguars
            Tennessee Titans
        West
            Denver Broncos
            Kansas City Chiefs
            Oakland Raiders
            San Diego Chargers
    NFC
        East
            Dallas Cowboys
            New York Giants
            Philadelphia Eagles
            Washington Redskins
        North
            Chicago Bears
            Detroit Lions
            Green Bay Packers
            Minnesota Vikings
        South
            Atlanta Falcons
            Carolina Panthers
            New Orleans Saints
            Tampa Bay Buccaneers
        West
            Arizona Cardinals
            Los Angeles Rams
            San Francisco 49ers
            Seattle Seahawks

## Extra Credit

If you get through the basic assignment and want to push yourself, try one or more of the following:

- Make your program work with another layer of data (e.g., players on each team)
- Make your program resilient to missing data (e.g., delete the teams from the AFC East [Sorry, Pats fans!])
- Make your program work with a different data set altogether (e.g., Cuisines/Dishes/Ingredients)
