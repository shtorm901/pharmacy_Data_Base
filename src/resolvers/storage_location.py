from sql_base import base_worker
from sql_base import models

def new_storage_loc(storage_location: models.BaseModel) -> int:
    storage_loc_id = base_worker.insert_data("INSERT INTO storage_location(storage_location_name, storage_location_telephone_number)"
                                             "VALUES(?, ?)",
                                             (storage_location.storage_location_name, storage_location.storage_location_telephone_number))

    return storage_loc_id