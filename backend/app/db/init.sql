CREATE DATABASE todo

USE todo

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NULL,
    status ENUM('pending','in_progress','completed') DEFAULT 'pending',

    CONSTRAINT orders_order_id_fk 
        FOREIGN KEY (user_id) 
        REFERENCES users(id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- CREATE TABLE sessions (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     user_id INT NOT NULL,
--     jti VARCHAR(255) NOT NULL,
--     is_valid BOOLEAN DEFAULT TRUE,
--     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
-- );


