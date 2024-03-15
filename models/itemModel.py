from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    price: float
    isOffer: Union[bool, None] = None