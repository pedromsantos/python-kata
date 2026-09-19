"""ElectricCar is forced to implement a refuelling method it cannot honour."""

from smelly_solid.isp.i_am_a_car import IAmACar, Location


class ElectricCar(IAmACar):
    def __init__(self) -> None:
        self._mileage = 0
        self._battery_kilo_watts = 0.0

    def go_to(self, location: Location) -> None:
        self._mileage += 1
        print(f"Driving to {location.lat}, {location.lng}")  # noqa: T201

    def refill_gasoline(self, gallons: float) -> None:
        msg = "Electric cars don't take gasoline"
        raise NotImplementedError(msg)

    def refill_electricity(self, kilo_watts: float) -> None:
        self._battery_kilo_watts += kilo_watts

    def current_mileage(self) -> int:
        return self._mileage
