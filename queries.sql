-- We should get acquainted with the movies table.
SELECT * FROM movies;

-- Suppose we are only interested in two of the columns. We can select individual columns by their names (separated by a comma):
SELECT name, genre, year 
FROM movies;

-- AS is a keyword in SQL that allows you to rename a column or table using an alias. 
SELECT name AS 'known_as'
FROM movies;

SELECT imdb_rating AS 'IMDb'
FROM movies;

-- DISTINCT is used to return unique values in the output. It filters out all duplicate values in the specified column(s).
SELECT DISTINCT genre 
FROM movies;

SELECT DISTINCT year 
FROM movies;

-- WHERE clause filters the result set to only include rows where the following condition is true.
SELECT * 
FROM movies 
WHERE imdb_rating < 5;

SELECT * 
FROM movies 
WHERE year > 2014;

-- LIKE can be a useful operator when you want to compare similar values.
-- LIKE is a special operator used with the WHERE clause to search for a specific pattern in a column.
-- _ means you can substitute any individual character here without breaking the pattern. 
SELECT * 
FROM movies
WHERE name LIKE 'Se_en';

-- The percentage sign % is another wildcard character that can be used with LIKE
-- % is a wildcard character that matches zero or more missing letters in the pattern.
SELECT * 
FROM movies 
WHERE name LIKE '%man%';

SELECT * 
FROM movies
WHERE name LIKE 'The %';

-- It is not possible to test for NULL values with comparison operators, such as = and !=.
-- Instead, we will have to use these operators:
-- IS NULL
-- IS NOT NULL
SELECT name
FROM movies 
WHERE imdb_rating IS NULL;

-- The BETWEEN operator is used in a WHERE clause to filter the result set within a certain range.
-- The operator is inclusive, but with strings, it will only include up to the precise minimal limit set by the operator
-- BETWEEN 'A' and 'J' for example will include strings containing only 'J' but not strings that would come after 'J' like 'Ja'
SELECT *
FROM movies
WHERE name BETWEEN 'D' AND 'G';

SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979;

-- Sometimes we want to combine multiple conditions in a WHERE clause to make the result set more specific and useful.
SELECT * 
FROM movies
WHERE year BETWEEN 1990 AND 1999
   AND genre = 'romance';

SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating > 8;

SELECT *
FROM movies
WHERE year < 1985
  AND genre = 'horror';

-- Similar to AND, the OR operator can also be used to combine multiple conditions in WHERE, but there is a fundamental difference:
-- OR operator displays a row if any condition is true.
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';

SELECT *
FROM movies
WHERE genre = 'comedy'
   OR genre = 'romance';

-- We can sort the results using ORDER BY, either alphabetically or numerically. 
-- DESC is a keyword used in ORDER BY to sort the results in descending order (high to low or Z-A).
-- ASC is a keyword used in ORDER BY to sort the results in ascending order (low to high or A-Z).
-- The column that we ORDER BY doesn’t even have to be one of the columns that we’re displaying.
-- ORDER BY always goes after WHERE (if WHERE is present).
SELECT name, year
FROM movies
ORDER BY name;

SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;

-- LIMIT is a clause that lets you specify the maximum number of rows the result set will have.
-- LIMIT always goes at the very end of the query. Also, it is not supported in all SQL databases.
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;

-- A CASE statement allows us to create different outputs (usually in the SELECT statement). It is SQL’s way of handling if-then logic.
-- The CASE statement must end with END.
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies;

SELECT name,
CASE
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy' THEN 'Chill'
  ELSE 'Intense'
END AS 'Mood'
FROM movies;


