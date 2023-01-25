-- This script lists all records in 'second_table' of database 'hbtn_0c_0'.
-- Rows  without the 'name' value shouldn't be listed.
-- The results should be displaye in the order 'name, score' in descending order.
-- The database name will be passed an argument in the terminal.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
