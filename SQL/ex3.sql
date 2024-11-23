-- Simple INSERT Command
INSERT INTO Driver (Name, DOB, Gender, Country_of_Birth)
VALUES ('Lewis Hamilton', '1985-01-07', 'M', 'United Kingdom');

-- Select the last 10 rows, prioritizing the most recently inserted ones
SELECT *
FROM Driver
ORDER BY Driver_ID DESC -- Assuming Driver_ID is an auto-increment column
LIMIT 10;

-- INSERT ... SELECT Command
INSERT INTO Driver (Name, DOB, Gender, Country_of_Birth)
SELECT 'Sebastian Vettel', '1987-07-03', 'M', 'Germany'
FROM DUAL;

-- Select the last 10 rows, prioritizing the most recently inserted ones
SELECT *
FROM Driver
ORDER BY Driver_ID DESC
LIMIT 10;

-- INSERT ... ON DUPLICATE KEY UPDATE Command
INSERT INTO Driver (Driver_ID, Name, DOB, Gender, Country_of_Birth)
VALUES (1, 'Max Verstappen', '1997-09-30', 'Male', 'Netherlands')
ON DUPLICATE KEY UPDATE Name = 'Max Verstappen', DOB = '1997-09-30', Gender = 'M', Country_of_Birth = 'Netherlands';

-- Select the last 10 rows, prioritizing the most recently inserted or updated ones
SELECT *
FROM Driver
ORDER BY Driver_ID ASC
LIMIT 10;
