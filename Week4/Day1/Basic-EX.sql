-- Database: Hollywood

-- CREATE DATABASE "Hollywood"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors;

-- SELECT * FROM ACTORS LIMIT 4;

-- SELECT * FROM ACTORS ORDER BY LAST_NAME DESC

-- SELECT * FROM ACTORS WHERE first_name ILIKE '%e%'

-- SELECT * FROM ACTORS WHERE number_oscars >= 5

-- UPDATE actors 
-- SET first_name='Maty' 
-- WHERE first_name='Matt' AND last_name='Damon'
-- RETURNING 
--     actor_id,
--     first_name, 
--     last_name,
--     age;

-- UPDATE actors 
-- SET number_oscars=4
-- WHERE first_name='George' AND last_name='Clooney'
-- RETURNING 
--     actor_id,
--     first_name, 
--     last_name,
--     age;

-- ALTER TABLE actors RENAME COLUMN age TO birthdate;

-- DELETE FROM actors WHERE last_name='Watson'
-- RETURNING actor_id, first_name, last_name, number_oscars;

-- SELECT * FROM actors;

