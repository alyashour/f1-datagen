from util import *

# HOW MANY MODELS THE GENERATOR MAKES
# DO NOT CHANGE UNLESS YOU KNOW WHAT YOU'RE DOING
MODEL_COUNT = 11 # DEFAULT 11

# HOW MUCH OF EACH SHOULD IT GENERATE
GENERATE_COUNTS = {
    DRIVERS: 775,  # DEFAULT 775
    CONSTRUCTORS: 200,  # DEFAULT 200
    SEASONS: 60,  # DEFAULT 100
    CIRCUITS: 100  # DEFAULT 100
}

# PIT STOP
PIT_STOP_MEAN_COUNT = 2
PIT_STOP_STD_DEVIATION = 0.6

# DRIVER
DRIVER_GEN_MIN_AGE = 18  # DEFAULT 18
DRIVER_GEN_MAX_AGE = 92  # DEFAULT 92
DRIVER_DEATH_AGE_AVG = 80  # DEFAULT 80
DRIVER_DEATH_AGE_STD = 0.2 # DEFAULT 0.2
ACTIVE_DRIVER_MIN_AGE = 18 # DEFAULT 18
DRIVER_RETIRE_AGE = 47 # DEFAULT 47

# SEASON
SEASON_MIN_YEAR = 1960  # DEFAULT 1960
SEASON_START_MONTH = '01'  # DEFAULT JANUARY
SEASON_START_DAY = '01'  # DEFAULT 1
SEASON_END_MONTH = '12'  # DEFAULT DECEMBER
SEASON_END_DAY = '31'  # DEFAULT 31
RACES_PER_SEASON = 3  # DEFAULT 20
DRIVERS_PER_RACE = 20  # DEFAULT 20
CONSTRUCTORS_PER_SEASON = int(DRIVERS_PER_RACE / 2)

# QUALIFYING
FASTEST_QUALIFYING_TIME_SECONDS = 92.726  # DEFAULT 92.726 (Charles LeClercs fastest time 2023)
MAX_QUALIFYING_LAP_TIME_VARIANCE_S = 15 # DEFAULT 15

# RACE RESULT
PIT_STOPS_VARIANCE = 2 # DEFAULT 2
AVG_PIT_STOPS_RANGE = (3, 5) # DEFAULT 3, 5

POINTS_LOOKUP = {
    1: 25,  # 1st place
    2: 18,  # 2nd place
    3: 15,  # 3rd place
    4: 12,  # 4th place
    5: 10,  # 5th place
    6: 8,  # 6th place
    7: 6,  # 7th place
    8: 4,  # 8th place
    9: 2,  # 9th place
    10: 1,  # 10th place
    11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
}
