from smelly_shopping_cart.domain.models.cart import Cart

_carts: dict[str, Cart] = {}


class InMemoryShoppingCartRepository:
    def save(self, cart: Cart) -> None:
        _carts[cart.id] = cart

    def find_by_id(self, id: str) -> Cart | None:  # noqa: A002
        return _carts.get(id)

    @staticmethod
    def clear() -> None:
        _carts.clear()
