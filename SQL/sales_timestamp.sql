SELECT
  FORMAT_DATE('%A', DATE(InvoiceDate)) AS DayOfWeek,
  EXTRACT(HOUR FROM InvoiceDate) AS Hour,
  ROUND(SUM(TotalSum), 2) AS Revenue
FROM `sqltest-489613.ecommerce_analysis.sales`
GROUP BY DayOfWeek, Hour
ORDER BY
  EXTRACT(DAYOFWEEK FROM InvoiceDate),
  Hour