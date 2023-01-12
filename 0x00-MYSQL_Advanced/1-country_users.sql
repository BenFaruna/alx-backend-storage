-- SQL query for creating table with id, email and name column
-- The id column is a primary key with auto increment
-- The email column only accepts unique values
-- Country column aacepts only 'US', 'CO' and 'TN'
CREATE TABLE IF NOT EXISTS users
    (id INTEGER NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255), PRIMARY KEY (id),
    country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US');