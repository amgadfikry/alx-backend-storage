-- script that creates a table users with specific requirements
-- create table users with column id, email, name, country
CREATE TABLE IF NOT EXISTS users(
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (id),
  UNIQUE (email)
);
