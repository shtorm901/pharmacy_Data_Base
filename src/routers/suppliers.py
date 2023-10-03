from fastapi import APIRouter
from sql_base.models import Suppliers
import resolvers.suppliers as res_suppliers

suppliers_router = APIRouter()

@suppliers_router.get('/')
def get_suppliers():
    return f'Responce: {{text: Страница со списком поставщиков}}'

@suppliers_router.post('/create')
def new_suppliers(suppliers: Suppliers):
    suppliers_id = res_suppliers.new_suppliers(suppliers)
    return f'{{code: 210, id: {suppliers_id}}}'

@suppliers_router.get('/{suppliers_id}')
def get_suppliers(suppliers_id: int):
    suppliers = res_suppliers.get_suplliers(suppliers_id)
    return f'Suppliers: {{ suppliers_name: название компании поставщика,suppliers_telephone_number: номер телефона поставщика, suppliers_shipping_cost: цена доставки, id:{suppliers_id}}}'

@suppliers_router.put('/{suppliers_id}')
def update_suppliers(suppliers_id:  int):
    return f'Update Suppliers {suppliers_id}'

@suppliers_router.delete('/{suppliers_id}')
def delete_suppliers(suppliers_id: int):
    return f'Delete suppliers {suppliers_id}'