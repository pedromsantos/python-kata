"""Location and Car demonstrating a Single Responsibility Principle violation."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Location:
    lat: float
    lng: float


# SRP violation: Car mixes domain behaviour (mileage/travel) with a
# persistence concern (save) -- two different reasons to change bundled
# into one class.
class Car:
    def __init__(self) -> None:
        self._mileage = 0
        self._location = Location(lat=0, lng=0)

    def current_mileage(self) -> int:
        return self._mileage

    def travel_to(self, location: Location) -> None:
        self._location = location
        self._mileage += 1

    def save(self) -> None:
        row = json.dumps({"mileage": self._mileage, "location": asdict(self._location)})
        Path("/tmp/car.json").write_text(row)  # noqa: S108
