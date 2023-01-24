-- The script list all the records with score >= 1 in 'second_table' of 'hbtn_0c_0'.
-- Results displayed in order score then name with top score appearing first.
-- Database name will be passed as argument name on terminal.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
