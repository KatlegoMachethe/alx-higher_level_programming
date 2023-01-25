-- This script lists the number of records with the same score in 'second_table' of 'hbtn_0c_0'.
-- The results shoul display the score and then after the number of record for the score (with label 'number').
-- List to be sorted in descending order for the number of records.
-- The database name shall be passed as an argument in the terminal.
-- @Author: Katlego Machethe

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
