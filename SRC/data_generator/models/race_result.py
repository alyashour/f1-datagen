import random

from faker import Faker
from tqdm import tqdm

from data_generator.config import DRIVERS_PER_RACE, AVG_PIT_STOPS_RANGE, POINTS_LOOKUP, PIT_STOPS_VARIANCE
from data_generator.models.constructor import Constructor
from data_generator.models.driver import Driver
from data_generator.models.driver_entry import DriverEntry
from data_generator.models.grand_prix import GrandPrix
from data_generator.models.main_race import MainRace
from data_generator.models.model import Model
from data_generator.models.season import Season
from util import UtilList

fake = Faker()
fake.unique.clear()

def first(list, predicate):
    for item in list:
        if predicate(item):
            return item
    raise Exception('no items in list pass predicate')

# takes in some YYYY-MM-DD and returns YYYY
def get_year(date: str) -> int:
    return int(date.split('-')[0])

class RaceResult(Model):
    def __init__(self, race_id, driver_id, constructor_id, position,
                 points_gain_loss=None, total_pit_stops=None):
        super().__init__()
        self.race_id = race_id
        self.driver_id = driver_id
        self.constructor_id = constructor_id
        self.position = position
        if points_gain_loss is not None:
            self.points_gain_loss = points_gain_loss
        else:
            self.points_gain_loss = POINTS_LOOKUP[position]
        if total_pit_stops is None:
            self.total_pit_stops = fake.random_int(AVG_PIT_STOPS_RANGE[0], AVG_PIT_STOPS_RANGE[1]) + fake.random_int(0, PIT_STOPS_VARIANCE)
        else:
            self.total_pit_stops = total_pit_stops

    @classmethod
    def generate(cls, races=None, driver_entries=None, drivers=None, show_progress=False):
        l = UtilList()

        if drivers is None:
            drivers = Driver.generate(30)
        if races is None or driver_entries is None:
            seasons = Season.generate(1)
        if races is None:
            grand_prix = GrandPrix.generate(seasons=seasons)
            races = MainRace.generate(grand_prix=grand_prix)
        if driver_entries is None:
            # then generate the driver entries
            constructors = Constructor.generate(10)
            driver_entries = DriverEntry.generate(drivers=drivers, constructors=constructors, seasons=seasons)

        # create a cache for results to speed up processing time
        participating_driver_entries_cache = {}
        filtered_entries_cache = {}

        # for every race, ever
        for race in tqdm(races, desc="Processing Races", unit="race"):
            # get the drivers who raced that season
            if race.date.year not in participating_driver_entries_cache:
                participating_driver_entries_cache[race.date.year] = UtilList([entry for entry in driver_entries if get_year(entry.start_date) == race.date.year])
            participating_driver_entries = participating_driver_entries_cache[race.date.year]
            participating_drivers = UtilList([drivers[entry.driver_id - 1] for entry in participating_driver_entries])

            # make sure there are enough drivers
            assert len(participating_drivers) >= DRIVERS_PER_RACE, (f"Need more drivers to generate race results!\n"
                                                                    f"Participating Drivers: {participating_drivers}\n"
                                                                    f"Len: {len(participating_drivers)}\n"
                                                                    f"Need: {DRIVERS_PER_RACE}\n")

            positions = random.sample(range(1, DRIVERS_PER_RACE + 1), DRIVERS_PER_RACE)
            driver_index = participating_drivers.unique_random_index_gen()

            # calculate the entries for that year
            year = race.date.year
            if year not in filtered_entries_cache:
                filtered_entries_cache[year] = [entry for entry in driver_entries if entry.get_year() == year]
            filtered_entries = filtered_entries_cache[year]

            # for every driver in a race
            for i in range(DRIVERS_PER_RACE):
                driver = drivers[next(driver_index)]

                # try to find the drivers entry for that season
                while True:
                    try:
                        temp = [entry for entry in filtered_entries if entry.driver_id == driver.id]
                        driver_entry = temp[0]
                        break
                    except IndexError:
                        driver = drivers[next(driver_index)]

                l.append(RaceResult(
                    race_id=race.id,
                    driver_id=driver.id,
                    constructor_id=driver_entry.constructor_id,
                    position=positions.pop()
                ))

        return l

if __name__ == "__main__":
    print(RaceResult.generate())