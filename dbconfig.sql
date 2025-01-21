-- Real Estate Management System Database Setup
-- Author: Satya
CREATE DATABASE IF NOT EXISTS real_estate_db;
USE real_estate_db;
CREATE TABLE IF NOT EXISTS properties (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    type VARCHAR(100) NOT NULL
);
