# Pair Programming

Programming consists of two related but different cognitive tasks, one strategic, the other tactical.

1. **Strategic:** How to meet the goals
1. **Tactical:** How to do the thing

Even for experienced programmers, it can be difficult to give both your full attention at any one time. In fact, most programmers constantly switch between the modes as they work.

[Pair programming](https://en.wikipedia.org/wiki/Pair_programming) is the act of two developers working together at a single workstation. This allows one to focus on the strategic while the other focuses on the tactical.

- **Navigator:** Focused on the strategic, observing, answering the question “Where are we going?”
- **Driver:** Focused on the tactical, writing the code, answering the question “How do we get there?”

> Pair programming is a social skill that takes time to learn. You are striving for a cooperative way to work that includes give and take from both partners regardless of corporate status. The best pair programmers know when to say “let’s try your idea first.” Don’t expect people to be good at it from the start.¹

## Benefits of Pair Programming

- Research shows² that because there are two sets of eyes on the problem, each bringing different experience, programs written in pairs are typically of higher quality than programs written by individuals in isolation.
- Members of the pair negotiate solutions when disagreements arise, leading a wider variety of solutions to be considered.
- Programmers who pair are constantly learning from each other.

## Drawbacks to Pair Programming

- More person hours may be involved in completing a task using pairing. (Though the research shows that this is usually offset by higher quality.)
- Talking is hard work. So take breaks!
- Some research shows³ that programmers are more creative when they enjoy “privacy, personal workspace, and freedome from interruption” (my hunch is this is more true the more experienced you are)

## How to Pair Program

- Start by discussing the problem and approach you’re going to take.
- Stay engaged (especially the navigator).
- Ask questions to clarify intent and approach.
    - “Do you think this is a valid test?”
    - “Does that look correct to you?”
    - “What’s next?”
- Make decisions together.
- Switch who is the “driver” freely and frequently.

## How to be a Good Pair Programming Partner

- Try to ask questions rather than criticize. Ask “What would happen if we did Y instead of X?” rather than declare “X sucks!”
- Criticize ideas, not people.
- Accept criticism without taking it personally. (Sometimes called [egoless programming](http://c2.com/cgi/wiki?EgolessProgramming).)
- Know when to say “let’s try your idea first.”
- Be courteous.

## How to be a Good Navigator

- Encourage your driver to [DTSTTCPW](http://c2.com/cgi/wiki?DoTheSimplestThingThatCouldPossiblyWork).
- Attempt to spot approaching pitfalls and offer gentle course corrections.
- Take responsibility for sticking to [TDD](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/4/test-driven-development.md).

## An Alternate Approach

An alternative to the driver/navigator approach to pair programming is the “ping pong” approach. This works well if you’re doing TDD. It works by having the pairing partners taking turns writing tests and making them pass.

        member 1         member 2
    --------------------------------
    write test
                     make test green
                     write next test
    make test green
    write next test
                     make test green
                     write next test

Try both! You may find that the two approaches work well for different parts of the programming process.

------

Sources:

1. [Extreme Programming](http://www.extremeprogramming.org/rules/pair.html)
1. [The Costs and Benefits of Pair Programming](http://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF) (PDF)
1. [Pair Programming Considered Harmful?](http://techcrunch.com/2012/03/03/pair-programming-considered-harmful/)
1. [PeopleSkills](http://c2.com/cgi/wiki?PeopleSkills)
1. [Effective Navigation in Pair Programming](https://www.thoughtworks.com/insights/blog/effective-navigation-in-pair-programming)
1. [How to Pair Program](http://www.wikihow.com/Pair-Program)
1. [Some thoughts on pair-programming styles](http://articles.coreyhaines.com/posts/thoughts-on-pair-programming/)
