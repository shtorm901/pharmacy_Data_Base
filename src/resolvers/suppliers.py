from sql_base import base_worker
from sql_base import models


def new_suppliers(suppliers: models.BaseModel ) -> int:
    suppliers_id = base_worker.insert_data("INSERT INTO suppliers(suppliers_name, storage_location_id, suppliers_telephone_number, suppliers_shipping_cost)"
                                           "VALUES(?, ?, ?, ?)",
                                           (suppliers.suppliers_name, suppliers.storage_location_id, suppliers.suppliers_telephone_number, suppliers.suppliers_shipping_cost))

    return suppliers_id