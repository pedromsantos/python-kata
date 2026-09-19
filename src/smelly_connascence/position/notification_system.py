"""NotificationSystem demonstrating Connascence of Position."""


# Connascence of Position: three same-typed string parameters carry
# meaning only through argument order -- swap recipient and sender and
# the call still compiles, but breaks silently.
class NotificationSystem:
    def send_email(self, recipient: str, sender: str, message: str) -> None:
        print(f"From: {sender}")  # noqa: T201
        print(f"To: {recipient}")  # noqa: T201
        print(f"Message: {message}")  # noqa: T201


notification_system = NotificationSystem()
notification_system.send_email("recipient@email.com", "sender@email.com", "text")
