-- This script creates a table 'second_table' in the database 'hbtn_0c_'.
-- Columns/variables of this table are id (int), name (varchar(256)), and score (int).
-- The script should create four records (as seen in the actual statements).
-- Challenge: Must not use SELECT and SHOW statements.
-- @Author: Katlego Machethe

CREATE TABLE IF NOT EXISTS second_table (
	id int,
	name varchar(256),
	score int);

INSERT INTO second_table (id, name, score)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
