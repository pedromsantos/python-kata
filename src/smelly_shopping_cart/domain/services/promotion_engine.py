import math

from smelly_shopping_cart.domain.models.line_item import LineItem


class PromotionEngine:
    _times_applied = 0

    def __init__(self) -> None:
        self._two_for_one_codes = ["VOUCHER"]
        self._bulk_discount_code = "TSHIRT"
        self._bulk_discount_threshold = 3
        self._bulk_discount_price = 19.0

    def apply(self, items: list[LineItem]) -> float:
        PromotionEngine._times_applied += 1

        total = 0.0
        for item in items:
            total += self._price_for(item)
        return total

    @staticmethod
    def get_times_applied() -> int:
        return PromotionEngine._times_applied

    def _price_for(self, item: LineItem) -> float:
        if item.product.code in self._two_for_one_codes:
            payable_units = math.ceil(item.quantity / 2)
            return payable_units * item.product.price

        if item.product.code == self._bulk_discount_code and item.quantity >= self._bulk_discount_threshold:
            return item.quantity * self._bulk_discount_price

        return item.quantity * item.product.price
