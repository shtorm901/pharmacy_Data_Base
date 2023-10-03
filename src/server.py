from fastapi import FastAPI
from sql_base import base_worker
from settings import Base
from routers.worksers import work_router
from routers.guide import guide_router
from routers.products import product_router
from routers.post import post_router
from routers.storage_location import storage_router
from routers.suppliers import suppliers_router


base_worker.set_base_bath(Base)


if not base_worker.Base_check():
    base_worker.Base_create('../sql/base.sql')


app = FastAPI()

@app.get("/")
def main_page():
    return {'page:' 'Connection is correct'}


app.include_router(work_router, prefix='/worker')
app.include_router(guide_router, prefix='/guide')
app.include_router(product_router, prefix='/products')
app.include_router(post_router, prefix='/post')
app.include_router(storage_router, prefix='/storage')
app.include_router(suppliers_router, prefix='/suppliers')