from smelly_shopping_cart.domain.models.cart import Cart
from smelly_shopping_cart.domain.models.product import Product
from smelly_shopping_cart.domain.repositories.shopping_cart_repository import (
    ShoppingCartRepository,  # noqa: TC001
)
from smelly_shopping_cart.infrastructure.repositories.in_memory_shopping_cart_repository import (
    InMemoryShoppingCartRepository,
)


def _a_cart_with_products(id: str) -> Cart:  # noqa: A002
    cart = Cart(id, "Ada Lovelace")
    cart.add_product(Product("MUG", "Coffee Mug", 7.5), 2)
    cart.add_product(Product("VOUCHER", "Gift Voucher", 5), 1)
    return cart


class TestInMemoryShoppingCartRepositoryIntegration:
    def setup_method(self) -> None:
        InMemoryShoppingCartRepository.clear()
        self.repository: ShoppingCartRepository = InMemoryShoppingCartRepository()

    def teardown_method(self) -> None:
        InMemoryShoppingCartRepository.clear()

    def test_finds_cart_when_saved_through_repository(self) -> None:
        cart = _a_cart_with_products("repository-integration-cart-1")

        self.repository.save(cart)
        found = self.repository.find_by_id(cart.id)

        assert found == cart

    def test_returns_none_when_cart_id_is_unknown(self) -> None:
        assert self.repository.find_by_id("unknown-cart") is None
