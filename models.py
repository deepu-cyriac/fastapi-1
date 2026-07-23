from pydantic import BaseModel


# Define a simple product model with typed attributes.
# This class is used to create product objects that can be returned by API endpoints.
# class Product:
#     id: int
#     name: str
#     description: str
#     price: float
#     quantity: int

#     def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
#         # Initialize the product instance using the provided values.
#         self.id = id
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity = quantity


class Product(BaseModel):
    # Define the attributes of the Product model with type annotations.
    id: int
    name: str
    description: str
    price: float
    quantity: int