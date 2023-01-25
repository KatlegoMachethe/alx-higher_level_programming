-- This script creates database 'hbtn_0d_usa' and the table 'states' if they dont exist.
-- 'states' has resources id (int unique, auto generated, can't be null and is a primary key) and
-- name (varchar(256) can't be null).
-- @Author:katlego Machethe

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id int UNIQUE AUTO_INRCEMENT PRIMARY KEY,
	name varchar(256) NOT NULL
	);

