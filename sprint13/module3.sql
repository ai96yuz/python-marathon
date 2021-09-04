-- 3.1 Select field
-- There are 2 tables
--   CUSTOMERS(ID, FIRSTNAME, LASTNAME, ADDRESS);
--   ORDERS (ID, PRODUCT_NAME, PRODUCT_PRICE, DATE_ORDER, ID_CUSTOMER, AMOUNT);
-- Find out which customers have been registered in our shop (show all available fields). Please sort the list by ID.

SELECT *
FROM CUSTOMERS
WHERE ID IN (SELECT ID_CUSTOMER FROM ORDERS)
GROUP BY ID;

-- 3.2 Select all
-- There are 2 tables
--   CUSTOMERS(ID, FIRSTNAME, LASTNAME, ADDRESS);
--   ORDERS (ID, PRODUCT_NAME, PRODUCT_PRICE, DATE_ORDER, ID_CUSTOMER, AMOUNT);
-- Show name of products from ORDERS table in one query ordered alphabetically.

-- 3.1 Select All
-- There are 2 tables
--   CUSTOMERS(ID, FIRSTNAME, LASTNAME, ADDRESS);
--   ORDERS (ID, PRODUCT_NAME, PRODUCT_PRICE, DATE_ORDER, ID_CUSTOMER, AMOUNT);
-- Show name of products from ORDERS table in one query ordered alphabetically.

SELECT PRODUCT_NAME FROM ORDERS
ORDER BY PRODUCT_NAME ASC;

-- 3.4 Select sorted
-- There are 2 tables
--   CUSTOMERS(ID, FIRSTNAME, LASTNAME, ADDRESS);
--   ORDERS (ID, PRODUCT_NAME, PRODUCT_PRICE, DATE_ORDER, ID_CUSTOMER, AMOUNT);
-- Find out which products and when have been ordered in our shop. The results should be sorted by ordering date in
-- ascending order and include only top 3 rows.
-- PS. Please pay attentions that we are using SQLite version of SQL language and "top 3 rows" can be achieved using
-- additional cause in end of the select sentence as additional phrase "limit 3"

