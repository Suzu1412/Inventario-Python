from product import Product
from inventory import Inventory
from utils import *
from storage import InventoryStorage

user_selection = 0
inventory = Inventory()

# Menu Functions
def add_product_menu(inventory: Inventory) -> None:
        print("Ingrese los datos para poder agregar el producto")
        try:
            product = create_product()
            inventory.add_product(product)
            print("Producto agregado exitosamente")
            export_json(inventory)

        except ValueError as error:
            print(error)


def find_product_menu(inventory: Inventory) -> None:
    try:
        product = find_product(inventory)
        if (product is None):
            print("No se ha encontrado ningún producto")
        else:
            print(product)
    except ValueError as error:
        print(error)

def delete_product_menu(inventory: Inventory) -> None:
    try:
        product = find_product(inventory)
        if (product is None):
            print("No se ha encontrado ningún producto")
        else:
            inventory.remove_product(product)
            print("Producto removido exitosamente")
            export_json(inventory)
    except ValueError as error:
        print(error)

def list_product_menu(inventory: Inventory) -> None:
    print("Listar productos")
    products = inventory.list_products()
    if (not products):
        print("No hay ningún producto agregado")
    else: 
        for product in products:
            print(product)

def modify_stock_menu(inventory: Inventory) -> None:
    product = find_product(inventory)
    if (product is None):
        print("No se ha encontrado ningún producto")
    else:
        try:
            quantity = read_int("Ingrese cantidad a modificar: ")
            product.modify_stock(quantity)

            print("Se ha modificado la cantidad exitosamente")
            print(product)
            export_json(inventory)
        except ValueError as error:
            print(error)

def export_json(inventory: Inventory) -> None:
    storage = InventoryStorage()
    storage.save(inventory)

def import_json() -> Inventory:
    storage = InventoryStorage()
    return storage.load()


# Functions
def read_user_selection() -> int:
    print("Acciones:")
    print("1- Agregar Producto")
    print("2- Encontrar Producto")
    print("3- Remover Producto")
    print("4- Listar Productos")
    print("5- Modificar Stock de Producto")
    print("6- Salir")

    return read_positive_int("Ingrese un número para ejecutar acción: ")

def create_product() -> Product:
    product_id = read_positive_int("Ingrese código: ")
    name = read_non_empty_string("Ingrese nombre: ")
    quantity = read_non_negative_int("Ingrese cantidad: ")

    return Product(product_id, name, quantity)


def find_product(inventory: Inventory) -> Product | None:
    product_id = read_positive_int("Ingrese código: ")

    product = inventory.find_product(product_id)
    return product

def main():
    inventory = import_json()
    print("----------------------")
    print("Inventario")
    print("----------------------")

    while True:
        user_selection = read_user_selection()
        print("---------")
        match user_selection:
            case 1:
                add_product_menu(inventory)
            case 2:
                find_product_menu(inventory)
            case 3:
                delete_product_menu(inventory)
            case 4: 
                list_product_menu(inventory)
            case 5: 
                modify_stock_menu(inventory)
            case 6:
                print("Cerrando aplicación")
                break
            case _:
                print("ERROR: El valor debe ser entre 1 y 6")


# Esto hará que solo se ejecute el código si se ejecuta main.py directamente, si otro archivo importa esto no se ejecutará código automáticamente
if __name__ == "__main__":
    main()