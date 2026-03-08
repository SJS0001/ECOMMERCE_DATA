SELECT
  Year,
  Month,
  ROUND(SUM(TotalSum), 2) AS revenue
FROM `sqltest-489613.ecommerce_analysis.sales`
GROUP BY Year, Month
ORDER BY Year, Month