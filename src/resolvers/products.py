from sql_base import base_worker
from sql_base import models


def new_products(products: models.Products) -> int:
    prod_id = base_worker.insert_data("INSERT INTO products(product_name, price, product_expiration_date)"
                                      "VALUES(?, ?, ?)",
                                      (products.product_name, products.price, products.product_expiration_date))

    return prod_id