"""ReceiptSender demonstrating Connascence of Execution Order."""


# Connascence of Execution Order: archive() is only correct if
# send_to_customer() has already run, but nothing in the type or method
# signatures expresses that -- the caller has to know the right order
# from tribal knowledge, not from the code.
class ReceiptSender:
    def __init__(self) -> None:
        self._sent = False

    def send_to_customer(self, receipt_id: str) -> None:
        print(f"Emailing receipt {receipt_id} to customer")  # noqa: T201
        self._sent = True

    def archive(self, receipt_id: str) -> None:
        if not self._sent:
            print(f"Warning: archiving {receipt_id} before it was sent")  # noqa: T201
        print(f"Archiving receipt {receipt_id}")  # noqa: T201
