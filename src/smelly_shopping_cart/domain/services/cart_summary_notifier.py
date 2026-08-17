from smelly_shopping_cart.domain.models.line_item import LineItem
from smelly_shopping_cart.domain.ports.notification_port import NotificationPort
from smelly_shopping_cart.domain.services.promotion_engine import PromotionEngine


class CartSummaryNotifier:
    def __init__(self, promotion_engine: PromotionEngine, notifications: NotificationPort) -> None:
        self._promotion_engine = promotion_engine
        self._notifications = notifications

    def notify_total(self, customer_email: str, items: list[LineItem]) -> float:
        total = self._promotion_engine.apply(items)
        self._notifications.send(customer_email, f"Cart total: {total:.2f}€")
        return total
