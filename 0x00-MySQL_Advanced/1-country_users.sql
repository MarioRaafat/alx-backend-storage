-- Creates a table users.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL IDENTITY PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US' check (country in ('US', 'CO', 'TN'))
);