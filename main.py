# Create a virtual env and install FastAPI and Uvicorn using pip.
# Install postgresql and pgadmin in system
# pip install -r requirements.txt

# Import FastAPI for building the web API.
from fastapi import FastAPI, Depends

# Import the Product class from the local models module.
from models import Product

from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
    db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    # return products
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    # for product in products:
    #     if product.id == id:
    #         return product

    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product

    return "Product not found"

@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    #products.append(product)
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = product
    #         return "Product added successfully"
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated"
    else:
        return "No product found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         del products[i]
    #         return "Product deleted successfully"
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    else:
        return "Product not found"