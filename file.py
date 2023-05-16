

A window function is a type of function in SQL that performs a calculation across a set of rows that are related to the current row. Here's an example of a window function in SQL using the OVER clause:
Let's say we have a table called "sales" that contains sales data for a company, with columns for "date", "product", and "sales_amount". We want to calculate the total sales for each product over the previous 3 days, including the current day.
We can use a window function to accomplish this by using the OVER clause to define a window that includes the current row and the preceding 2 rows. Here's the SQL code for this query:

SELECT date, product, sales_amount,
  SUM(sales_amount) OVER (
    PARTITION BY product
    ORDER BY date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS total_sales
FROM sales

In this example, the SUM function is used as a window function to calculate the total sales for each product over the previous 3 days. The PARTITION BY clause groups the data by product, and the ORDER BY clause orders the data by date within each product group. The ROWS BETWEEN clause defines the window as including the current row and the 2 preceding rows.
The result set will include columns for "date", "product", "sales_amount", and "total_sales", with the "total_sales" column showing the sum of sales_amount over the previous 3 days for each product.
