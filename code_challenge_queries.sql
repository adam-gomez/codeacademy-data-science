-- Find the number of girls who were named Lillian for the full span of time of the database.
-- Select only the year and number columns.

SELECT year, number
FROM babies
WHERE name = 'Lillian' AND gender = 'F';

-- Find 20 distinct names that start with ‘S’.
-- Select only the name column.

SELECT DISTINCT name
FROM babies
WHERE name LIKE 'S%'
LIMIT 20;

-- What are the top 10 names in 1880?
-- Select the name, gender, and number columns.

SELECT name, gender, number
FROM babies
WHERE year = 1880
ORDER BY number DESC
LIMIT 10;

-- Suppose your friend Jaime wants to go out to Japanese, but you’re on a budget.
-- Return all the restaurants that are Japanese and $$.
-- Select all the columns.

SELECT * 
FROM nomnom
WHERE cuisine = 'Japanese' AND price = '$$';

-- Your roommate Bevers can’t remember the exact name of a restaurant he went to but he knows it contains the word ‘noodle’ in it.
-- Can you find it for him using a query?
-- Select all the columns.

SELECT *
FROM nomnom
WHERE name LIKE '%noodle%';

-- Some of the restaurants have not been inspected yet or are currently appealing their health grade score.
-- Find the restaurants that have empty health values.
-- Select all the columns.

SELECT *
FROM nomnom
WHERE health IS NULL;

-- Order the table by title (from A-Z).
-- Select only the title and publisher columns.

SELECT title, publisher
FROM news
ORDER BY title ASC;

-- Which article names have the word 'bitcoin' in it?
-- Select all the columns.

SELECT *
FROM news
WHERE title LIKE '%bitcoin%';

-- Can we match for a specific casing of text?
/* we can utilize a special type of statement in SQLite, known as a PRAGMA statement. 
PRAGMA statements are a specific type of statement in SQLite, 
and can be used to modify certain behaviors of the available functionality. */

PRAGMA case_sensitive_like = true;

SELECT *
FROM news
WHERE column LIKE '%Bitcoin%';

-- The category column contains the article category:
-- 'b' stands for Business
-- 't' stands for Technology
-- What are the 20 business articles published most recently?
-- Select all the columns.

SELECT *
FROM news
WHERE category = 'b'
ORDER BY timestamp DESC
LIMIT 20;

-- Is your name in babies?
SELECT *
FROM babies
WHERE name LIKE '%adam%';

-- How many babies were given your name? 
SELECT number
FROM babies
WHERE name LIKE '%adam%';

-- What are the top 5 restaurants in nomnom?
SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 5;

-- What are the top 5 Chinese restaurants?
SELECT *
FROM nomnom
WHERE cuisine = 'Chinese'
ORDER BY review DESC
LIMIT 5;

-- Which articles are from Wall Street Journal in news?
SELECT *
FROM news
WHERE publisher = 'Wall Street Journal';

-- Which technology articles are from Wall Street Journal?
SELECT *
FROM news
WHERE category = 't' AND publisher = 'Wall Street Journal';

