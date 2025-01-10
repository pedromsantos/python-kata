# Guild Raid kata

## First run

- Write tests to characterize the code as is

You will soon realize that it's very hard to write tests for this code due to the usage of static methods. Once you gave it a good try at writing characterization tests read the section below and try again.

### Breaking dependencies using a seam

Legacy Code requires extra care than code written with tests. Here, the first goal is to put the tests in place. In this context, Michael Feathers introduced the concept of “seam”. “A seam is a place where you can alter behavior in your program without editing in that place.”

types of seams:

- Pre-Processing seams: where we can inject behavior when a pre-processor runs
- Link seams: intercepting calls to external files at link time and replacing them with injectable behavior
- Object seams: when dealing with Object Oriented languages, we can use polymorphism or other techniques to change the behavior at (test) runtime

#### Using inheritance to decouple production code

In the following example, we will see one application of the seam model to some code snippets. We informally call this "_the mother of all refactoring_" (for legacy code), because it depicts very well the main underlying idea.

_Example:_

```python

class Game:
    def play(self):
        import random
        dice_result = random.randint(1, 6)
        # ... other game logic ...

```

In this case, the Game class is coupled with the random number generator library. We need to control the dice rolling to test the Game class.

**Step 1:** Add a method to the Game class to encapsulate the behavior that has the Coupling issue.

```python

class Game:
    def play(self):
        dice_result = self.roll()
        # ... other game logic ...

    def roll(self):
        import random
        return random.randint(1, 6)
```

**Step 2:** In your _test code_, inherit from the Game class and change the behavior of the method `Roll` to something you have control over.

```python

class TestableGame(Game):
    def __init__(self, desired_roll):
        self.roll = desired_roll

    def roll(self):
        return self.roll
```

**Step 3:** Write a test using the TestableGame class.

```python

class GameShould:
    def test_do_something_when_a_six_is_rolled(self):
        game = TestableGame(6)

        game.play()

        #ASSERT
```

This technique can also work when a class calls static methods. The main advantage of this technique is that it can be performed by the IDE using automated refactoring only. That reduces the manual changes to production code and the risk of introducing bugs.

With good test coverage, you can refactor the Game class. You can completely remove the need for a seam, by injecting the dependency in the Game class, for example.

Here, in terms of design, the seam makes things worse. But the goal is to have tests. And once we have them, we can then proceed with the refactoring of the design and make things better!

## Second run

- Refactor the code to remove design issues
