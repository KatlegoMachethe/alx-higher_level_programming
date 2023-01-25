-- This script creates a user 'user_0d_0' with the password 'user_0d_1_pwd' if the user doesnt already exist.
-- The user should have all the privileges on the my MySQL server (localhost).
-- Author: Katlego Machethe

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
