from fastapi import APIRouter
from sql_base.models import Storage_location
import resolvers.storage_location as res_storage

storage_router = APIRouter()


@storage_router.get('/')
def get_storage():
    return f'Responce: {{text: Страница со списком складов}}'

@storage_router.post('/create')
def new_storage(storage_location: Storage_location):
    storage_location_id = res_storage.new_storage_loc(storage_location)
    return f'{{code: 210, id: {storage_location_id}}}'

@storage_router.get('/{storage_location_id}')
def get_storage(storage_location_id: int):
    storage_location = storage_router.get_storage(storage_location_id)
    return f'Storage: {{storage_location_name: название склада, storage_location_telephone_number: номер телефона склада, id:{storage_location_id}}}'

@storage_router.put('/{storage_location_id')
def update_storage(storage_location_id: int):
    return f'Update storage {storage_location_id}'

@storage_router.delete('/{storage_location_id}')
def delete_storage(storage_location_id: int):
    return f'Delete storage {storage_location_id}'