create database restaurant;
use restaurant;
CREATE TABLE menu_items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,   
    price DECIMAL(10,2)NOT NULL,                 
    description TEXT            
)
select * from menu_items;
