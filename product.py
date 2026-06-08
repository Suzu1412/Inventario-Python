from dataclasses import dataclass
@dataclass 
class Product:
    product_id: int
    name: str
    quantity: int

    # Con esto agregamos validaciones para impedir que pueda crearse algo con errores
    def __post_init__(self): 

        if self.product_id <= 0:
            raise ValueError(
                "ID inválido"
            )

        if not self.name.strip(): # strip remueve todos los carácteres haciendo una copia primero
            raise ValueError(
                "Nombre vacío"
            )

        if self.quantity < 0:
            raise ValueError(
                "Cantidad inválida"
            )
        
    def modify_stock(self, amount: int):
        if self.quantity + amount < 0:
            raise ValueError(
                "Stock insuficiente"
            )
        self.quantity += amount

    # Este es el equivalente al methodo ToString()
    def __str__(self):
        return (
            f"Producto: {self.name}"
            f" - código: {self.product_id}"
            f" - cantidad: {self.quantity}"
        )