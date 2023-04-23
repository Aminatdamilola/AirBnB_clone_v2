-- create new database hbnb_test_db if not exist
-- craete new user hbnb_test if not exist with all privileges on the database (hbnb_test_db)
-- and with SELECT privilege on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test';
GRANT SELECT ON performance_schema.* TO 'hbnb_test';
