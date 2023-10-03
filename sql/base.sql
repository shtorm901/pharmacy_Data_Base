CREATE TABLE IF NOT EXISTS guide(
    pharmacy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pharmacy_name VARCHAR(100)NOT NULL,
    pharmacy_telephone_number VARCHAR(100) NOT NULL,
    pharmacy_address VARCHAR NOT NULL
);
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    product_expiration_date DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(100) NOT NULL,
    user_password VARCHAR(100) NOT NULL,
    user_telephone_number VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS post(
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_name VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS workers(
    workers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    post_id INTEGER,
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);
CREATE TABLE IF NOT EXISTS storage_location(
    storage_location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    storage_location_name VARCHAR(100) NOT NULL,
    storage_location_telephone_number INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS suppliers(
    suppliers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    suppliers_name VARCHAR(100) NOT NULL,
    storage_location_id INTEGER,
    suppliers_telephone_number INTEGER NOT NULL,
    suppliers_shipping_cost INTEGER NOT NULL,
    FOREIGN KEY (storage_location_id) REFERENCES storage_location(storage_location_id)
);