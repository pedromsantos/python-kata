"""Chef selects how to cook depending on the oven it receives."""

from smelly_solid.lsp.microwave import Microwave
from smelly_solid.lsp.oven import Oven


# The isinstance special-case here is the diagnostic signature of the
# LSP violation in Microwave: a caller that can't just trust Oven.cook().
class Chef:
    def cook(self, oven: Oven, food: str) -> None:
        if isinstance(oven, Microwave):
            oven.cook_microwaving(food)
        else:
            oven.cook(food)
