class Product:
    def __init__(self, code: str, name: str, price: float) -> None:
        self.code = code
        self.name = name
        self.price = price

    def equals(self, other: "Product") -> bool:
        return self.code == other.code
