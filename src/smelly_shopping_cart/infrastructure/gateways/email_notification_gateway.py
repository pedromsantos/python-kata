class EmailNotificationGateway:
    def __init__(self, from_address: str = "orders@shop.example.com") -> None:
        self._from_address = from_address

    def send(self, to: str, message: str) -> None:
        print(f"[EMAIL {self._from_address} -> {to}] {message}")  # noqa: T201
