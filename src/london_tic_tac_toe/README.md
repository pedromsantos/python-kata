# Tic Tac Toe kata

## Rules

- X always plays first
- Players alternate placing X’s and O’s on the board
- Players cannot play on a played position
- A Player wins when it has three in a row
  - Horizontally
  - Vertically
  - Diagonally
- If all nine squares are filled and neither player has won, the game is a draw

In this version of TicTacToe nothing is returned but a call to an Output is made to print the game events.

Use the type definitions in `kata.py` to get started.

## TDD Rules

1. ✅ Write production code only to pass a failing unit test
2. ✅ Write only enough of a unit test to make it fail
3. ✅ Write only enough production code to make the failing test pass

## First run

Implement Tic Tac Toe using the provided type definitions. Focus on making the game logic work.

## Second run

Refactor the implementation applying the [Transformation Priority Premise](https://kentbeck.github.io/tpp/) to evolve your code from simple to elegant.

## Third run

Apply [Object Calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/) rules:

- Wrap all primitives and strings
- First class collections
- One dot per line (Law of Demeter)
- No getters/setters — Tell, Don't Ask!
- No classes with more than two instance variables
- Only one level of indentation per method
- Don't use the ELSE keyword
