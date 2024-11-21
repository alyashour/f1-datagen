-- Create Circuit table
CREATE TABLE Circuit (
    Circuit_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL
);
DESCRIBE Circuit;

-- Create Season table
CREATE TABLE Season (
    Season_ID INT AUTO_INCREMENT PRIMARY KEY,
    Driver_Winner INT,
    Constructor_Winner INT,
    FOREIGN KEY (Driver_Winner) REFERENCES Driver(Driver_ID),
    FOREIGN KEY (Constructor_Winner) REFERENCES Constructor(Constructor_ID)
);
DESCRIBE Season;

-- Create Grand Prix table
CREATE TABLE GrandPrix (
    GrandPrix_ID INT AUTO_INCREMENT PRIMARY KEY,
    Circuit_ID INT NOT NULL,
    Season_ID INT NOT NULL,
    Qual_ID INT,
    Race_ID INT,
    Name VARCHAR(255) NOT NULL,
    Qualifying_Format VARCHAR(50),
    FOREIGN KEY (Circuit_ID) REFERENCES Circuit(Circuit_ID),
    FOREIGN KEY (Season_ID) REFERENCES Season(Season_ID)
);
DESCRIBE GrandPrix;

-- Create Driver table
CREATE TABLE Driver (
    Driver_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    DOB DATE NOT NULL,
    DOD DATE,
    Gender VARCHAR(50) NOT NULL,
    Country_of_Birth VARCHAR(255),
    Total_Championships INT,
    Total_Race_Entries INT,
    Total_Race_Wins INT,
    Total_Points INT
);
DESCRIBE Driver;

-- Create Constructor table
CREATE TABLE Constructor (
    Constructor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Country VARCHAR(255) NOT NULL,
    Date_of_First_Debut DATE,
    Total_Championships INT,
    Total_Race_Entries INT,
    Total_Race_Wins INT,
    Total_Points INT
);
DESCRIBE Constructor;

-- Create Qualification Race table
CREATE TABLE QualificationRace (
    Qual_ID INT AUTO_INCREMENT PRIMARY KEY,
    GrandPrix_ID INT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (GrandPrix_ID) REFERENCES GrandPrix(GrandPrix_ID)
);
DESCRIBE QualificationRace;

-- Create Qualifying Result table
CREATE TABLE QualifyingResult (
    QualResult_ID INT AUTO_INCREMENT PRIMARY KEY,
    Driver_ID INT NOT NULL,
    Qual_ID INT NOT NULL,
    Best_Time TIME,
    Gap TIME,
    Position TINYINT,
    FOREIGN KEY (Driver_ID) REFERENCES Driver(Driver_ID),
    FOREIGN KEY (Qual_ID) REFERENCES QualificationRace(Qual_ID)
);
DESCRIBE QualifyingResult;

-- Create Main Race table
CREATE TABLE MainRace (
    Race_ID INT AUTO_INCREMENT PRIMARY KEY,
    GrandPrix_ID INT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (GrandPrix_ID) REFERENCES GrandPrix(GrandPrix_ID)
);
DESCRIBE MainRace;

-- Create Race Result table
CREATE TABLE RaceResult (
    RaceResult_ID INT AUTO_INCREMENT PRIMARY KEY,
    Race_ID INT NOT NULL,
    Driver_ID INT NOT NULL,
    Constructor_ID INT NOT NULL,
    Position TINYINT,
    Points_Gain_Loss TINYINT,
    Total_Pit_Stops TINYINT,
    FOREIGN KEY (Race_ID) REFERENCES MainRace(Race_ID),
    FOREIGN KEY (Driver_ID) REFERENCES Driver(Driver_ID),
    FOREIGN KEY (Constructor_ID) REFERENCES Constructor(Constructor_ID)
);
DESCRIBE RaceResult;

-- Create Pit Stop table
CREATE TABLE PitStop (
    PitStop_ID INT AUTO_INCREMENT PRIMARY KEY,
    Race_ID INT NOT NULL,
    Driver_ID INT NOT NULL,
    Lap_Number TINYINT,
    Time_in_Pit TIME,
    FOREIGN KEY (Race_ID) REFERENCES MainRace(Race_ID),
    FOREIGN KEY (Driver_ID) REFERENCES Driver(Driver_ID)
);
DESCRIBE PitStop;

-- Create Driver Entry table
CREATE TABLE DriverEntry (
    DriverEntry_ID INT AUTO_INCREMENT PRIMARY KEY,
    Driver_ID INT NOT NULL,
    Constructor_ID INT NOT NULL,
    Start_Date DATE NOT NULL,
    End_Date DATE,
    Driver_Role VARCHAR(50),
    FOREIGN KEY (Driver_ID) REFERENCES Driver(Driver_ID),
    FOREIGN KEY (Constructor_ID) REFERENCES Constructor(Constructor_ID)
);
DESCRIBE DriverEntry;

-- Display all tables in the database
SHOW TABLES;
