-- This script creates a table 'unique_id' if it doesnt exist with resources id(int with default 1 and must beunique)
-- and name (varchar(256)).
-- @Author: Katlego Machethe

CREATE TABLE IF NOT EXISTS unique_id (
	id int DEFAULT 1,
	name varchar(256),
	UNIQUE(id)
	);
