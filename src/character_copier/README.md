# Character Copier Kata

## Source

<https://www.planetgeek.ch/2010/03/31/mocking-kata-copier-net/>

## Problem Description

The Character Copier is a simple class that reads characters from a source and copies them to a destination one character at a time.

### Behavior

- When the `copy` method is called, it reads characters from the source and copies them to the destination
- The copying continues until a newline character (`\n`) is encountered
- The newline character should not be copied to the destination

### Function Signature

```python
class CharacterCopier:
    def __init__(self, source: "CharacterSource", destination: "CharacterDestination") -> None: ...
    def copy(self) -> None: ...
```

### Interface

Use the provided definitions in `kata.py` to get started.

### Testing Focus

- Implement the character copier using Test Doubles for the source and destination
- Explore different testing approaches:
  - Using Spies (manually written mocks)
  - Using a mocking framework (e.g., `unittest.mock`)

### Example Input/Output

| Input (`get_char`) | Output (`put_char`) | Notes                 |
| ------------------ | ------------------- | --------------------- |
| `'a'`              | `'a'`               | Copy single character |
| `'b'`              | `'b'`               | Copy single character |
| `'\n'`            | —                   | Stop on newline       |
