-- CREATE TABLE items(
-- 	item_id SERIAL PRIMARY KEY,
-- 	object_name VARCHAR(50) NOT NULL,
-- 	price DECIMAL NOT NULL
-- )

-- CREATE TABLE customers(
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- )

-- INSERT INTO items (object_name, price)
-- VALUES('small desk', 100);

-- INSERT INTO items (object_name, price)
-- VALUES('large desk', 300);

-- INSERT INTO items (object_name, price)
-- VALUES('fan', 80);

-- INSERT INTO customers (first_name, last_name)
-- VALUES('Greg', 'Jones');

-- INSERT INTO customers (first_name, last_name)
-- VALUES('Sandra', 'Jones');

-- INSERT INTO customers (first_name, last_name)
-- VALUES('Scott', 'Scott');

-- INSERT INTO customers (first_name, last_name)
-- VALUES('Trevor', 'Green');

-- INSERT INTO customers (first_name, last_name)
-- VALUES('Melanie', 'Johnson');

-- SELECT * FROM items;
-- SELECT * FROM items WHERE price > 80.0;
-- SELECT * FROM items WHERE price <= 300.0;

-- SELECT * FROM customers WHERE last_name = 'Smith';
-- SELECT * FROM customers WHERE last_name = 'Jones';
-- SELECT * FROM customers WHERE NOT first_name = 'Jones';

