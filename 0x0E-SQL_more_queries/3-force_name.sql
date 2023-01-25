-- This script creates a table 'force_name' if it doesn't exist.
-- The table must have resource id (int) and name (varchar(265) cant be null).
-- The database name is to be passed as argument in the terminal.
-- @Author: Katlego Machethe

CREATE TABLE IF NOT EXISTS force_name (
	id int,
	name varchar(256) NOT NULL
	);
