"""Module-level singleton demonstrating Connascence of Identity."""


# Connascence of Identity: correctness of every consumer depends on
# them all sharing this exact single module-level instance -- there is
# no way to have two independent counters, and the dependency is
# invisible from any one consumer's own code.
class _Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> int:
        self.value += 1
        return self.value

    def current(self) -> int:
        return self.value


global_counter = _Counter()
