-- Update Pit Stops in Race Results
UPDATE RaceResult rr
SET Total_Pit_Stops = (
    SELECT COUNT(*)
    FROM PitStop ps
    WHERE ps.Race_ID = rr.Race_ID AND ps.Driver_ID = rr.Driver_ID
);

-- Update Season Winners
-- Driver Winner
UPDATE Season s
SET Driver_Winner = (
    SELECT Driver_ID
    FROM RaceResult rr
             JOIN MainRace mr ON rr.Race_ID = mr.Race_ID
             JOIN GrandPrix gp ON mr.GrandPrix_ID = gp.GrandPrix_ID
    WHERE gp.Season_ID = s.Season_ID
    GROUP BY Driver_ID
    ORDER BY SUM(rr.Points_Gain_Loss) DESC
    LIMIT 1
    );

-- Constructor Winner
UPDATE Season s
SET Constructor_Winner = (
    SELECT Constructor_ID
    FROM RaceResult rr
             JOIN MainRace mr ON rr.Race_ID = mr.Race_ID
             JOIN GrandPrix gp ON mr.GrandPrix_ID = gp.GrandPrix_ID
    WHERE gp.Season_ID = s.Season_ID
    GROUP BY Constructor_ID
    ORDER BY SUM(rr.Points_Gain_Loss) DESC
    LIMIT 1
    );

-- Update Driver Stats
UPDATE Driver d
SET Total_Race_Entries = (
    SELECT COUNT(*)
    FROM RaceResult rr
    WHERE rr.Driver_ID = d.Driver_ID
),
    Total_Race_Wins = (
        SELECT COUNT(*)
        FROM RaceResult rr
        WHERE rr.Driver_ID = d.Driver_ID AND rr.Position = 1
    ),
    Total_Points = (
        SELECT COALESCE(SUM(rr.Points_Gain_Loss), 0)
        FROM RaceResult rr
        WHERE rr.Driver_ID = d.Driver_ID
    ),
    Total_Championships = (
        SELECT COUNT(*)
        FROM Season s
        WHERE s.Driver_Winner = d.Driver_ID
    );

-- Update Constructor Stats
UPDATE Constructor c
SET Total_Race_Entries = (
    SELECT COUNT(*)
    FROM RaceResult rr
    WHERE rr.Constructor_ID = c.Constructor_ID
),
Total_Race_Wins = (
    SELECT COUNT(*)
    FROM RaceResult rr
    WHERE rr.Constructor_ID = c.Constructor_ID AND rr.Position = 1
),
Total_Points = (
    SELECT COALESCE(SUM(rr.Points_Gain_Loss), 0)
    FROM RaceResult rr
    WHERE rr.Constructor_ID = c.Constructor_ID
),
Total_Championships = (
    SELECT COUNT(*)
    FROM Season s
    WHERE s.Constructor_Winner = c.Constructor_ID
),
Date_of_First_Debut = (
    SELECT MIN(Start_Date)
    FROM DriverEntry de
    WHERE de.Constructor_ID = c.Constructor_ID
);