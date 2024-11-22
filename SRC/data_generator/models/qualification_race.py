from datetime import date, timedelta

from faker import Faker

from data_generator.config import SEASON_START_MONTH, SEASON_START_DAY
from data_generator.models.model import Model
from data_generator.models.grand_prix import GrandPrix
from util import UtilList


fake = Faker()
fake.unique.clear()

def _get_saturdays(year):
    start_date = date(year, int(SEASON_START_MONTH), int(SEASON_START_DAY))

    # Find the first Sunday of the year
    days_to_saturday = (5 - start_date.weekday()) % 7
    first_saturday = start_date + timedelta(days=days_to_saturday)

    # Generate Sundays sequentially
    current_saturday = first_saturday
    while current_saturday.year == year:
        yield current_saturday
        current_saturday += timedelta(days=7)

class QualificationRace(Model):
    def __init__(self, grand_prix_id, date: date):
        super().__init__()
        self.grand_prix_id = grand_prix_id
        self.date: date = date

    def get_year(self):
        return self.date.year

    def get_season_id(self):
        return self.get_year()

    @classmethod
    def generate(cls, n=1, grand_prix=None):
        if grand_prix is None:
            grand_prix = GrandPrix.generate(n)

        l = UtilList()
        for gp in grand_prix:
            gen = _get_saturdays(gp.season_id)
            race = QualificationRace(
                grand_prix_id=gp.id,
                date=next(gen)
            )

            l.append(race)

            # also update gp
            gp.qual_id = race.id
        return l

if __name__ == "__main__":
    print(QualificationRace.generate(5))