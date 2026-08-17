# ruff: noqa: PLR2004
import time
from types import SimpleNamespace

import pytest

from smelly_shopping_cart.domain.models.cart import Cart
from smelly_shopping_cart.domain.models.product import Product
from smelly_shopping_cart.infrastructure.gateways.email_notification_gateway import EmailNotificationGateway
from smelly_shopping_cart.infrastructure.repositories.in_memory_shopping_cart_repository import (
    InMemoryShoppingCartRepository,
)

DEFAULT_CUSTOMER_EMAIL = "customer@example.com"


class TestInMemoryShoppingCartRepository:
    def test2(self) -> None:
        repository = InMemoryShoppingCartRepository()
        cart = Cart("cart-1", "Ada Lovelace")
        cart.add_product(Product("MUG", "Coffee Mug", 7.5), 1)

        repository.save(cart)

        assert cart is not None

    def test_finds_the_cart_saved_earlier(self) -> None:
        repository = InMemoryShoppingCartRepository()
        found = repository.find_by_id("cart-1")

        assert found

    def test_saves_and_re_finds_and_mutates_and_re_saves_and_counts_items_and_checks_the_customer_name(
        self,
    ) -> None:
        repository = InMemoryShoppingCartRepository()
        cart = Cart("cart-2", "Grace Hopper")
        cart.add_product(Product("VOUCHER", "Voucher", 5.0), 1)
        repository.save(cart)

        first_find = repository.find_by_id("cart-2")
        first_find.add_product(Product("TSHIRT", "T-Shirt", 20.0), 1)  # type: ignore[union-attr]
        repository.save(first_find)  # type: ignore[arg-type]

        second_find = repository.find_by_id("cart-2")
        assert second_find is not None
        assert second_find.id == "cart-2"
        assert second_find.customer_name == "Grace Hopper"
        assert len(second_find.line_items) == 2
        assert repository.find_by_id("does-not-exist") is None

    def test_slowly_waits_for_the_in_memory_store_to_be_ready(self) -> None:
        time.sleep(0.05)
        repository = InMemoryShoppingCartRepository()
        cart = Cart("cart-3", "Margaret Hamilton")
        repository.save(cart)
        assert repository.find_by_id("cart-3") is not None

    def test_saves_a_cart_double_instead_of_a_real_cart(self) -> None:
        mock_cart = SimpleNamespace(
            id="cart-4",
            customer_name="Katherine Johnson",
            line_items=[],
            add_product=lambda *args, **kwargs: None,  # noqa: ARG005
            calculate_subtotal=lambda: None,
        )
        repository = InMemoryShoppingCartRepository()

        repository.save(mock_cart)  # type: ignore[arg-type]
        found = repository.find_by_id("cart-4")

        assert found is mock_cart


class TestEmailNotificationGateway:
    def test_sends_an_order_confirmation_email(self, capsys: pytest.CaptureFixture[str]) -> None:
        gateway = EmailNotificationGateway()

        gateway.send(DEFAULT_CUSTOMER_EMAIL, "Order confirmed: ORD-1")

        captured = capsys.readouterr()
        assert DEFAULT_CUSTOMER_EMAIL in captured.out
