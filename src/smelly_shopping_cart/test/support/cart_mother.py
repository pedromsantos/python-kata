from smelly_shopping_cart.domain.models.cart import Cart
from smelly_shopping_cart.domain.models.product import Product

DEFAULT_CART_ID = "cart-1"
DEFAULT_CUSTOMER_NAME = "Ada Lovelace"


def _create() -> Cart:
    return Cart(DEFAULT_CART_ID, DEFAULT_CUSTOMER_NAME)


class CartMother:
    create = staticmethod(_create)

    @staticmethod
    def empty_cart() -> Cart:
        return _create()

    @staticmethod
    def voucher_cart(quantity: int) -> Cart:
        cart = _create()
        cart.add_product(Product("VOUCHER", "Voucher", 5), quantity)
        return cart

    @staticmethod
    def t_shirt_cart(quantity: int) -> Cart:
        cart = _create()
        cart.add_product(Product("TSHIRT", "T-Shirt", 20), quantity)
        return cart
