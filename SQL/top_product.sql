SELECT
  Description,
  SUM(Quantity) AS units_sold,
  ROUND(SUM(TotalSum), 2) AS Revenue
FROM `sqltest-489613.ecommerce_analysis.sales`
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10