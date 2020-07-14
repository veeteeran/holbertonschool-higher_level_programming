-- creates the database hbtn_0d_usa and the table states
-- Another fucking comment
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, name VARCHAR(256));
