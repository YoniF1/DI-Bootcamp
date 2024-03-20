-- Active: 1710676755686@@127.0.0.1@5432@day4@public
CREATE TABLE menu_items(
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
)


SELECT * FROM menu_items;
