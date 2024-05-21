--t displays the max temperature of each state
SELECT state, MAX(temperature) AS max_temp
FROM temperatures ORDER BY state;
