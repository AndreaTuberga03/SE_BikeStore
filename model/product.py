from dataclasses import dataclass

@dataclass
class Product:
    id: int
    product_name: str

    def __str__(self):
        return self.product_name

    def __repr__(self):
        return self.product_name

    def __hash__(self):
        return hash(self.id)