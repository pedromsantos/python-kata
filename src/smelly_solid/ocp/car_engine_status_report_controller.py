"""Controller demonstrating an Open/Closed Principle violation."""

from smelly_solid.ocp.car_engine_print_view import CarEnginePrintView
from smelly_solid.ocp.car_engine_view_model import CarEngineViewModel
from smelly_solid.ocp.car_engine_web_view import CarEngineWebView


# OCP violation: every new report format needs a new method on this
# controller (and a new concrete view class) -- the controller must be
# edited, not extended, to add a case.
class CarEngineStatusReportController:
    def __init__(self, view_model: CarEngineViewModel) -> None:
        self._view_model = view_model

    def display_engine_status_report(self) -> CarEngineWebView:
        web_view = CarEngineWebView()
        web_view.fill_with(self._view_model)
        return web_view

    def print_engine_status_report(self) -> CarEnginePrintView:
        print_view = CarEnginePrintView()
        print_view.fill_with(self._view_model)
        return print_view
