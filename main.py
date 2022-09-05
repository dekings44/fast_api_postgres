from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel): #act as a serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool


@app.get('/')
def index():
    return {'message': 'Hello WOrld'}


@app.get('/greet/{name}')
def greet_name(name:str):
    return {'greeting': f'Hello {name}, how are you doing today?'}


@app.get('/greet')
def greet_optional(name:Optional[str] = "user"):
    return {"message": f"Hello {name}"}


@app.put('/item/{item_id}')
def update_item(item_id:int, item:Item):
    return {'name': item.name,
            'description': item.description,
            'price':item.price,
            'on_offer':item.on_offer
            }
