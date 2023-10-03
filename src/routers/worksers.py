from fastapi import APIRouter
from sql_base.models import Workers
import resolvers.worker as res_work

work_router = APIRouter()


@work_router.get('/')
def get_worker():
    return f'Responce: {{text: Страница со списком работников }}'


@work_router.post('/create')
def new_workers(workers: Workers):
    work_id = res_work.new_workers(workers)
    return f'{{code: 201, id: {work_id}}}'


@work_router.get('/{worker_id}')
def get_worker(worker_id: int):
    worker = res_work.get_worker(worker_id)
    return f'Worker: {{name: имя, surname: фамилия, id: {worker_id}}}'

@work_router.put('/{worker_id}')
def update_worker(worker_id: int):
    return f'Update worker {worker_id}'


@work_router.delete('/{worker_id')
def delete_worker(worker_id: int):
    return f'Delete worker {worker_id}'