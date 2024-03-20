-- Active: 1710676755686@@127.0.0.1@5432@day4@public

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    capital VARCHAR(50),
    flag VARCHAR,
    subregion VARCHAR(50),
    population INT
)


SELECT * FROM countries;