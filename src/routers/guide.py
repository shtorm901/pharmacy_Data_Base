from fastapi import APIRouter
from sql_base.models import Guide
import resolvers.guide as res_guide

guide_router = APIRouter()


@guide_router.get('/')
def get_guide():
    return f'Responce: {{text:Страница со списком аптек}}'

@guide_router.post('/create')
def new_guide(guide: Guide):
    guide_id = res_guide.new_pharmacy(guide)
    return f'{{code: 210, id: {guide_id}}}'

@guide_router.get('/{guide_id}')
def get_guide(guide_id: int):
    guide = res_guide.get_guide(guide_id)
    return f'Guide: {{guide_name: название аптеки, guide_telephone_number: номер телефона аптеки, guide_address: адрес аптеки, id:{guide_id}}}'

@guide_router.put('/{guide_id}')
def update_guide(guide_id: int):
    return f'Update guide {guide_id}'

@guide_router.delete('/guide_id}')
def delete_guide(guide_id: int):
    return f'Delete guide {guide_id}'