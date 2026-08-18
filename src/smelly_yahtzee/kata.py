# pylint: skip-file
import random
from typing import Protocol


class Die:
    def __init__(self, value: int) -> None:
        self.value = value

    def equals(self, other: "Die") -> bool:
        return self.value == other.value


class TelemetryPort(Protocol):
    def record(self, entry: str) -> None: ...


class DiceCup:
    def __init__(self, random_source=random.random) -> None:
        self.random_source = random_source
        self.dice: list[Die] = []
        self.selected_indexes: list[int] = []

    def roll(self) -> list[Die]:
        self.dice = [self._roll_die() for _ in range(5)]
        self.selected_indexes = []
        return self.dice

    def select_for_reroll(self, indexes) -> None:
        self.selected_indexes = list(indexes)

    def reroll_selected(self) -> list[Die]:
        for index in self.selected_indexes:
            self.dice[index] = self._roll_die()
        self.selected_indexes = []
        return self.dice

    @property
    def current_dice(self) -> list[Die]:
        return self.dice

    def _roll_die(self) -> Die:
        return Die(int(self.random_source() * 6) + 1)


class TurnLog:
    def __init__(self, dice_cup: DiceCup, telemetry: TelemetryPort) -> None:
        self.dice_cup = dice_cup
        self.telemetry = telemetry

    def reroll_selected_dice(self) -> list[Die]:
        dice = self.dice_cup.reroll_selected()
        self.telemetry.record(f"rerolled:{','.join(str(die.value) for die in dice)}")
        return dice
