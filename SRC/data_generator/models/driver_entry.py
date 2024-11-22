from faker import Faker

from data_generator.config import SEASON_START_MONTH, SEASON_START_DAY, SEASON_END_MONTH, SEASON_END_DAY
from data_generator.models.constructor import Constructor
from data_generator.models.driver import Driver
from data_generator.models.model import Model
from data_generator.models.season import Season
from util import UtilList

fake = Faker()
fake.unique.clear()

PRIMARY = 'primary'
SECONDARY = 'secondary'
RESERVE = 'reserve'

class DriverEntry(Model):
    def __init__(self, driver_id, constructor_id, start_date, end_date, driver_role):
        super().__init__()
        self.driver_id = driver_id
        self.constructor_id = constructor_id
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.driver_role = driver_role

        self.season_id = self.get_year()

    def get_year(self):
        return int(self.start_date.split('-')[0])

    @classmethod
    def get_seasons_drivers(cls, entries, season_id):
        l = [entry for entry in entries if entry.season_id == season_id]
        return UtilList(l)

    @classmethod
    def generate(cls, drivers=None, constructors=None, seasons=None):
        if drivers is None:
            drivers = Driver.generate(30)
        if constructors is None:
            constructors = Constructor.generate(10)
        if seasons is None:
            seasons = Season.generate(10)

        l = UtilList()

        # have to be at least 3 drivers per constructor
        assert len(drivers) >= len(constructors) * 3, ("Not enough drivers. "
                                                       "Please make sure there are at least 3 drivers per team to generate. "
                                                       f"Received {len(drivers)} need {len(constructors) * 3}")

        # loop over all years
        for season in seasons:
            driver_id = drivers.unique_random_index_gen()
            for constructor in constructors:
                primary_driver: Driver= drivers[next(driver_id)]
                secondary_driver: Driver = drivers[next(driver_id)]
                reserve_driver: Driver = drivers[next(driver_id)]

                l.append(DriverEntry(
                    driver_id=primary_driver.id,
                    constructor_id=constructor.id,
                    start_date=f'{season.id}-{SEASON_START_MONTH}-{SEASON_START_DAY}',
                    end_date=f'{season.id}-{SEASON_END_MONTH}-{SEASON_END_DAY}',
                    driver_role=PRIMARY
                ))

                l.append(DriverEntry(
                    driver_id=secondary_driver.id,
                    constructor_id=constructor.id,
                    start_date=f'{season.id}-{SEASON_START_MONTH}-{SEASON_START_DAY}',
                    end_date=f'{season.id}-{SEASON_END_MONTH}-{SEASON_END_DAY}',
                    driver_role=SECONDARY
                ))

                l.append(DriverEntry(
                    driver_id=reserve_driver.id,
                    constructor_id=constructor.id,
                    start_date=f'{season.id}-{SEASON_START_MONTH}-{SEASON_START_DAY}',
                    end_date=f'{season.id}-{SEASON_END_MONTH}-{SEASON_END_DAY}',
                    driver_role=RESERVE
                ))
        return l

if __name__ == "__main__":
    print(DriverEntry.generate())