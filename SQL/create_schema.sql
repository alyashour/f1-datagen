-- Creating tables

CREATE TABLE `Qualifying Result` (
    `Qual Result ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Driver ID` INT,
    `Qual ID` INT,
    `Best Time` TIME,
    `Gap` TIME,
    `Position` TINYINT
);

CREATE TABLE `Qualification Race` (
    `Qual ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Grand Prix ID` INT,
    `Date` DATE
);

CREATE TABLE `Driver` (
    `Driver ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255),
    `Date of Birth` DATE,
    `Date of Death` DATE,
    `Gender` VARCHAR(255),
    `Country of Birth` VARCHAR(255),
    `Total Championships` INT,
    `Total Race Entries` INT,
    `Total Race Wins` INT,
    `Total Points` INT
);

CREATE TABLE `Driver Entry` (
    `Driver Entry ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Driver ID` INT,
    `Constructor ID` INT,
    `Start Date` DATE,
    `End Date` DATE,
    `Driver Role` VARCHAR(255)
);

CREATE TABLE `Constructor` (
    `Constructor ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Country` VARCHAR(255),
    `Name` VARCHAR(255),
    `Date of First Debut` DATE,
    `Total Championships` INT,
    `Total Race Entries` INT,
    `Total Race Wins` INT,
    `Total Points` INT
);

CREATE TABLE `Main Race` (
    `Race ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Grand Prix ID` INT,
    `Date` DATE
);

CREATE TABLE `Season` (
    `Season ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Driver Winner` VARCHAR(255),
    `Constructor Winner` VARCHAR(255)
);

CREATE TABLE `Grand Prix` (
    `Grand Prix ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Circuit ID` INT,
    `Season ID` INT,
    `Qual ID` INT,
    `Race ID` INT,
    `Name` VARCHAR(255),
    `Qualifying Format` VARCHAR(255)
);

CREATE TABLE `Circuit` (
    `Circuit ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255),
    `Country` VARCHAR(255)
);

CREATE TABLE `Pit Stop` (
    `Pit Stop ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Race ID` INT,
    `Driver ID` INT,
    `Lap Number` TINYINT,
    `Time in Pit` TIME
);

CREATE TABLE `Race Result` (
    `Race Result ID` INT AUTO_INCREMENT PRIMARY KEY,
    `Race ID` INT,
    `Driver ID` INT,
    `Position` TINYINT,
    `Points Gain/Loss` TINYINT,
    `Total Pit Stops` TINYINT
);

-- Adding relationships

ALTER TABLE `Qualifying Result`
ADD CONSTRAINT FK_QualifyingResult_Qual
FOREIGN KEY (`Qual ID`) REFERENCES `Qualification Race`(`Qual ID`),
ADD CONSTRAINT FK_QualifyingResult_Driver
FOREIGN KEY (`Driver ID`) REFERENCES `Driver`(`Driver ID`);

ALTER TABLE `Qualification Race`
ADD CONSTRAINT FK_QualificationRace_GrandPrix
FOREIGN KEY (`Grand Prix ID`) REFERENCES `Grand Prix`(`Grand Prix ID`);

ALTER TABLE `Grand Prix`
ADD CONSTRAINT FK_GrandPrix_Circuit
FOREIGN KEY (`Circuit ID`) REFERENCES `Circuit`(`Circuit ID`),
ADD CONSTRAINT FK_GrandPrix_Season
FOREIGN KEY (`Season ID`) REFERENCES `Season`(`Season ID`),
ADD CONSTRAINT FK_GrandPrix_Qual
FOREIGN KEY (`Qual ID`) REFERENCES `Qualification Race`(`Qual ID`),
ADD CONSTRAINT FK_GrandPrix_Race
FOREIGN KEY (`Race ID`) REFERENCES `Main Race`(`Race ID`);

ALTER TABLE `Main Race`
ADD CONSTRAINT FK_MainRace_GrandPrix
FOREIGN KEY (`Grand Prix ID`) REFERENCES `Grand Prix`(`Grand Prix ID`);

ALTER TABLE `Pit Stop`
ADD CONSTRAINT FK_PitStop_Race
FOREIGN KEY (`Race ID`) REFERENCES `Main Race`(`Race ID`),
ADD CONSTRAINT FK_PitStop_Driver
FOREIGN KEY (`Driver ID`) REFERENCES `Driver`(`Driver ID`);

ALTER TABLE `Race Result`
ADD CONSTRAINT FK_RaceResult_Race
FOREIGN KEY (`Race ID`) REFERENCES `Main Race`(`Race ID`),
ADD CONSTRAINT FK_RaceResult_Driver
FOREIGN KEY (`Driver ID`) REFERENCES `Driver`(`Driver ID`);

ALTER TABLE `Driver Entry`
ADD CONSTRAINT FK_DriverEntry_Driver
FOREIGN KEY (`Driver ID`) REFERENCES `Driver`(`Driver ID`),
ADD CONSTRAINT FK_DriverEntry_Constructor
FOREIGN KEY (`Constructor ID`) REFERENCES `Constructor`(`Constructor ID`);
