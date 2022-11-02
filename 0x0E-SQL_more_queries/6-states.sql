-- creates the database hbtn_0d_usa and the table states
-- states description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST states
(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
);
