"""IAmACar interface demonstrating an Interface Segregation Principle violation."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Location:
    lat: float
    lng: float


# ISP violation: gasoline and electric refuelling are mutually exclusive
# capabilities bundled into one fat interface -- no single car honestly
# supports both.
class IAmACar(ABC):
    @abstractmethod
    def go_to(self, location: Location) -> None: ...

    @abstractmethod
    def refill_gasoline(self, gallons: float) -> None: ...

    @abstractmethod
    def refill_electricity(self, kilo_watts: float) -> None: ...

    @abstractmethod
    def current_mileage(self) -> int: ...
