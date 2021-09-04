-- 2.2 Create tableVirtual programming lab
-- Create a table named CUSTOMERS, which contains the ID (first field, primary key, integer value), Last and first names
-- of a customer: FIRSTNAME, LASTNAME (second and third filed using varchar, not more than 30 characters for each one).

CREATE TABLE CUSTOMERS (
  ID INTEGER PRIMARY KEY,
  FIRSTNAME VARCHAR (30),
  LASTNAME VARCHAR (30)
);

-- 2.3 Alter table
-- To the CUSTOMERS table, add a field named ADDRESS of a string type (varchar), which could contain up to 100 characters.

ALTER TABLE `CUSTOMERS` ADD COLUMN `ADRESS` VARCHAR(100);

-- 2.4 Create second table
-- Create a table named ORDERS, which contains an ID field of integer type for storing an order number (primary key),
-- field with product names (PRODUCT_NAME) of a string type (varchar(30)), field with product price (PRODUCT_PRICE) of
-- float type,  field with a date of the order (DATE_ORDER) of a date type, and a number of customer (ID_CUSTOMER) of
-- integer type.

CREATE TABLE ORDERS (
    ID INTEGER PRIMARY KEY,
    PRODUCT_NAME VARCHAR (30),
    PRODUCT_PRICE FLOAT,
    DATE_ORDER DATE TYPE,
    ID_CUSTOMER INTEGER
);

-- 2.5 Update structure of ORDERS table
-- To the table ORDERS, add the AMOUNT field of integer type, which would store the amount of the item bought.

ALTER TABLE ORDERS ADD AMOUNT INTEGER;