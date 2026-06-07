from product import Product
from inventory import Inventory
from utils import *

user_selection = 0
inventory = Inventory()

# Menu Functions
def add_product_menu(inventory: Inventory) -> None:
        print("Ingrese los datos para poder agregar el producto")
        try:
            product = create_product()
            inventory.add_product(product)
            print("Producto agregado exitosamente")

        except ValueError as error:
            print(error)


def find_product_menu(inventory: Inventory) -> None:
    try:
        product = find_product(inventory)
        if (product is None):
            print("No se ha encontrado ningún producto")
        else:
            print("Producto: ", product.name, " - código: ", product.product_id, " - cantidad: ", product.quantity)
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
    except ValueError as error:
        print(error)

def list_product_menu(inventory: Inventory) -> None:
    print("Listar productos")
    products = inventory.list_products()
    if (not products):
        print("No hay ningún producto agregado")
    else: 
        for product in products.values():
            print("Producto: ", product.name, " - código: ", product.product_id, " - cantidad: ", product.quantity)


# Functions
def read_user_selection() -> int:
    print("Acciones:")
    print("1- Agregar Producto")
    print("2- Encontrar Producto")
    print("3- Remover Producto")
    print("4- Listar Productos")
    print("5- Salir")

    try:
        user_selection = read_positive_int("Ingrese un número para ejecutar acción: ")
        return user_selection
    except ValueError:
        print("Debe ingresar un número")


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
                print("Cerrando aplicación")
                break
            case _:
                print("ERROR: El valor debe ser entre 1 y 5")


# Esto hará que solo se ejecute el código si se ejecuta main.py directamente, si otro archivo importa esto no se ejecutará código automáticamente
if __name__ == "__main__":
    main()