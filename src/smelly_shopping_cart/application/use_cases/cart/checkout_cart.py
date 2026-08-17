import random
from collections.abc import Callable
from dataclasses import dataclass

from smelly_shopping_cart.application.use_cases.cart.order_clock import OrderClock
from smelly_shopping_cart.domain.ports.clock import Clock
from smelly_shopping_cart.domain.ports.notification_port import NotificationPort
from smelly_shopping_cart.domain.repositories.shopping_cart_repository import ShoppingCartRepository
from smelly_shopping_cart.infrastructure.gateways.email_notification_gateway import EmailNotificationGateway


@dataclass
class Receipt:
    cart_id: str
    total: float
    confirmation_code: str
    confirmed_at: str


class CheckoutCart:
    def __init__(
        self,
        repository: ShoppingCartRepository,
        notifier: NotificationPort | None = None,
        clock: Clock | None = None,
        random_source: Callable[[], float] = random.random,
    ) -> None:
        self._repository = repository
        self._notifier: NotificationPort = notifier if notifier is not None else EmailNotificationGateway()
        self._clock: Clock = clock if clock is not None else OrderClock()
        self._random_source = random_source

    def execute(self, cart_id: str, customer_email: str) -> Receipt:
        cart = self._repository.find_by_id(cart_id)
        if cart is None:
            msg = f"Cart {cart_id} not found"
            raise ValueError(msg)

        total = cart.calculate_subtotal()
        confirmation_code = f"ORD-{int(self._random_source() * 1_000_000)}"
        confirmed_at = self._clock.now()

        self._notifier.send(customer_email, f"Order confirmed: {confirmation_code}, total {total:.2f}€")

        return Receipt(cart_id=cart_id, total=total, confirmation_code=confirmation_code, confirmed_at=confirmed_at)
