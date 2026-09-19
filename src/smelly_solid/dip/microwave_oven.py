"""MicrowaveOven demonstrating a Dependency Inversion Principle violation."""

from smelly_solid.dip.microwave_generator import MicrowaveGenerator


# DIP violation: MicrowaveOven news up a concrete MicrowaveGenerator
# itself instead of depending on an injected abstraction.
class MicrowaveOven:
    def __init__(self) -> None:
        self._heater = MicrowaveGenerator()

    def cook(self) -> None:
        self._heater.generate()
