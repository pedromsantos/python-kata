# Anagrams Kata

## Problem Description

Write a function that generates all possible anagrams (permutations) of an input string.

### Function Signature

```python
def anagrams(word: str) -> list[str]:
    ...
```

### Example

For the input: `"abc"`

The potential anagrams are:

- abc, acb, bac, bca, cab, cba

For the input: `"aab"`

The potential anagrams are:

- aab, aba, baa

## TDD Rules

1. ✅ Write production code only to pass a failing unit test
2. ✅ Write only enough of a unit test to make it fail
3. ✅ Write only enough production code to make the failing test pass

## Edge Cases to Consider

- Empty string `""` → should return `[""]` or `[]`
- Single character `"a"` → should return `["a"]`
- String with duplicate characters `"aab"` → avoid duplicate results
- Long strings — consider efficiency

## Resources

- [Test Desiderata by Kent Beck](https://kentbeck.github.io/TestDesiderata)
