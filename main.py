# Import FastAPI for building the web API.
from fastapi import FastAPI

# Import the Product class from the local models module.
from models import Product

# Create the FastAPI application instance.
# Uvicorn will use this object to serve the API.
# Use uvicorn main:app --reload to run the application in development mode.
app = FastAPI()

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
    return products