"""Microwave demonstrating a Liskov Substitution Principle violation."""

from smelly_solid.lsp.oven import Oven


# LSP violation: Microwave can't honour Oven's cook() contract, so it
# raises instead -- callers that only know about Oven get a broken promise.
class Microwave(Oven):
    def cook(self, food: str) -> None:
        msg = "Microwave does not support cook(); use cook_microwaving() instead"
        raise NotImplementedError(msg)

    def cook_microwaving(self, food: str) -> None:
        print(f"Microwaving {food}")  # noqa: T201
