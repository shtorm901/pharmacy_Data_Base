from sql_base import base_worker
from sql_base import models


def new_worker(workers: models.Workers) -> int:
    work_id = base_worker.insert_data("INSERT INTO workers(post_id, name, surname)"
                                      "VALUES(?,?,?)"
                                      "RETURNING workers_id",
                                      (workers.post_id, workers.name, workers.surname))
    return work_id