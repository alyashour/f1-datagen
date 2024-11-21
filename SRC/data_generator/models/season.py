from faker import Faker

from SRC.data_generator.models.util import Model
from SRC.data_generator.config import SEASON_MIN_YEAR as MIN_YEAR

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
        self.year = next(year)

if __name__ == "__main__":
    print(Season.generate(5))