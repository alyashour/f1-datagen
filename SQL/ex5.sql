-- Query 1: Select all race results along with driver names and constructor names
SELECT rr.RaceResult_ID, d.Name AS Driver_Name, c.Name AS Constructor_Name, rr.Position, rr.Points_Gain_Loss
FROM RaceResult rr
JOIN Driver d ON rr.Driver_ID = d.Driver_ID
JOIN Constructor c ON rr.Constructor_ID = c.Constructor_ID
ORDER BY RAND()
LIMIT 10;

-- Query 2: Select drivers who have won at least one race
SELECT Name
FROM Driver
WHERE Driver_ID IN (
    SELECT Driver_ID
    FROM RaceResult
    WHERE Position = 1
)
ORDER BY RAND()
LIMIT 10;

-- Query 3: Select constructors that have participated in at least one race
SELECT Name
FROM Constructor c
WHERE EXISTS (
    SELECT 1
    FROM RaceResult rr
    WHERE rr.Constructor_ID = c.Constructor_ID
)
ORDER BY RAND()
LIMIT 10;

-- Query 4: Count the number of races each driver has participated in
SELECT d.Name, COUNT(rr.RaceResult_ID) AS Race_Count
FROM Driver d
JOIN RaceResult rr ON d.Driver_ID = rr.Driver_ID
GROUP BY d.Name
ORDER BY RAND()
LIMIT 10;

-- Query 5: Select drivers who have scored more than 50 points
SELECT d.Name, SUM(rr.Points_Gain_Loss) AS Total_Points
FROM Driver d
JOIN RaceResult rr ON d.Driver_ID = rr.Driver_ID
GROUP BY d.Name
HAVING SUM(rr.Points_Gain_Loss) > 50
ORDER BY RAND()
LIMIT 10;

-- Query 6: Select the name of the driver who has the highest total points
SELECT d.Name
FROM Driver d
WHERE d.Total_Points = (
    SELECT MAX(Total_Points)
    FROM Driver
)
LIMIT 10;

-- Query 7: Select the average points gained by drivers in each constructor
SELECT c.Name AS Constructor_Name, AVG(rr.Points_Gain_Loss) AS Avg_Points
FROM RaceResult rr
JOIN Constructor c ON rr.Constructor_ID = c.Constructor_ID
GROUP BY c.Name
ORDER BY RAND()
LIMIT 10;