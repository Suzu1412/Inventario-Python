def read_int(message: str) -> int:

    while True:
        try:
            return int(input(message))

        except ValueError:
            print("ERROR: Debe ingresar un número válido")


def read_non_empty_string(message: str) -> str:

    while True:

        value = input(message).strip()

        if value:
            return value

        print("ERROR: El texto no puede estar vacío")

def read_positive_int(message: str) -> int:

    while True:

        value = read_int(message)

        if value > 0:
            return value

        print("ERROR: Debe ser mayor que cero")

def read_non_negative_int(message: str) -> int:

    while True:

        value = read_int(message)

        if value >= 0:
            return value

        print("ERROR: No puede ser negativo")