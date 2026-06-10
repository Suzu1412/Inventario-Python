from product import Product
from inventory import Inventory
from dataclasses import asdict
import json

class InventoryStorage:
    FILE_NAME = "inventory.json"

    def save(self, inventory: Inventory) -> None:
        # 1- Usar asdict para generar la estructura JSON
        products_data = [asdict(product) for product in inventory.list_products()]

        # esta forma ^ es una manera optimizada y mucho mas comunmente usada en python, es el equivalente a:
        #for product in inventory.list_products():
        #    products_data.append(asdict(product))

        # 2- Serializar y guardar en el archivo
        with open(self.FILE_NAME, "w") as file:
            json.dump(products_data, file, indent=4)

    
    def load(self) -> Inventory:
        inventory = Inventory()

        try:
            # 1- Leer el archivo
            with open(self.FILE_NAME, "r") as file:
                products_data = json.load(file)

        except FileNotFoundError:
            return inventory

        # 2- Agregar al inventario
        for product_data in products_data:
            product = Product(**product_data)
            inventory.add_product(product)

        # 3- Por último retornar el inventario completo
        return inventory