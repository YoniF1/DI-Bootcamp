-- SELECT COUNT(*) as number_of_actors FROM actors;

-- INSERT INTO actors (last_name, number_oscars)
-- VALUES('Gadot', 2)

-- ERROR:  Failing row contains (21, null, Gadot, null, 2).null value in column "first_name" of relation "actors" violates not-null constraint 

-- ERROR:  null value in column "first_name" of relation "actors" violates not-null constraint
-- SQL state: 23502
-- Detail: Failing row contains (21, null, Gadot, null, 2).

-- There is an error because we have a null constraint on columns in database which does not allow empty value