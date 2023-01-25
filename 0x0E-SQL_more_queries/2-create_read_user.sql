-- This script creates the database 'hbtn_0d_2' and user 'user_0d_2' (in localhost server obviously).
-- 'user_0d_2' should have only SELECT privilege in the database 'hbtn_0d_2' with password 'user_0d_2_pwd'.
-- If both the database and the user already exist, the script shouldn't fail.
-- @Author: Katlego Machethe

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2'@'localhost';
