from product import Product 

class Inventory:
    def __init__(self):
        self.products: dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        if self.find_product(product.product_id):
            raise ValueError(
                "El producto ya existe"
            )
        self.products[product.product_id] = product


    def find_product(self, product_id: int) -> Product | None:
        return self.products.get(product_id)        

    def remove_product(self, product: Product) -> None:
        del self.products[product.product_id]

    def list_products(self) -> dict[int, Product]:
        return self.products

