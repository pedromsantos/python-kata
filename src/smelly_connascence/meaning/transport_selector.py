"""TransportSelector demonstrating Connascence of Meaning."""


# Connascence of Meaning: "1"/"2"/"3"/"4" only mean bike/car/train/bus by
# an unstated convention shared between the caller and this method --
# nothing in the code documents or enforces the mapping.
class TransportSelector:
    def __init__(self) -> None:
        self._selected: list[str] = []

    def set_transport(self, transport: str) -> None:
        if transport == "1":
            self._selected.append("bike")
        elif transport == "2":
            self._selected.append("car")
        elif transport == "3":
            self._selected.append("train")
        elif transport == "4":
            self._selected.append("bus")
        else:
            msg = f"Unknown transport code: {transport}"
            raise ValueError(msg)
