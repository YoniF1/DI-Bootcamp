-- Active: 1710676755686@@127.0.0.1@5432@dailychallenge@public

CREATE TABLE customer(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(100) NOT NULL
)

CREATE TABLE customer_profile(
    id INTEGER,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INTEGER NOT NULL,
    PRIMARY KEY(customer_id),
    CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customer(id)
)

INSERT INTO customer(first_name, last_name)
VALUES
    ('John', 'Doe'),
    ('Jerome', 'Lalu'),
    ('Lea', 'Rive')

INSERT INTO customer_profile(isloggedin, customer_id)
VALUES
    (TRUE, (SELECT id FROM customer WHERE first_name='John'))

INSERT INTO customer_profile(customer_id)
VALUES
    ((SELECT id FROM customer WHERE first_name='Jerome'))

SELECT * FROM customer_profile


SELECT customer.first_name FROM customer INNER JOIN customer_profile ON customer.id = customer_profile.customer_id WHERE customer_profile.isloggedin = TRUE

SELECT customer.first_name, customer_profile.isloggedin FROM customer LEFT OUTER JOIN customer_profile ON customer.id = customer_profile.customer_id

SELECT COUNT(customer.id) FROM customer INNER JOIN customer_profile ON customer.id = customer_profile.customer_id WHERE customer_profile.isloggedin = FALSE

#Exercise2

CREATE TABLE book(
    book_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL
)

INSERT INTO book(title, author)
VALUES
    ('Alice in Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To Kill a Mockingbird', 'Harper Lee')

CREATE TABLE student(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INTEGER,
    CHECK (age BETWEEN 0 AND 15)
)

INSERT INTO student(name, age)
VALUES
    ('John', 12),
    ('Lera', 10),
    ('Patrick', 10),
    ('Bob', 14)

CREATE TABLE Library(
    book_fk_id INTEGER,
    student_fk_id INTEGER,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY(book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
)

INSERT INTO Library(student_fk_id, book_fk_id, borrowed_date)
VALUES
    ((SELECT student_id FROM student WHERE name = 'John'), (SELECT book_id FROM book WHERE title='Alice in Wonderland'), '2022-02-15'),
    ((SELECT student_id FROM student WHERE name = 'Bob'), (SELECT book_id FROM book WHERE title='To Kill a Mockingbird'), '2021-03-03'),
    ((SELECT student_id FROM student WHERE name = 'Lera'), (SELECT book_id FROM book WHERE title='Alice in Wonderland'), '2021-05-23'),
    ((SELECT student_id FROM student WHERE name = 'Bob'), (SELECT book_id FROM book WHERE title='Harry Potter'), '2021-08-12')

SELECT * FROM library;

SELECT student.name, book.title FROM library 
INNER JOIN student ON library.student_fk_id = student.student_id
INNER JOIN book ON library.book_fk_id = book.book_id

SELECT AVG(student.age) AS average_age FROM library 
INNER JOIN student ON library.student_fk_id = student.student_id
INNER JOIN book ON library.book_fk_id = book.book_id
WHERE book.title = 'Alice in Wonderland'


SELECT * FROM library

DELETE FROM student WHERE name='John'

#After the student was deleted, because of the cascade, the record with the student was also removed in the library table