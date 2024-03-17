-- CREATE TABLE students(
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(50) NOT NULL,
-- 	birth_date DATE NOT NULL
-- )

-- SET datestyle = 'ISO, DMY';

-- INSERT INTO students(first_name, last_name, birth_date)
-- VALUES
-- 	('Marc', 'Benichou', '02/10/1998'),
-- 	('Yoan', 'Cohen', '03/12/2010'),
-- 	('Lea', 'Benichou', '27/07/1987'),
-- 	('Amelia', 'Dux', '07/04/1996'),
-- 	('David', 'Grez', '14/06/2003'),
-- 	('Omer', 'Simpson', '03/10/1980');

-- SELECT * FROM students;
-- SELECT first_name, last_name FROM students;
-- SELECT * FROM students WHERE id=2;
-- SELECT * FROM students WHERE last_name='Benichou' OR first_name='Marc';
-- SELECT * FROM students WHERE first_name LIKE '%a%';
-- SELECT * FROM students WHERE first_name LIKE 'a%';
-- SELECT * FROM students WHERE first_name LIKE 'a%';
-- SELECT * FROM students WHERE first_name LIKE '%a_';
-- SELECT * FROM students WHERE id=1 AND id=3;
-- SELECT * FROM students WHERE birth_date >='1/01/2000'


-- Exercise XP Gold

-- SELECT * 
-- 	FROM (
--     SELECT *
--     FROM students
--     LIMIT 4
-- )
-- ORDER BY last_name;

-- SELECT * FROM students ORDER BY birth_date LIMIT 1

-- SELECT * FROM students OFFSET 2 LIMIT 3;
