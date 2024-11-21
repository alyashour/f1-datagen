-- Create View 1: DriverStats
CREATE VIEW DriverStats AS
SELECT
    Driver_ID,
    Name,
    Total_Championships,
    Total_Race_Entries,
    Total_Race_Wins,
    Total_Points
FROM Driver;

-- Create View 2: ConstructorPerformance
CREATE VIEW ConstructorPerformance AS
SELECT
    Constructor_ID,
    Name,
    Total_Championships,
    Total_Race_Entries,
    Total_Race_Wins,
    Total_Points
FROM Constructor;

-- Query involving DriverStats view
SELECT * FROM DriverStats;

-- Query involving ConstructorPerformance view
SELECT * FROM ConstructorPerformance;

-- Attempt to modify DriverStats view
INSERT INTO DriverStats (Driver_ID, Name, Total_Championships, Total_Race_Entries, Total_Race_Wins, Total_Points)
VALUES (4, 'Charles Leclerc', 0, 0, 0, 0);

-- Attempt to modify ConstructorPerformance view
INSERT INTO ConstructorPerformance (Constructor_ID, Name, Total_Championships, Total_Race_Entries, Total_Race_Wins, Total_Points)
VALUES (4, 'McLaren', 0, 0, 0, 0);