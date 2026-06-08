from product import Product 

class Inventory:
    def __init__(self):
        self._products: dict[int, Product] = {} # Privado para comunicar que no se debe tocar

    def add_product(self, product: Product) -> None:
        if self.find_product(product.product_id):
            raise ValueError("El producto ya existe")
        self._products[product.product_id] = product


    def find_product(self, product_id: int) -> Product | None:
        return self._products.get(product_id)        

    def remove_product(self, product: Product) -> None:
        del self._products[product.product_id]

    def list_products(self) -> dict[int, Product]:
        return self._products.values()

