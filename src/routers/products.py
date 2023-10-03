from fastapi import APIRouter
from sql_base.models import Products
import resolvers.products as res_products

product_router = APIRouter()


@product_router.get('/')
def get_product():
    return f'Responce: {{text: Страница со списком товаров}}'

@product_router.post('/create')
def new_product(product: Products):
    product_id = res_products.new_products(product)
    return f'{{code: 210, id: {product_id}}}'

@product_router.get('/{pgoduct_id')
def get_product(product_id: int):
    product = res_products.get_product(product_id)
    return f'Product: product_name: название продукта, price: цена, product_expiration_date: срок годности, id:{product_id}}}'

@product_router.put('/{product_id}')
def update_product(product_id: int):
    return f'Update product {product_id}'

@product_router.delete ('/{product_id}')
def delete_product(product_id: int):
    return f'Delete product {product_id}'