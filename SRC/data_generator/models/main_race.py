from data_generator.config import SEASON_START_MONTH, SEASON_START_DAY
from data_generator.models.grand_prix import GrandPrix
from data_generator.models.model import Model
from util import UtilList

from datetime import date, timedelta

def _get_sundays(year: int):
    start_date = date(year, int(SEASON_START_MONTH), int(SEASON_START_DAY))

    # Find the first Sunday of the year
    days_to_sunday = (6 - start_date.weekday()) % 7
    first_sunday = start_date + timedelta(days=days_to_sunday)

    # Generate Sundays sequentially
    current_sunday = first_sunday
    while current_sunday.year == year:
        yield current_sunday
        current_sunday += timedelta(days=7)

class MainRace(Model):
    def __init__(self, grand_prix_id, date):
        super().__init__()
        self.grand_prix_id = grand_prix_id
        self.date = date

    @classmethod
    def generate(cls, n=1, grand_prix=None):
        if grand_prix is None:
            grand_prix = GrandPrix.generate(n)

        l = UtilList()

        gens = {}
        for gp in grand_prix:
            year = int(gp.season_id)
            if year not in gens:
                gens[year] = _get_sundays(year)
            l.append(MainRace(
                grand_prix_id=gp.id,
                date=next(gens[year])
            ))
        return l

if __name__ == "__main__":
    print(MainRace.generate())