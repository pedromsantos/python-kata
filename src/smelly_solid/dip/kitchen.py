"""Kitchen demonstrating a Dependency Inversion Principle violation."""

from smelly_solid.dip.microwave_oven import MicrowaveOven


# DIP violation: Kitchen (high-level policy) directly constructs a
# concrete MicrowaveOven (low-level detail) -- it can't work with any
# other kind of oven.
class Kitchen:
    def __init__(self) -> None:
        self._oven = MicrowaveOven()

    def cook_dinner(self) -> None:
        self._oven.cook()
