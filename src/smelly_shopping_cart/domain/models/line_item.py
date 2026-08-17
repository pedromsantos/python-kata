from dataclasses import dataclass

from smelly_shopping_cart.domain.models.product import Product


@dataclass
class LineItem:
    product: Product
    quantity: int
