"""GrillOven honours the Oven contract."""

from smelly_solid.lsp.oven import Oven


class GrillOven(Oven):
    def cook(self, food: str) -> None:
        print(f"Grilling {food}")  # noqa: T201
