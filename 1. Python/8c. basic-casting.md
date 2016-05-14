# Basic Casting

Python gives you ways to change the type of a value, keeping the meaning _as close as possible._ These functions are called **casting functions**.

The functions are named after the type you want:

    str(5)  #> '5'
    int('5')  #> 5
    float('5')  #> 5.0

If the meaning of the input value can’t be represented in the output type, you get an error:

    int('hello')  #> throws ValueError

Sometimes the meaning of the input is close enough and the cast works:

    int(5.5)  #> 5
