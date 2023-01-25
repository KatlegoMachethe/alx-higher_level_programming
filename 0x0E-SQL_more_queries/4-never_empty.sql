-- This script creates a table 'id_not_null' on MySQL server if it doesnt exist.
-- The table must have resourses id (int with default value of 1) and name (varchar(256)).
-- The database name shall be passed as an argument in the terminal.

CREATE TABLE IF NOT EXISTS id_not_null (
	id int DEFAULT 1,
	name varchar(256)
	);
