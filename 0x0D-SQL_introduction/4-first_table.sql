-- This script ceate a table called first_table in my sql database
-- The table should have two attributes id (int) and name (varchar(256))
-- Database name will be passed as an argument in mysql command.
-- The script shouldnt fail if the table already exists
-- Challenge: Shouldnt use SELECT or SHOW.
-- @Author: Katlego Machethe

CREATE TABLE IF NOT EXISTS first_table (
	id int,
	name varchar(256));
