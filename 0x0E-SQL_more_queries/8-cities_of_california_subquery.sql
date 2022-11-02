-- lists all the cities of california in the database
-- results stored in ascending order by cities.id
SELECT id, name
FROM cities
WHERE state_d = 1
ORDER BY id;
