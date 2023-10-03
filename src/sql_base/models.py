from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Workers(BaseModel):
    workers_id: Optional[int]
    name: str
    surname: str
    post_id: Optional[int]

class Post(BaseModel):
    post_id: Optional[int]
    post_name: str

class Guide(BaseModel):
    pharmacy_id: Optional[int]
    pharmacy_name: str
    pharmacy_telephone_number: str
    pharmacy_address: str

class Products(BaseModel):
    product_id: Optional[int]
    product_name: str
    price: int
    product_expiration_date: Optional[datetime]

class Users(BaseModel):
    user_id: Optional[int]
    user_name: str
    user_password: str
    user_telephone_number: str

class Storage_location(BaseModel):
    storage_location_id: Optional[int]
    storage_location_name: str
    storage_location_telephone_number: str

class Suppliers(BaseModel):
    suppliers_id: Optional[int]
    suppliers_name: str
    suppliers_location_id: Optional[int]
    suppliers_telephone_number: str
    suppliers_shipping_cost: int