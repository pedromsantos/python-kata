"""Web view for the OCP violation kata."""

from smelly_solid.ocp.car_engine_view_model import CarEngineViewModel


class CarEngineWebView:
    def __init__(self) -> None:
        self.html = ""

    def fill_with(self, view_model: CarEngineViewModel) -> None:
        self.html = f"<div>{view_model.rpm} rpm, {view_model.temperature}C</div>"
