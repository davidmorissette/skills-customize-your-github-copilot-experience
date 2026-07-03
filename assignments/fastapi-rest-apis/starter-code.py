"""
FastAPI REST API Starter Code

This is a skeleton application to help you get started building a REST API.
Complete the TODOs throughout this file to build your API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI application
app = FastAPI(
    title="My REST API",
    description="A simple REST API for managing items",
    version="1.0.0"
)

# TODO: Define a Pydantic model for your Item
# This model will validate incoming requests and format responses
class Item(BaseModel):
    """Model representing an item in the API"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


# TODO: Create an in-memory storage for items (e.g., a list or dictionary)
items_db = []


# Root endpoint - this one is already done for you!
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the FastAPI REST API!"}


# TODO: Implement GET /items
# Should return a list of all items
@app.get("/items")
def get_items():
    """Retrieve all items"""
    pass


# TODO: Implement GET /items/{item_id}
# Should return a specific item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    pass


# TODO: Implement POST /items
# Should create a new item and return it
@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item"""
    pass


# TODO: Implement PUT /items/{item_id}
# Should update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item"""
    pass


# TODO: Implement DELETE /items/{item_id}
# Should delete an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by ID"""
    pass


# Running the server:
# 1. Install FastAPI and Uvicorn: pip install fastapi uvicorn
# 2. Run: uvicorn starter_code:app --reload
# 3. Visit http://localhost:8000/docs to see the interactive API documentation
