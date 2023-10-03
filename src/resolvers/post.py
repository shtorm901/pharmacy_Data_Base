from sql_base import base_worker
from sql_base import models

def new_post(post: models.BaseModel) -> int:
    post_id = base_worker.insert_data("INSERT INTO post(post_name)"
                                      "VALUES(?)",
                                      (post.post_name))

    return post_id