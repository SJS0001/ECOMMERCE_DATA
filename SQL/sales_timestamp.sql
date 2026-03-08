SELECT
  CASE 
    WHEN DayOfWeek = 'Monday' THEN '1-Pondělí'
    WHEN DayOfWeek = 'Tuesday' THEN '2-Úterý'
    WHEN DayOfWeek = 'Wednesday' THEN '3-Středa'
    WHEN DayOfWeek = 'Thursday' THEN '4-Čtvrtek'
    WHEN DayOfWeek = 'Friday' THEN '5-Pátek'
    WHEN DayOfWeek = 'Saturday' THEN '6-Sobota'
    WHEN DayOfWeek = 'Sunday' THEN '7-Neděle'
    ELSE DayOfWeek
  END AS DayOfWeek_Fixed,
  LPAD(CAST(Hour AS STRING), 2, '0') AS Hour, 
  ROUND(SUM(TotalSum), 2) AS Revenue
FROM `sqltest-489613.ecommerce_analysis.sales`
GROUP BY DayOfWeek_Fixed, Hour
ORDER BY DayOfWeek_Fixed, Hour
