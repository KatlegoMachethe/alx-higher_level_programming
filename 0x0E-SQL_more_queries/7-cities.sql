-- Script creates database 'hbtn_0d_usa' and table 'cities' if they don't exist.
-- 'cities' has resources id (int, unique, auto generted, not null, primary key),
-- state_id (int, not null, foreign key referencing the id of states able), and name (varchar(256) not null).
-- @Author: Katlego Machethe

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id int UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id int NOT NULL FOREIGN KEY (state_id) REFERENCES states (id),
	name varchar(256) NOT NULL
	);
