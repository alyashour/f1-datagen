-- Insert the result of a query
-- Insert a new driver entry for Lewis Hamilton into the Mercedes constructor
INSERT INTO DriverEntry (Driver_ID, Constructor_ID, Start_Date, Driver_Role)
SELECT d.Driver_ID, c.Constructor_ID, '2023-01-01', 'Primary Driver'
FROM Driver d, Constructor c
WHERE d.Name = 'Lewis Hamilton' AND c.Name = 'Mercedes';

-- Show the result of the insertion
SELECT * FROM DriverEntry;

-- Update several tuples at once
-- Update total points for drivers with more than 10 race entries
UPDATE Driver
SET Total_Points = Total_Points + 10
WHERE Driver_ID IN (
    SELECT Driver_ID
    FROM RaceResult
    GROUP BY Driver_ID
    HAVING COUNT(RaceResult_ID) > 10
);

-- Show the result of the update
SELECT * FROM Driver;

-- Delete a set of tuples
-- Delete all race results for Sebastian Vettel from Ferrari
DELETE FROM RaceResult
WHERE Driver_ID = (SELECT Driver_ID FROM Driver WHERE Name = 'Sebastian Vettel')
AND Constructor_ID = (SELECT Constructor_ID FROM Constructor WHERE Name = 'Ferrari');

-- Show the result of the deletion
SELECT * FROM RaceResult;
