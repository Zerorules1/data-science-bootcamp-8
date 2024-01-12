-- Open my Database 'restaurant'
.open restaurant.db

  -- Create table and insert data
CREATE TABLE IF NOT EXISTS MenuItems (
    item_id INT,
    item_name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

INSERT INTO MenuItems VALUES
  (1, 'Pizza', 'Cheese Pizza', 9.99),
  (2, 'Burger', 'Beef Burger', 8.99),
  (3, 'Fries', 'Curly Fries', 5.99),
  (4, 'Salad', 'Ceaser Salad', 6.99),
  (5, 'Soda', 'Coke', 1.99);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT,
    customer_name TEXT NOT NULL,
    city TEXT
);

INSERT INTO Customers VALUES
  (1, 'John', 'New York'),
  (2, 'Mary', 'London'),
  (3, 'Bob', 'Paris'),
  (4, 'Alice', 'Tokyo'),
  (5, 'Eve', 'Sydney')
;

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL
);

INSERT INTO Orders VALUES 
  (1, 1, '2022-08-01'),
  (2, 2, '2022-08-02'),
  (3, 3, '2022-08-03'),
  (4, 4, '2022-08-04'),
  (5, 5, '2022-08-05')
;

CREATE TABLE IF NOT EXISTS Employees (
    employee_id INT,
    employee_name TEXT NOT NULL,
    position TEXT
);

INSERT INTO Employees VALUES 
  (1, 'Danny', 'Manager'),
  (2, 'Lisa', 'Chef'),
  (3, 'Rose', 'Waiter')
;

CREATE TABLE IF NOT EXISTS OrderItems (
    order_item_id INT,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL
);

INSERT INTO OrderItems VALUES 
  (1, 1, 4, 3),
  (2, 1, 2, 1),
  (3, 1, 3, 2),
  (4, 2, 1, 1),
  (5, 2, 5, 5)
;

-- Use Common Table Expression to find the total sales for each menu item
WITH ItemSales AS (
  SELECT mi.item_name, SUM(oi.quantity * mi.price) AS total_sales
  FROM MenuItems mi
  JOIN OrderItems oi ON mi.item_id = oi.item_id
  GROUP BY mi.item_name
)
SELECT * FROM ItemSales;

-- Use a subquery to find the customer with the highest total order amount
SELECT customer_name
FROM Customers
WHERE customer_id = (
    SELECT customer_id
    FROM Orders
    JOIN (
        SELECT order_id, SUM(quantity * price) AS total_amount
        FROM OrderItems
        JOIN MenuItems ON OrderItems.item_id = MenuItems.item_id
        GROUP BY order_id
        ORDER BY total_amount DESC
        LIMIT 1
    ) AS highest_order ON Orders.order_id = highest_order.order_id
);
