# Imperative Programming

The kinds of programs you write in Python are **imperative**:
you have to give the computer explicit instructions for how to do work.

Your `.py` file is the list of explicit instructions. Each line is a **statement** or one instruction. Python runs each statement one at a time from top to bottom.

To move information from one statement to another, you save values in variables:

    miles = 300
    miles_per_gallon = 30
    cost_per_gallon_of_gas = 2.50
    
    gallons_needed = miles / miles_per_gallon
    road_trip_cost = gallons_needed * cost_per_gallon_of_gas

The list of previously-stored variables that you can access is called the **current scope**.

All of your variable and function names must have values by the time the code runs. Thus, you can only access values that you’ve stored previously. You can’t look into the future.
