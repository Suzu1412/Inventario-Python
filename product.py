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
        
    def increase_stock(self, amount: int):
        self.quantity += amount

    def decrease_stock(self, amount: int):
        if amount > self.quantity:
            raise ValueError(
                "Stock insuficiente"
            )

        self.quantity -= amount