# Exercise: Fun with Networks (jQuery Edition)

## Objective

Write a simple program that accesses a public JSON API and prints the results formatted in a readable way.

1. Fork the [template pen](http://codepen.io/segdeha/pen/LZNvMV) and call it something like “Fun with Networks”
1. Add jQuery to the pen using the pen settings “Quick-add” feature
1. Using [jQuery’s Ajax method](http://api.jquery.com/jQuery.ajax/), fetch JSON representing 5 randomly generated people from the following URL: [http://api.randomuser.me/?results=5](http://api.randomuser.me/?results=5)
1. Print the results something like the following:

```
Name: Mr Aventino Lima
Email: aventino.lima@example.com
Username: heavybutterfly582
Registration date: 10/2/2002
Birth date: 6/5/1994

Name: Mrs Sheryl Gardner
Email: sheryl.gardner@example.com
Username: whiteduck688
Registration date: 8/11/2014
Birth date: 6/4/1983

# Repeat for the remaining people
```

_Hint: It might help you understand the structure of the returned JSON to run it through this [pretty printer](http://jsonprettyprint.com/)._

------

## Advanced

- Format each entry as a card with the user’s photo floated to the right and the email linked, something like the following (or prettier!):

![Formatted cards](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/3.%20JavaScript/assets/formatted-cards.png?token=AAAQ0qHm3qC0ZkTXJQB8Ny5pqG9sjZwFks5Xlp0nwA%3D%3D)
