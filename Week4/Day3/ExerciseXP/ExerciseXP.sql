-- Active: 1710676755686@@127.0.0.1@5432@dvdrental@public
#in dvdrental database
#Exercise1
SELECT name FROM language;

SELECT film.title, film.description, language.name FROM film INNER JOIN language ON film.language_id = language.language_id;

SELECT film.title, film.description, language.name FROM film RIGHT OUTER JOIN language ON film.language_id = language.language_id;

CREATE TABLE new_film(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
)

INSERT INTO new_film(name)
VALUES 
        ('Gladiator'),
        ('Star Wars'),
        ('Wolf of Wall Street'),
        ('Lord of the Rings'),
        ('The Shawshank Redemption')
        ('Les Choristes')

CREATE TABLE customer_review(
    review_id SERIAL PRIMARY KEY,
    film_id INT,
    language_id INT,
    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES language(language_id),
    title VARCHAR(50),
    score INT,
    CHECK (score BETWEEN 1 AND 10),
    review_text VARCHAR,
    last_update TIMESTAMP
)
INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES
        ((SELECT id FROM new_film WHERE name='Gladiator'), (SELECT language_id FROM language WHERE name='English'), 'My film review', 10, 'A simply awesome film', CURRENT_TIMESTAMP ),
        ((SELECT id FROM new_film WHERE name='Les Choristes'), (SELECT language_id FROM language WHERE name='French'), 'My second film review', 9, 'Marvellous, a true blockbuster', CURRENT_TIMESTAMP)

DELETE FROM new_film WHERE name='Les Choristes'
# Deleting from parent deletes the corresponding review in child class
SELECT * from customer_review;

#Exercise 2
UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'French')
WHERE title='Chamber Italian' OR title='Airport Pollock'

SELECT * from customer;
#On the customer table there is the address_id foreign key and store_id foreign key
#It affects the way we insert because we need to make sure the data exists in the other table's primary key column
-- e.g you cannot have a foreign key value of 8 in address_id if there are only 7 records in the address table. Also we need to mindful of the effect of deletion.

DROP TABLE customer_review;
# It's a simple drop as the child customer_review table does not affect any rows of the parent new_film

SELECT COUNT(film.film_id) FROM film INNER JOIN inventory ON film.film_id = inventory.film_id INNER JOIN rental ON inventory.inventory_id = rental.inventory_id WHERE rental.return_date IS NULL;
#183

SELECT film.title, film.rental_rate FROM film INNER JOIN inventory ON film.film_id = inventory.film_id INNER JOIN rental ON inventory.inventory_id = rental.inventory_id WHERE rental.return_date IS NULL ORDER BY film.rental_rate DESC LIMIT 30;


SELECT film.title, description FROM film INNER JOIN film_actor ON film.film_id = film_actor.film_id INNER JOIN actor ON film_actor.actor_id = actor.actor_id WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.fulltext@@to_tsquery('sumo');

#Park Citizen

SELECT film.title FROM film 
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE film.length < 60 AND film.rating='R' AND category.name LIKE 'Documentary'

#Cupboard Sinners

SELECT film.title, payment.amount, rental.return_date FROM film 
INNER JOIN inventory ON film.film_id = inventory.film_id 
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id 
INNER JOIN payment ON rental.rental_id = payment.rental_id 
INNER JOIN customer ON payment.customer_id = customer.customer_id 
WHERE 
customer.first_name = 'Matthew' 
AND customer.last_name = 'Mahan' 
AND payment.amount > 4.00 
AND rental.return_date > '2005-07-28' 
AND rental.return_date < '2005-08-01'

#Sugar Wonka

SELECT film.title, film.replacement_cost, film.description FROM film 
INNER JOIN inventory ON film.film_id = inventory.film_id 
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id 
INNER JOIN payment ON rental.rental_id = payment.rental_id 
INNER JOIN customer ON payment.customer_id = customer.customer_id 
WHERE fulltext@@to_tsquery('boat')
AND customer.first_name = 'Matthew' 
AND customer.last_name = 'Mahan'
ORDER BY film.replacement_cost DESC

#Stone Fire is most expensive of the three