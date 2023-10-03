from fastapi import APIRouter
from sql_base.models import Post
import resolvers.post as res_post

post_router = APIRouter()


@post_router.get('/')
def get_post():
    return f'Responce: {{text: Страница со списков должностей}}'

@post_router.post('/create')
def new_post(post: Post):
    post_id = res_post.new_post(post)
    return f'{{code: 210, id: {post_id}}}'

@post_router.get('/{post_id}')
def get_post(post_id: int):
    post = res_post.get_post(post_id)
    return f'Post: {{ post_name: назввание должности, id: {post_id}}}'

@post_router.put('/{post_id}')
def update_post(post_id: int):
    return f'Update post {post_id}'

@post_router.delete('/{post_id')
def delete_post(post_id: int):
    return f'Delete post {post_id}'