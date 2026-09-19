"""Print view for the OCP violation kata."""

from smelly_solid.ocp.car_engine_view_model import CarEngineViewModel


class CarEnginePrintView:
    def __init__(self) -> None:
        self.text = ""

    def fill_with(self, view_model: CarEngineViewModel) -> None:
        self.text = f"RPM: {view_model.rpm}, Temp: {view_model.temperature}"
