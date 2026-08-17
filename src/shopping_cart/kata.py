from typing import Protocol


class Cart:
    pass


class ShoppingCartRepository(Protocol):
    def save(self, cart: object) -> None: ...

    def get(self, cart_id: str) -> object | None: ...

    def get_all(self) -> list[object]: ...


class InMemoryShoppingCartRepository:
    def save(self, cart: object) -> None:
        pass

    def get(self, cart_id: str) -> object | None:
        return {"id": cart_id}

    def get_all(self) -> list[object]:
        return []


class AddProduct(Protocol):
    def execute(self, cart_id: str, product_id: str) -> None: ...


class CalculateCartPrice(Protocol):
    def query(self, cart_id: str) -> float: ...


class CreateEmpty(Protocol):
    def execute(self, cart_id: str, customer_name: str) -> None: ...
