# ruff: noqa: PLR2004
from smelly_shopping_cart.domain.models.cart import Cart
from smelly_shopping_cart.domain.models.product import Product
from smelly_shopping_cart.test.support.cart_mother import CartMother


class TestCartMother:
    def test_creates_a_valid_cart_with_stable_defaults(self) -> None:
        cart = CartMother.create()

        assert isinstance(cart, Cart)
        assert cart.id == "cart-1"
        assert cart.customer_name == "Ada Lovelace"
        assert len(cart.line_items) == 0

    def test_uses_named_scenarios_to_create_valid_carts_with_controlled_quantities(self) -> None:
        empty_cart = CartMother.empty_cart()
        voucher_cart = CartMother.voucher_cart(3)
        t_shirt_cart = CartMother.t_shirt_cart(4)

        assert len(empty_cart.line_items) == 0
        assert len(voucher_cart.line_items) == 1
        assert isinstance(voucher_cart.line_items[0].product, Product)
        assert voucher_cart.line_items[0].product.code == "VOUCHER"
        assert voucher_cart.line_items[0].quantity == 3
        assert len(t_shirt_cart.line_items) == 1
        assert isinstance(t_shirt_cart.line_items[0].product, Product)
        assert t_shirt_cart.line_items[0].product.code == "TSHIRT"
        assert t_shirt_cart.line_items[0].quantity == 4
