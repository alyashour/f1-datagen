from datetime import date
from faker import Faker
from dateutil.relativedelta import relativedelta

from SRC.data_generator.models.util import Model, sequential_id_gen

fake = Faker()
fake.unique.clear()

id = sequential_id_gen()

class Driver(Model):
    def __init__(self):
        self.id = next(id)
        self.name=fake.name()
        self.dob=fake.date_of_birth(minimum_age=18, maximum_age=92)
        dod = self.dob.replace(year=self.dob.year + 80)
        dt = relativedelta(date.today(), self.dob).years
        self.dod= self.dob.replace(year=self.dob.year + 80) if dod < date.today() else None
        self.gender=fake.passport_gender()
        self.country_of_birth=fake.country()
        self.total_championships=fake.random_int(0, 2)
        self.total_race_entries=fake.random_int(0, 2)
        self.total_race_wins=fake.random_int(0, 105)
        self.total_points=fake.random_int(0, 5000)

if __name__ == "__main__":
    l = Driver.generate(n=5)
    for d in l:
        print(d)