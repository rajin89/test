from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API Server",
    description="A simple FastAPI server",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

# In-memory database (for demo purposes)
items_db: dict = {}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Server", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Create a new item"""
    items_db[item.id] = item
    return item

@app.get("/items/")
async def list_items():
    """Get all items"""
    return {"items": list(items_db.values())}

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    if item_id not in items_db:
        return {"error": "Item not found"}
    return items_db[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemUpdate):
    """Update an existing item"""
    if item_id not in items_db:
        return {"error": "Item not found"}
    
    existing_item = items_db[item_id]
    update_data = item_update.dict(exclude_unset=True)
    updated_item = existing_item.copy(update={**update_data})
    items_db[item_id] = updated_item
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in items_db:
        return {"error": "Item not found"}
    del items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)