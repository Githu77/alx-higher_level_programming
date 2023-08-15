--  lists the max temperatures in order by state name.
SELECT state, max(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
