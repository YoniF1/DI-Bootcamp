-- Active: 1710676755686@@127.0.0.1@5432@dailychallenge@public

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)

SELECT * FROM SecondTab

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

#Returns count of 0 as a comparison with NULL is essentially unknown in SQL not false so in short its 'find ids from FirstTab which are not in unknown (the result of the subquery)' 

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

#Returns a count of 2 which would be ids 6 and 7 in FirstTab. Again the ID null is unknown so does not count.

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
#Returns a count of 0 as again the comparison is unknown because of the NULL value in SecondTab

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

#Returns count of 2 as id=6 and id=7 in FirstTab are not in SecondTab where the result of subquery is id=5