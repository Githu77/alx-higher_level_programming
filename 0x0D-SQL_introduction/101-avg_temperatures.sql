-- shows the average temperature "Fahr" by city in descending order in order by city.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;
