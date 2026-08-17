# ruff: noqa: ARG002
import pytest

from smelly_shopping_cart.domain.models.product import Product


class TestProductEquality:
    @pytest.mark.parametrize(
        ("difference", "product", "other_product"),
        [
            ("different names", Product("MUG", "Coffee Mug", 7.5), Product("MUG", "Travel Mug", 12)),
            ("different prices", Product("VOUCHER", "Gift Voucher", 5), Product("VOUCHER", "Gift Voucher", 10)),
        ],
    )
    def test_treats_products_with_the_same_code_as_equal_despite_difference(
        self, difference: str, product: Product, other_product: Product
    ) -> None:
        assert product.equals(other_product) is True

    def test_treats_products_with_distinct_codes_as_different_when_their_details_match(self) -> None:
        mug = Product("MUG", "Coffee Mug", 7.5)
        other_mug = Product("MUG-PROMO", "Coffee Mug", 7.5)

        assert mug.equals(other_mug) is False
