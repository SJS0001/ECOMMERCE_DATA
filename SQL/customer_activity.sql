SELECT
  CustomerID,
  COUNT(DISTINCT InvoiceNo) AS number_of_orders,
  ROUND(SUM(TotalSum) / COUNT(DISTINCT InvoiceNo), 2) AS average_order_value
FROM `sqltest-489613.ecommerce_analysis.sales`
WHERE CustomerID != 0
GROUP BY CustomerID
ORDER BY average_order_value DESC