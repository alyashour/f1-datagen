-- Query 1: Select all race results along with driver names and constructor names
WITH temp AS (SELECT pitstop.pitstop_id,
                     pitstop.race_id,
                     pitstop.time_in_pit,
                     pitstop.driver_id,
                     driver.name      AS driver_name,
                     grandprix.grandprix_id,
                     grandprix.season_id,
                     grandprix.name   AS grandprix_name,
                     driverentry.constructor_id,
                     constructor.name AS constructor_name
              FROM pitstop
                       JOIN driver,
                   grandprix,
                   driverentry,
                   constructor
              WHERE (
                        driver.driver_id = pitstop.driver_id
                            AND grandprix.race_id = pitstop.race_id
                            AND driverentry.driver_id = driver.driver_id
                            AND driverentry.season_id = grandprix.season_id
                            AND driverentry.constructor_id = constructor.constructor_id
                        ))
SELECT constructor_id,
       constructor_name,
       MIN(time_in_pit) AS min_time_in_pit
FROM temp
GROUP BY constructor_id;


-- Query 2: Select drivers who have won at least one race
SELECT Name
FROM Driver
WHERE Driver_ID IN (SELECT Driver_ID
                    FROM RaceResult
                    WHERE Position = 1);

-- Query 3: Select constructors that have participated in at least one race
SELECT Name
FROM Constructor c
WHERE EXISTS (SELECT 1
              FROM RaceResult rr
              WHERE rr.Constructor_ID = c.Constructor_ID);

-- Query 4: Count the number of races each driver has participated in
SELECT d.Name, COUNT(rr.RaceResult_ID) AS Race_Count
FROM Driver d
         JOIN RaceResult rr ON d.Driver_ID = rr.Driver_ID
GROUP BY d.Name;

-- Query 5: Select drivers who have scored more than 50 points
SELECT d.Name, SUM(rr.Points_Gain_Loss) AS Total_Points
FROM Driver d
         JOIN RaceResult rr ON d.Driver_ID = rr.Driver_ID
GROUP BY d.Name
HAVING SUM(rr.Points_Gain_Loss) > 50;

-- Query 6: Select the name of the driver who has the highest total points
SELECT d.Name
FROM Driver d
WHERE d.Total_Points = (SELECT MAX(Total_Points)
                        FROM Driver);

-- Query 7: Select the average points gained by drivers in each constructor
SELECT c.Name AS Constructor_Name, AVG(rr.Points_Gain_Loss) AS Avg_Points
FROM RaceResult rr
         JOIN Constructor c ON rr.Constructor_ID = c.Constructor_ID
GROUP BY c.Name;