from sql_base import base_worker
from sql_base import models


def new_pharmacy(guide: models.Guide) -> int:
    pharmacy_id = base_worker.insert_data("INSERT INTO guide(pharmacy_name, pharmacy_telephone_number, pharmacy_address)"
                                          "VALUES(?, ?, ?)"
                                          "RETURNING pharmacy_id",
                                          (guide.name, guide.telephone_number, guide.pharmacy_address))

    return pharmacy_id