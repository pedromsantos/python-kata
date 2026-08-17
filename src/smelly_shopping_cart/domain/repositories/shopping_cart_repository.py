from typing import Protocol

from smelly_shopping_cart.domain.models.cart import Cart


class ShoppingCartRepository(Protocol):
    def save(self, cart: Cart) -> None: ...

    def find_by_id(self, id: str) -> Cart | None: ...  # noqa: A002
