create database restaurent;
use restaurent;
CREATE TABLE customers (
    cust_id VARCHAR(20) PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL,   
    food TEXT,                 
    quantity INT NOT NULL            
);
INSERT INTO customers (cust_id, cust_name, food , quantity)
VALUES 
('R001', 'Janani', 'Biryani', 5),
('R002', 'Mahitha', 'Dosa', 6),
('R003', 'Abinaya', 'Noodles', 3);
select * from customers;