from typing import ClassVar

from smelly_shopping_cart.domain.models.product import Product
from smelly_shopping_cart.domain.repositories.shopping_cart_repository import ShoppingCartRepository


class _ProductCatalog:
    _catalog: ClassVar[dict[str, Product]] = {
        "VOUCHER": Product("VOUCHER", "Voucher", 5.0),
        "TSHIRT": Product("TSHIRT", "T-Shirt", 20.0),
        "MUG": Product("MUG", "Coffee Mug", 7.5),
    }

    @staticmethod
    def find(code: str) -> Product:
        product = _ProductCatalog._catalog.get(code)
        if product is None:
            msg = f"Unknown product code {code}"
            raise ValueError(msg)
        return product


class AddProductToCart:
    def __init__(self, repository: ShoppingCartRepository) -> None:
        self._repository = repository

    def execute(self, cart_id: str, product_code: str, quantity: int = 1) -> None:
        cart = self._repository.find_by_id(cart_id)
        if cart is None:
            msg = f"Cart {cart_id} not found"
            raise ValueError(msg)

        cart.add_product(_ProductCatalog.find(product_code), quantity)
        self._repository.save(cart)
