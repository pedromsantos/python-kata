# Tic Tac Toe kata

## Rules

- The game is played on a grid that's 3 squares by 3 squares
- Players alternate placing X's and O's in empty squares
- X always plays first
- Players cannot play on a played square
- A Player wins when it has three squares in a row
  - Horizontally
  - Vertically
  - Diagonally
- If all nine squares are filled and neither player has won, the game is a draw

## Follow TDD rules strictly

1. ✅ Write production code only to pass a failing unit test
2. ✅ Write only enough of a unit test to make it fail
3. ✅ Write only enough production code to make the failing test pass

## First run

Implement Tic Tac Toe as best as you can using TDD.

## Second run

Implement Tic Tac Toe strictly applying object calisthenics rules.

### Object Calisthenics Rules

1. **Wrap all primitives and strings** — Wrap primitives in a type, especially if it has behaviour or it's an important domain concept
2. **First class collections** — Wrap collections in a type, especially if it has behaviour
3. **One dot per line** — Do not write `dog.Body.Tail.Wag()`, write `dog.ExpressHappiness()` (Law of Demeter)
4. **No getters/setters** — TELL, DON'T ASK!
5. **No classes with more than two instance variables**
6. **Only one level of indentation per method**
7. **Don't use the ELSE keyword**
8. **Don't abbreviate names**
9. **Keep all entities small** — 10 files per package, 50 lines per class, 5 lines per method, 2-3 arguments per method

## Resources

- [Object Calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/)
- [Learn These 9 Rules to Start Writing Clean Code Immediately](https://levelup.gitconnected.com/learn-these-9-rules-to-start-writing-clean-code-immediately-a7ee40fe1e1b)
