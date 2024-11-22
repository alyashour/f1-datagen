from datetime import date
from faker import Faker

from data_generator.models.model import Model
from data_generator.config import *

fake = Faker()
fake.unique.clear()

class Driver(Model):
    def __init__(self):
        super().__init__()
        self.name=fake.name()
        self.dob=fake.date_of_birth(minimum_age=DRIVER_GEN_MIN_AGE, maximum_age=DRIVER_GEN_MAX_AGE)
        dod = self.dob.replace(year=self.dob.year + DRIVER_GEN_DEATH_AGE)
        self.dod= dod if dod < date.today() else None
        self.gender=fake.passport_gender()
        self.country_of_birth=fake.country()
        # todo: come back and gen these instead of assigning them
        # self.total_championships=fake.random_int(0, DRIVER_GEN_MAXIMUM_CHAMPIONSHIPS)
        # self.total_race_entries=fake.random_int(0, DRIVER_GEN_MAX_TOTAL_RACE_ENTRIES)
        # self.total_race_wins=fake.random_int(0, DRIVER_GEN_MAX_RACE_WINS)
        # self.total_points=fake.random_int(0, DRIVER_GEN_MAX_POINTS)
        self.total_championships=0
        self.total_race_entries=0
        self.total_race_wins=0
        self.total_points=0

if __name__ == "__main__":
    drivers = Driver.generate(5)
    print(drivers)