SELECT
  Country,
  ROUND(SUM(TotalSum), 2) AS Revenue,
  COUNT(DISTINCT CustomerID) AS Customers,
FROM `sqltest-489613.ecommerce_analysis.sales`
WHERE CustomerID != 0 
GROUP BY Country
ORDER BY Revenue DESC