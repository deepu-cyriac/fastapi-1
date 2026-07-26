# Create a virtual env and install FastAPI and Uvicorn using pip.
# Install postgresql and pgadmin in system
# pip install -r requirements.txt

# Import FastAPI for building the web API.
from fastapi import FastAPI

# Import the Product class from the local models module.
from models import Product

from database import SessionLocal, engine
import database_models

# Create the FastAPI application instance.
# Uvicorn will use this object to serve the API.
# Use uvicorn main:app --reload to run the application in development mode.
# http://localhost:8000/docs - Swagger UI for API documentation and testing. ( inbuilt in FastAPI )
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    # Return a simple greeting message when the root URL is visited.
    return "Welcome to FarmUp"

# Create a list of sample products in memory.
# In a real application, this would normally come from a database.
products = [
    Product(id=1, name="phone", description="A smartphone", price=599.99, quantity=10),
    Product(id=2, name="laptop", description="A powerful laptop", price=1299.99, quantity=5),
    Product(id=3, name="headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="smartwatch", description="A smartwatch with fitness tracking", price=299.99, quantity=8),
    Product(id=5, name="tablet", description="A lightweight tablet", price=399.99, quantity=12)
]

@app.get("/products")
def get_all_products():
    db = SessionLocal()
    db.query()
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully"

    return "No product found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"

    return "Product not found"