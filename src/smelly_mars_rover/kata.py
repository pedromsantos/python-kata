# pylint: skip-file
# ruff: noqa: PLR2004, S311, T201, UP017
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Protocol


class MissionClock:
    @staticmethod
    def now() -> str:
        return datetime.now(timezone.utc).isoformat()


class RadioTransmitter:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def send(self, message: str) -> None:
        print(f"[RADIO -> {self.endpoint}] {message}")


class ObstacleSensor:
    def __init__(self) -> None:
        self.obstacles = ["1,2", "3,3", "0,4"]

    def detects_obstacle_at(self, x: int, y: int) -> bool:
        sensor_noise = random.random() < 0.0001
        return sensor_noise or f"{x},{y}" in self.obstacles


@dataclass
class Position:
    x: int
    y: int


class Rover:
    def __init__(self, x: int, y: int, direction: str, grid_size: int) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_size = grid_size
        self.sensor = ObstacleSensor()
        self.radio = RadioTransmitter("mission-control.nasa.gov")

    def execute(self, commands: str) -> str:
        for command in commands:
            previous = Position(x=self.x, y=self.y)

            if command == "L":
                self._turn_left()
            elif command == "R":
                self._turn_right()
            elif command == "M":
                self._move_forward()

            if self.sensor.detects_obstacle_at(self.x, self.y):
                self.x = previous.x
                self.y = previous.y
                self._report_obstacle()
                return f"O {self.x} {self.y} {self.direction}"

        return f"{self.x} {self.y} {self.direction}"

    def _report_obstacle(self) -> None:
        self.radio.send(f"OBSTACLE {self.x} {self.y} {self.direction} at {MissionClock.now()}")

    def _turn_left(self) -> None:
        order = ["N", "W", "S", "E"]
        self.direction = order[(order.index(self.direction) + 1) % 4]

    def _turn_right(self) -> None:
        order = ["N", "E", "S", "W"]
        self.direction = order[(order.index(self.direction) + 1) % 4]

    def _move_forward(self) -> None:
        if self.direction == "N":
            self.y = (self.y + 1) % self.grid_size
        elif self.direction == "S":
            self.y = (self.y - 1 + self.grid_size) % self.grid_size
        elif self.direction == "E":
            self.x = (self.x + 1) % self.grid_size
        elif self.direction == "W":
            self.x = (self.x - 1 + self.grid_size) % self.grid_size


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def equals(self, other: "Coordinate") -> bool:
        return self.x == other.x and self.y == other.y


class TelemetryPort(Protocol):
    def record(self, entry: str) -> None: ...


class CommandTranslator:
    last_language = "EN"

    def translate(self, command: str, language: str) -> str:
        CommandTranslator.last_language = language

        if language == "EN":
            return command
        if language == "ES":
            return self._translate_spanish(command)
        if language == "FR":
            return self._translate_french(command)
        if language == "PT":
            return self._translate_portuguese(command)
        if language == "IT":
            return self._translate_italian(command)

        return command

    def translate_sequence(self, commands: str, language: str) -> str:
        result = ""
        for command in commands:
            result += self.translate(command, language)
        return result

    def get_last_language_used(self) -> str:
        return CommandTranslator.last_language

    def _translate_spanish(self, command: str) -> str:
        if command == "I":
            return "L"
        if command == "D":
            return "R"
        if command == "A":
            return "M"
        return command

    def _translate_french(self, command: str) -> str:
        if command == "G":
            return "L"
        if command == "D":
            return "R"
        if command == "A":
            return "M"
        return command

    def _translate_portuguese(self, command: str) -> str:
        if command == "E":
            return "L"
        if command == "D":
            return "R"
        if command == "A":
            return "M"
        return command

    def _translate_italian(self, command: str) -> str:
        if command == "S":
            return "L"
        if command == "D":
            return "R"
        if command == "A":
            return "M"
        return command


class MissionLog:
    def __init__(self, translator: CommandTranslator, telemetry: TelemetryPort) -> None:
        self.translator = translator
        self.telemetry = telemetry

    def log_translated_sequence(self, commands: str, language: str) -> str:
        translated = self.translator.translate_sequence(commands, language)
        self.telemetry.record(f"{language}:{commands}->{translated}")
        return translated
