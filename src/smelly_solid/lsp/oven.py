"""Abstract Oven contract for the Liskov Substitution Principle kata."""

from abc import ABC, abstractmethod


class Oven(ABC):
    @abstractmethod
    def cook(self, food: str) -> None: ...
