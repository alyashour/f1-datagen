-- Simple INSERT Command
INSERT INTO Driver (Name, DOB, Gender, Country_of_Birth)
VALUES ('Lewis Hamilton', '1985-01-07', 'Male', 'United Kingdom');

SELECT * FROM Driver;

-- INSERT ... SELECT Command
INSERT INTO Driver (Name, DOB, Gender, Country_of_Birth)
SELECT 'Sebastian Vettel', '1987-07-03', 'Male', 'Germany'
FROM DUAL;

SELECT * FROM Driver;

-- INSERT ... ON DUPLICATE KEY UPDATE Command
INSERT INTO Driver (Driver_ID, Name, DOB, Gender, Country_of_Birth)
VALUES (1, 'Max Verstappen', '1997-09-30', 'Male', 'Netherlands')
ON DUPLICATE KEY UPDATE Name = 'Max Verstappen', DOB = '1997-09-30', Gender = 'Male', Country_of_Birth = 'Netherlands';

-- Select all rows from Driver table to see the end result
SELECT * FROM Driver;
