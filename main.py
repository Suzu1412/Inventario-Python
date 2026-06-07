from product import Product
from inventory import Inventory

user_selection = 0
inventory = Inventory()

while user_selection != 5:
    print("----------------------")
    print("Inventario")
    print("----------------------")
    print("Acciones:")
    print("1- Agregar Producto")
    print("2- Encontrar Producto")
    print("3- Remover Producto")
    print("4- Listar Productos")
    print("5- Salir")

    try:
        user_selection = int(
            input("Ingrese un número para ejecutar acción: ")
        )
    except ValueError:
            print("Debe ingresar un número")

    print("---------")
    match user_selection:
        case 1:
            print("Ingrese los datos para poder agregar el producto")
            try:
                product_id = int(input("Ingrese código de producto: "))
                name = str(input("Ingrese el nombre del producto: "))
                quantity = int(input("Ingrese la cantidad de productos: "))
                    
                product = Product(product_id, name, quantity)
                inventory.add_product(product)

                print("¡Producto agregado exitosamente!")

            except ValueError as error:
                print(f"ERROR: {error}")

        case 2:
            try:
                product_id = int(input("Ingrese código de producto: "))

                product = inventory.find_product(product_id)
                if (product is None):
                    print("Ningún artículo posee el código seleccionado")
                else:
                    print("Producto: ", product.name, " - código: ", product.product_id, " - cantidad: ", product.quantity)

            except ValueError:
                print("Debe ingresar un número")

        case 3:
            try:
                product_id = int(
                    input("Ingrese código de producto: ")
                )
                product = inventory.find_product(product_id)

                if (product is None):
                    print("Ningún artículo posee el código seleccionado")
                else:
                    inventory.remove_product(product)
                    print("Producto removido exitosamente")
            except ValueError:
                print("Debe ingresar un número")
        case 4: 
            print("Listar productos")
            products = inventory.list_products()
            if (not products):
                print("No hay ningún producto agregado")
            for product in products.values():
                print("Producto: ", product.name, " - código: ", product.product_id, " - cantidad: ", product.quantity)

        case 5:
            print("Cerrando aplicación")
            break
        case _:
            print("ERROR: El valor debe ser entre 1 y 5")





