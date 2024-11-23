from datetime import date
from faker import Faker

from data_generator.models.model import Model
from data_generator.config import *

fake = Faker()
fake.unique.clear()

MALE = 'M'
FEMALE = 'F'

def gen_date_in_year(year: int):
    return fake.date_between(date(year=year, month=1, day=1), date(year=year, month=12, day=31))

def gen_dod(dob):
    death_age = int(random.gauss(DRIVER_DEATH_AGE_AVG, DRIVER_DEATH_AGE_STD))
    death_year = int(dob.year + death_age)
    dod = gen_date_in_year(death_year)
    if dod <= date.today():
        return dod
    else:
        return None

def gen_dob(year: int | None = None):
    if year:
        dob = gen_date_in_year(year)
    else:
        dob = fake.date_of_birth(minimum_age=DRIVER_GEN_MIN_AGE, maximum_age=DRIVER_GEN_MAX_AGE)
    return dob

def gen_name(gender):
    if gender == 'M':
        return fake.name_male()
    elif gender == 'F':
        return fake.name_female()
    else:
        return fake.name_nonbinary()

class Driver(Model):
    def __init__(self):
        super().__init__()

        self.gender = fake.passport_gender()
        self.name = gen_name(self.gender)
        self.dob = gen_dob()
        self.dod = gen_dod(self.dob)
        self.country_of_birth = fake.country()
        self.total_championships=0
        self.total_race_entries=0
        self.total_race_wins=0
        self.total_points=0

        # lock the dob if it's been set in a second pass by the gen
        self.dates_locked = False

    @classmethod
    def generate(cls, n=1):
        l = super().generate(n)

        if len(l) > 0:
            l[0].name = 'Lewis Hamilton'
            l[0].gender = MALE
        if len(l) > 2:
            l[1].name = 'Sebastian Vettel'
            l[1].gender = MALE

        return l

    def get_age(self, year=date.today().year):
        return year - self.dob.year

    def is_active(self, year):
        """
        Returns true if the driver could be active in that year.
        That means age > min age and age < max age
        :param year:
        :return:
        """
        age = self.get_age(year)
        return ACTIVE_DRIVER_MIN_AGE < age < DRIVER_RETIRE_AGE

    def ensure_active(self, year):
        """
        Updates bod and dod to ensure that the driver is of age for that year.
        :param year: some int
        :return: True or False based on if the method was able to make the driver active.
        """
        # if the driver is already active, return True
        if self.is_active(year):
            return True

        # if the driver is inactive and we can't change their dates return False
        if self.dates_locked:
            return False

        # if we're able to change the dates make it true
        age = ACTIVE_DRIVER_MIN_AGE
        yob = year - age
        self.dob = gen_dob(yob)
        self.dod = gen_dod(self.dob)
        self.dates_locked = True
        return True

if __name__ == "__main__":
    drivers = Driver.generate(5)
    for driver in drivers:
        print(driver.name, driver.dob, driver.dod)