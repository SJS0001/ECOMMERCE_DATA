SELECT
  Description,
  SUM(Quantity) AS units_sold,
  ROUND(SUM(TotalSum), 2) AS Revenue
FROM `sqltest-489613.ecommerce_analysis.sales`
WHERE Description NOT IN ('POSTAGE', 'DOTCOM POSTAGE', 'MANUAL')
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10
