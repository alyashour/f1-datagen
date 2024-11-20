-- Insert statments for any tables for loading the data can be done here.

-- Load data into Circuit table
INSERT INTO `Circuit` (`Name`, `Country`) VALUES
('Silverstone', 'United Kingdom'),
('Monza', 'Italy'),
('Spa-Francorchamps', 'Belgium'),
('Suzuka', 'Japan'),
('Interlagos', 'Brazil');

-- Load data into Season table
INSERT INTO `Season` (`Driver Winner`, `Constructor Winner`) VALUES
('Lewis Hamilton', 'Mercedes'),
('Max Verstappen', 'Red Bull Racing'),
('Sebastian Vettel', 'Ferrari');

-- Load data into Grand Prix table
INSERT INTO `Grand Prix` (`Circuit ID`, `Season ID`, `Name`, `Qualifying Format`) VALUES
(1, 1, 'British Grand Prix', 'Standard'),
(2, 2, 'Italian Grand Prix', 'Standard'),
(3, 3, 'Belgian Grand Prix', 'Sprint');

-- Load data into Qualification Race table
INSERT INTO `Qualification Race` (`Grand Prix ID`, `Date`) VALUES
(1, '2024-03-15'),
(2, '2024-04-01'),
(3, '2024-05-20');

-- Load data into Main Race table
INSERT INTO `Main Race` (`Grand Prix ID`, `Date`) VALUES
(1, '2024-03-16'),
(2, '2024-04-02'),
(3, '2024-05-21');

-- Load data into Driver table
INSERT INTO `Driver` (`Name`, `Date of Birth`, `Gender`, `Country of Birth`, `Total Championships`, `Total Race Entries`, `Total Race Wins`, `Total Points`) VALUES
('Lewis Hamilton', '1985-01-07', 'Male', 'United Kingdom', 7, 300, 103, 4200),
('Max Verstappen', '1997-09-30', 'Male', 'Netherlands', 2, 180, 47, 2300),
('Charles Leclerc', '1997-10-16', 'Male', 'Monaco', 0, 90, 7, 750);

-- Load data into Constructor table
INSERT INTO `Constructor` (`Name`, `Country`, `Date of First Debut`, `Total Championships`, `Total Race Entries`, `Total Race Wins`, `Total Points`) VALUES
('Mercedes', 'Germany', '2010-03-14', 8, 300, 120, 5200),
('Red Bull Racing', 'Austria', '2005-03-06', 6, 350, 100, 4800),
('Ferrari', 'Italy', '1950-05-13', 16, 1000, 240, 7800);

-- Load data into Driver Entry table
INSERT INTO `Driver Entry` (`Driver ID`, `Constructor ID`, `Start Date`, `End Date`, `Driver Role`) VALUES
(1, 1, '2013-03-01', '2024-12-31', 'Lead Driver'),
(2, 2, '2016-03-01', '2024-12-31', 'Lead Driver'),
(3, 3, '2018-03-01', '2024-12-31', 'Lead Driver');

-- Load data into Qualifying Result table
INSERT INTO `Qualifying Result` (`Driver ID`, `Qual ID`, `Best Time`, `Gap`, `Position`) VALUES
(1, 1, '01:18:23', '00:00:00', 1),
(2, 1, '01:18:45', '00:00:22', 2),
(3, 1, '01:19:10', '00:00:47', 3);

-- Load data into Race Result table
INSERT INTO `Race Result` (`Race ID`, `Driver ID`, `Position`, `Points Gain/Loss`, `Total Pit Stops`) VALUES
(1, 1, 1, 25, 2),
(1, 2, 2, 18, 3),
(1, 3, 3, 15, 2);

-- Load data into Pit Stop table
INSERT INTO `Pit Stop` (`Race ID`, `Driver ID`, `Lap Number`, `Time in Pit`) VALUES
(1, 1, 10, '00:25:34'),
(1, 2, 12, '00:28:50'),
(1, 3, 15, '00:30:12');

-- Example SELECT commands to verify data
SELECT * FROM `Driver`;
SELECT * FROM `Grand Prix`;
SELECT * FROM `Qualifying Result`;
