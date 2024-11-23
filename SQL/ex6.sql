-- Insert the result of a query
-- Insert a new driver entry for Lewis Hamilton into the Mercedes constructor

-- Delete all previous entries of Lewis Hamilton in Mercedes
DELETE FROM DriverEntry
WHERE Driver_ID = (SELECT Driver_ID FROM Driver WHERE Name = 'Lewis Hamilton')
AND Constructor_ID = (SELECT Constructor_ID FROM Constructor WHERE Name = 'Mercedes');

-- Select to show the entries before inserting the new entry for Lewis Hamilton
SELECT * FROM DriverEntry
WHERE Driver_ID = (SELECT Driver_ID FROM Driver WHERE Name = 'Lewis Hamilton')
AND Constructor_ID = (SELECT Constructor_ID FROM Constructor WHERE Name = 'Mercedes')
LIMIT 10;

-- Insert the new entry
INSERT INTO DriverEntry (Driver_ID, Constructor_ID, Start_Date, Driver_Role, Season_ID)
SELECT 
    (SELECT Driver_ID FROM Driver WHERE Name = 'Lewis Hamilton'),
    (SELECT Constructor_ID FROM Constructor WHERE Name = 'Mercedes'),
    '2019-01-01',
    'Primary Driver',
    2019;

-- Select to show the new entry for Lewis Hamilton
SELECT * FROM DriverEntry
WHERE Driver_ID = (SELECT Driver_ID FROM Driver WHERE Name = 'Lewis Hamilton')
AND Constructor_ID = (SELECT Constructor_ID FROM Constructor WHERE Name = 'Mercedes')
LIMIT 10;

-- Update several tuples at once
-- Update total points for drivers with more than 10 race entries

-- Select to show the total points before the update
SELECT * FROM Driver
WHERE Driver_ID IN (
    SELECT Driver_ID
    FROM RaceResult
    GROUP BY Driver_ID
    HAVING COUNT(RaceResult_ID) > 10
)
LIMIT 10;

-- Perform the update
UPDATE Driver
SET Total_Points = Total_Points + 10
WHERE Driver_ID IN (
    SELECT Driver_ID
    FROM RaceResult
    GROUP BY Driver_ID
    HAVING COUNT(RaceResult_ID) > 10
);

-- Select to show the updated total points for drivers with more than 10 race entries
SELECT * FROM Driver
WHERE Driver_ID IN (
    SELECT Driver_ID
    FROM RaceResult
    GROUP BY Driver_ID
    HAVING COUNT(RaceResult_ID) > 10
)
LIMIT 10;

-- Delete a set of tuples
-- Delete all race results for a random driver where RaceResult_ID is even

-- Select a random Driver_ID
SET @randomDriverID = (SELECT Driver_ID FROM Driver ORDER BY RAND() LIMIT 1);

-- Select to show the race results before the delete
SELECT * FROM RaceResult
WHERE Driver_ID = @randomDriverID
AND MOD(RaceResult_ID, 2) = 0
LIMIT 10;

-- Perform the delete
DELETE FROM RaceResult
WHERE Driver_ID = @randomDriverID
AND MOD(RaceResult_ID, 2) = 0;

-- Select to show the remaining race results for the random driver where RaceResult_ID is even
SELECT * FROM RaceResult
WHERE Driver_ID = @randomDriverID
AND MOD(RaceResult_ID, 2) = 0
LIMIT 10;