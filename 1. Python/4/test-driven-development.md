# Test-Driven Development

[Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) is an approach to programming where you write tests to satisfy the requirements first, then write the code to get the tests to pass.

## Benefits of TDD

Tests are like the brakes on your car. They’re what allows you go go fast!

As your programs grow more complex, you will find yourself refactoring more. If your code is well-covered with tests and the tests still pass, you can be confident you haven’t broken anything and can keep moving forward.

Developers following TDD ()compared with other testing approaches such as Test-Last) tend to…

- Write more tests
- Write testable code (which is more modular and single-responsibility)
- Catch problems earlier

## Limitations of TDD

TDD tends to apply more to code that you can unit-test (as opposed to functional-test). It therefore isn’t as effective for things like UI work or validating the correct use of external services (e.g., databases or web APIs).

Additionally, the following are concerns with testing in general:

- Tests need to be maintained as interfaces and public APIs change
- Poorly written tests may give a false sense of confidence in the codebase

## How to do TDD

1. Add the fewest, simplest tests needed to test a given requirement
1. Run your tests to see make sure the new tests fail (they _should_ fail at first!)
1. Write some code to make the tests pass
1. Run your tests again
1. Refactor the code
1. Repeat

In the course of writing a program, you will typically encounter corner cases (e.g., your program may crash when given unexpected input). When you find one of these, write a test to reproduce it _then_ write the code to correct it.
