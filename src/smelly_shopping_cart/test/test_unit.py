# ruff: noqa: PLR2004, ARG002, SIM300
import math
import time

from smelly_shopping_cart.domain.models.line_item import LineItem
from smelly_shopping_cart.domain.models.product import Product
from smelly_shopping_cart.domain.services.cart_summary_notifier import CartSummaryNotifier
from smelly_shopping_cart.domain.services.promotion_engine import PromotionEngine

_shared_engine = PromotionEngine()
_run_count = 0

TEST_RUN_TIMESTAMP = time.time()


class TestPromotionEngine:
    def test1(self) -> None:
        global _run_count  # noqa: PLW0603
        _run_count += 1
        items = [LineItem(product=Product("VOUCHER", "Voucher", 5.0), quantity=2)]
        result = _shared_engine.apply(items)
        assert result is not None

    def test_should_work(self) -> None:
        assert _run_count > 0
        assert PromotionEngine.get_times_applied() > 0

    def test_prices_vouchers_and_tshirts_and_mugs_and_applies_bulk_discount_and_counts_applications(self) -> None:
        engine = PromotionEngine()
        voucher = Product("VOUCHER", "Voucher", 5.0)
        tshirt = Product("TSHIRT", "T-Shirt", 20.0)
        mug = Product("MUG", "Coffee Mug", 7.5)

        assert engine.apply([LineItem(product=voucher, quantity=2)]) == 5.0
        assert engine.apply([LineItem(product=mug, quantity=1)]) == 7.5
        assert engine.apply([LineItem(product=tshirt, quantity=3)]) == 57.0
        assert engine.apply([LineItem(product=tshirt, quantity=2)]) == 40.0
        assert PromotionEngine.get_times_applied() >= 4

    def test_computes_the_expected_total_using_the_same_logic_as_production(self) -> None:
        engine = PromotionEngine()
        items = [
            LineItem(product=Product("VOUCHER", "Voucher", 5.0), quantity=3),
            LineItem(product=Product("TSHIRT", "T-Shirt", 20.0), quantity=4),
        ]

        expected = 0.0
        for item in items:
            if item.product.code == "VOUCHER":
                expected += math.ceil(item.quantity / 2) * item.product.price
            elif item.product.code == "TSHIRT" and item.quantity >= 3:
                expected += item.quantity * 19.0
            else:
                expected += item.quantity * item.product.price

        assert engine.apply(items) == expected

    def test_reaches_into_a_private_pricing_helper_directly(self) -> None:
        engine = PromotionEngine()
        private_result = engine._price_for(  # noqa: SLF001
            LineItem(product=Product("MUG", "Coffee Mug", 7.5), quantity=1)
        )
        assert private_result == 7.5

    def test_slowly_waits_for_the_engine_to_be_ready(self) -> None:
        time.sleep(0.05)
        engine = PromotionEngine()
        assert engine.apply([LineItem(product=Product("MUG", "Coffee Mug", 7.5), quantity=1)]) == 7.5

    def test_prices_a_single_mug_duplicate_case_one(self) -> None:
        engine = PromotionEngine()
        assert engine.apply([LineItem(product=Product("MUG", "Coffee Mug", 7.5), quantity=1)]) == 7.5

    def test_prices_a_single_mug_duplicate_case_two(self) -> None:
        engine = PromotionEngine()
        assert engine.apply([LineItem(product=Product("MUG", "Coffee Mug", 7.5), quantity=1)]) == 7.5

    def test_prices_a_single_mug_duplicate_case_three(self) -> None:
        engine = PromotionEngine()
        assert engine.apply([LineItem(product=Product("MUG", "Coffee Mug", 7.5), quantity=1)]) == 7.5


class TestCartSummaryNotifier:
    def test_notifies_the_customer_of_the_cart_total(self) -> None:
        class _MockPromotionEngine:
            def apply(self, _items: list[LineItem]) -> float:
                return 42

        class _RecordingNotificationPort:
            def send(self, to: str, message: str) -> None:
                pass

        mock_product = Product("MUG", "Coffee Mug", 7.5)
        notifier = CartSummaryNotifier(_MockPromotionEngine(), _RecordingNotificationPort())  # type: ignore[arg-type]

        total = notifier.notify_total("customer@example.com", [LineItem(product=mock_product, quantity=1)])

        assert total == 42
        assert mock_product.code == "MUG"

    def test_records_the_run_timestamp_alongside_the_notification(self) -> None:
        sent: list[str] = []

        class _RecordingNotificationPort:
            def send(self, to: str, message: str) -> None:
                sent.append(message)

        notifier = CartSummaryNotifier(PromotionEngine(), _RecordingNotificationPort())

        notifier.notify_total(
            "customer@example.com",
            [LineItem(product=Product("MUG", "Coffee Mug", 7.5), quantity=1)],
        )

        assert "Cart total" in sent[0]
        assert TEST_RUN_TIMESTAMP <= time.time()
