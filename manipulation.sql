-- A statement is text that the database recognizes as a valid command. Statements always end in a semicolon
SELECT * FROM celebs;

CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);

-- CREATE TABLE is a clause. Clauses perform specific tasks in SQL. By convention, clauses are written in capital letters. Clauses can also be referred to as commands.
-- table_name refers to the name of the table that the command is applied to.
-- (column_1 data_type, column_2 data_type, column_3 data_type) is a parameter. A parameter is a list of columns, data types, or values that are passed to a clause as an argument. Here, the parameter is a list of column names and the associated data type.

-- CREATE:
-- CREATE statements allow us to create a new table in the database.
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
 );

 -- When you try to create a table with an already existing table name, you will receive an error message, and no table will be modified or created.

-- INSERT:
-- The INSERT statement inserts a new row into a table.
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 22);

INSERT INTO celebs (id, name, age) 
VALUES (2, 'Beyonce Knowles', 33); 
 
INSERT INTO celebs (id, name, age) 
VALUES (3, 'Jeremy Lin', 26); 
 
INSERT INTO celebs (id, name, age) 
VALUES (4, 'Taylor Swift', 26); 

SELECT * FROM celebs;

-- Is there a shorter way to insert multiple rows in a table?
-- Yes, you can list the values for each row separated by commas, following the VALUES clause of the statement.

-- Here is how it would look:

INSERT INTO table (col1, col2, col3)
VALUES
(row1_val1, row1_val2, row1_val3),
(row2_val1, row2_val2, row2_val3),
(row3_val1, row3_val2, row3_val3);

-- SELECT:
-- SELECT statements are used to fetch data from a database.

SELECT name FROM celebs; 
SELECT * FROM celebs;

-- In most SQL databases, by default, the rows will be selected in the order that they appear in the table, from top to bottom. For instance, if you have a statement like
-- SELECT * FROM table; this will select all rows from the table from the first row that appears down to the bottom row.

-- ALTER:
-- The ALTER TABLE statement adds a new column to a table.
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT;

-- Rows that existed before the column was added have NULL (∅) values

-- can we add a column at a specific position to a table?
-- No, unfortunately, you cannot specify what position to add a column to a table.
-- You can always select the columns in any order

-- UPDATE:
-- The UPDATE statement edits a row in a table. You can use the UPDATE statement when you want to change existing records.
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4;

-- DELETE: 
-- The DELETE FROM statement deletes one or more rows from a table.

DELETE FROM celebs 
WHERE twitter_handle IS NULL;

-- CONSTRAINTS:
-- Constraints that add information about how a column can be used are invoked after specifying the data type for a column. They can be used to tell the database to reject inserted data that does not adhere to a certain restriction.
-- The statement below sets constraints on the celebs table.
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
-- PRIMARY KEY columns can be used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a constraint violation which will not allow you to insert the new row.
-- UNIQUE columns have a different value for every row. This is similar to PRIMARY KEY except a table can have many different UNIQUE columns.
-- NOT NULL columns must have a value. Attempts to insert a row without a value for a NOT NULL column will result in a constraint violation and the new row will not be inserted.
-- DEFAULT columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.
