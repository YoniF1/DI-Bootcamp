-- Active: 1710676755686@@127.0.0.1@5432@dvdrental@public
#Exercise1

#Will only work with public database

-- SELECT * FROM items ORDER BY price;

-- SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

-- SELECT first_name, last_name FROM customers ORDER BY first_name LIMIT 3;

-- SELECT last_name FROM customers ORDER BY last_name DESC;

#Exercise2

#With dvdrental database

-- SELECT * FROM customer;

-- SELECT CONCAT(first_name,' ', last_name) AS full_name FROM customer;

-- SELECT DISTINCT create_date FROM customer;

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

-- SELECT address, phone FROM address WHERE district='Texas';

-- SELECT * FROM film WHERE film_id = 15 OR film_id = 150;

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Lord of the Rings';

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Lo%'

-- SELECT * FROM film ORDER BY rental_rate LIMIT 10;

-- SELECT * FROM film ORDER BY rental_rate OFFSET 10 LIMIT 10;
#OR
-- SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY rental_rate) AS row_num FROM film) WHERE row_num BETWEEN 11 and 20

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date 
-- FROM customer INNER JOIN payment 
-- ON payment.customer_id = customer.customer_id
-- ORDER BY payment.customer_id;

-- SELECT * FROM film LEFT OUTER JOIN inventory
-- ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;

-- SELECT city.city, country.country FROM city INNER JOIN country
-- ON city.country_id = country.country_id

-- SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date 
-- FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id  
-- INNER JOIN staff ON payment.staff_id = staff.staff_id 
-- ORDER BY payment.staff_id;

