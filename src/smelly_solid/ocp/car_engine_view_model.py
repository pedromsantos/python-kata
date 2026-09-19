"""View model shared by the OCP violation's report views."""

from dataclasses import dataclass


@dataclass
class CarEngineViewModel:
    rpm: float
    temperature: float
