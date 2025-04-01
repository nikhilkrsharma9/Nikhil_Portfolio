# filepath: /c:/Users/ASUS/Desktop/Portfolio/nik_portfolio/fastapi_app.py
import os
import django
from fastapi import FastAPI
from pydantic import BaseModel
from portfolio.models import Item

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nik_portfolio.settings')
django.setup()

app = FastAPI()

class ItemSchema(BaseModel):
    name: str
    description: str

@app.post("/items/")
def create_item(item: ItemSchema):
    new_item = Item(name=item.name, description=item.description)
    new_item.save()
    return {"id": new_item.id, "name": new_item.name, "description": new_item.description}

@app.get("/items/")
def read_items():
    items = Item.objects.all()
    return [{"id": item.id, "name": item.name, "description": item.description} for item in items]