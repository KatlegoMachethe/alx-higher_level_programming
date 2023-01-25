-- This script removes all records with score <= 5in 'second_table'.
-- The database name 'hbtn_0c_0' will be passed as an argument in the terminal.

DELETE FROM second_table
WHERE score <= 5;
