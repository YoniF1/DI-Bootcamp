#It will only work with the right database set up

#Exercise1
#dvdrental

SELECT rating, COUNT(rating) FROM film GROUP BY rating;

SELECT title FROM film WHERE rating IN ('G', 'PG-13') AND rental_rate < 3.00 AND length < 120 ORDER BY title;

UPDATE customer
SET first_name = 'Yoni', last_name = 'F', email = 'yoni@email.com'
WHERE customer_id = 1;

UPDATE address
SET address='123 Fake Street'
WHERE address_id = 5;

#Exercise2
#bootcamp

SELECT * FROM students;

UPDATE students
SET birth_date='02/11/1998'
WHERE last_name='Benichou'

UPDATE students
SET last_name = 'Guez'
WHERE last_name='Grez'

DELETE from students
WHERE first_name='Lea'
RETURNING *;

SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM students WHERE birth_date > '1/01/2000';

ALTER TABLE students
ADD math_grade SMALLINT;

UPDATE students
SET math_grade = 80
WHERE id = 1;

UPDATE students
SET math_grade = 90
WHERE id=2 OR id=4

UPDATE students
SET math_grade = 40
WHERE id = 6;

SELECT COUNT(*) FROM students WHERE math_grade > 83;

INSERT INTO students(first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '2003-06-14', 70);

SELECT first_name, last_name, COUNT(math_grade) AS total_grade FROM students GROUP BY first_name, last_name;

SELECT SUM(math_grade) AS sum_of_grades FROM students;

#Exercise3
#public database

CREATE TABLE purchases(
    id SERIAL PRIMARY KEY,
    customer_id INT,
    item_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    quantity_purchased SMALLINT
);

INSERT INTO purchases(customer_id, item_id, quantity_purchased)
SELECT
    (SELECT customer_id FROM customers WHERE first_name='Scott' AND last_name='Scott'),
    (SELECT item_id FROM items WHERE object_name = 'fan'),
    1;

INSERT INTO purchases(customer_id, item_id, quantity_purchased)
SELECT
    (SELECT customer_id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'),
    (SELECT item_id FROM items WHERE object_name='large desk'),
    10;

INSERT INTO purchases(customer_id, item_id, quantity_purchased)
SELECT
    (SELECT customer_id FROM customers WHERE first_name='Greg' AND last_name='Jones'),
    (SELECT item_id FROM items WHERE object_name='small desk'),
    2;


SELECT * FROM purchases;
# It is useful but as two of the three columns are foreign keys we can't get more useful information without joining the other tables
SELECT * FROM purchases INNER JOIN customers ON purchases.customer_id = customers.customer_id;

SELECT * FROM purchases INNER JOIN customers ON purchases.customer_id = customers.customer_id WHERE purchases.customer_id = 5;

SELECT * FROM purchases INNER JOIN items ON purchases.item_id = items.item_id WHERE object_name='large desk' AND object_name='small desk'

SELECT customers.first_name, customers.last_name, items.object_name 
FROM purchases
INNER JOIN customers 
ON purchases.customer_id = customers.customer_id 
INNER JOIN items
ON purchases.item_id = items.item_id

INSERT INTO purchases(customer_id, quantity_purchased)
VALUES (1, 2)
#It works but the item_id is left blank. It's possible as there is no null constraint on the item_id column when 
#the table was created


