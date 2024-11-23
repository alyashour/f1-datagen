from faker import Faker

from data_generator.models.model import Model
from data_generator.config import SEASON_MIN_YEAR as MIN_YEAR

fake = Faker()
fake.unique.clear()

def year_gen(start=MIN_YEAR):
    y = start
    while True:
        yield y
        y += 1

year = year_gen()

class Season(Model):
    def __init__(self):
        super().__init__()
        self.id = next(year)

        self.driver_winner = 1
        self.constructor_winner = 1

    def get_year(self):
        return self.id

if __name__ == "__main__":
    print(Season.generate(5))