# ruff: noqa: PLR2004
# Acceptance tests for the CheckoutCart use case.
# Boundary: use case -> domain. Mocked: repository, notifier, clock, random source.
# Real: Cart, Product, LineItem, PromotionEngine (the domain is exercised for real).
import pytest

from smelly_shopping_cart.application.use_cases.cart.checkout_cart import CheckoutCart
from smelly_shopping_cart.domain.models.cart import Cart
from smelly_shopping_cart.domain.models.product import Product

MUG = Product("MUG", "Coffee Mug", 7.5)
VOUCHER = Product("VOUCHER", "Voucher", 5.0)

FIXED_CONFIRMED_AT = "2024-01-01T00:00:00.000Z"


def _fixed_random_source() -> float:
    return 0.5  # -> int(0.5 * 1_000_000) = 500000


class _FakeShoppingCartRepository:
    def __init__(self) -> None:
        self._carts: dict[str, Cart] = {}

    def seed(self, cart: Cart) -> None:
        self._carts[cart.id] = cart

    def save(self, cart: Cart) -> None:
        self._carts[cart.id] = cart

    def find_by_id(self, id: str) -> Cart | None:  # noqa: A002
        return self._carts.get(id)


class _FixedClock:
    def __init__(self, fixed_instant: str) -> None:
        self._fixed_instant = fixed_instant

    def now(self) -> str:
        return self._fixed_instant


class _RecordingNotificationPort:
    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def send(self, to: str, message: str) -> None:
        self.sent.append((to, message))


class TestCheckoutCartAcceptance:
    def setup_method(self) -> None:
        self.repository = _FakeShoppingCartRepository()
        self.notifier = _RecordingNotificationPort()
        self.use_case = CheckoutCart(
            self.repository,
            self.notifier,
            _FixedClock(FIXED_CONFIRMED_AT),
            _fixed_random_source,
        )

    def test_confirms_checkout_and_returns_a_receipt_when_the_cart_has_no_discounts(self) -> None:
        cart = Cart("cart-1", "Ada Lovelace")
        cart.add_product(MUG, 1)
        self.repository.seed(cart)

        receipt = self.use_case.execute("cart-1", "ada@example.com")

        assert receipt.cart_id == "cart-1"
        assert receipt.total == 7.5
        assert receipt.confirmation_code == "ORD-500000"
        assert receipt.confirmed_at == FIXED_CONFIRMED_AT

    def test_notifies_the_customer_of_the_confirmed_total_when_checkout_succeeds(self) -> None:
        cart = Cart("cart-2", "Ada Lovelace")
        cart.add_product(MUG, 1)
        self.repository.seed(cart)

        receipt = self.use_case.execute("cart-2", "ada@example.com")

        assert len(self.notifier.sent) == 1
        assert self.notifier.sent[0] == (
            "ada@example.com",
            f"Order confirmed: {receipt.confirmation_code}, total 7.50€",
        )

    def test_computes_the_confirmed_total_using_real_promotion_rules_for_a_two_for_one_discount(self) -> None:
        cart = Cart("cart-3", "Grace Hopper")
        cart.add_product(VOUCHER, 3)  # two-for-one: 2 payable units * 5.0€ = 10.0€
        self.repository.seed(cart)

        receipt = self.use_case.execute("cart-3", "grace@example.com")

        assert receipt.total == 10.0
        assert self.notifier.sent[-1] == (
            "grace@example.com",
            f"Order confirmed: {receipt.confirmation_code}, total 10.00€",
        )

    def test_rejects_checkout_when_the_cart_does_not_exist(self) -> None:
        with pytest.raises(ValueError, match="Cart missing-cart not found"):
            self.use_case.execute("missing-cart", "nobody@example.com")

    def test_does_not_notify_the_customer_when_the_cart_does_not_exist(self) -> None:
        with pytest.raises(ValueError, match="not found"):
            self.use_case.execute("missing-cart", "nobody@example.com")

        assert self.notifier.sent == []
