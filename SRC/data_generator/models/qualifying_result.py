from faker import Faker
from tqdm import tqdm

from SRC.data_generator.config import DRIVERS_PER_RACE, FASTEST_QUALIFYING_TIME_SECONDS
from SRC.data_generator.models import DriverEntry, Constructor, GrandPrix, Circuit
from SRC.data_generator.models.season import Season
from SRC.data_generator.models.model import Model
from SRC.data_generator.models.driver import Driver
from SRC.data_generator.models.qualification_race import QualificationRace
from SRC.util import UtilList

fake = Faker()
fake.unique.clear()

def seconds_to_time(seconds):
    # Extract hours, minutes, and seconds
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)  # Fractional seconds as milliseconds

    # Format to HH:MM:SS.mmm
    return f"{hours:02}:{minutes:02}:{secs:02}.{milliseconds:03}"

class QualifyingResult(Model):
    def __init__(self, driver_id, constructor_id, qualifying_id, best_time, gap, position):
        super().__init__()
        self.driver_id = driver_id
        self.constructor_id = constructor_id
        self.qualifying_id = qualifying_id
        self.best_time = best_time
        self.gap = gap
        self.position = position

    @classmethod
    def generate(cls, driver_entries=None, qualifying_races=None, show_progress=False):
        if qualifying_races is None or driver_entries is None:
            seasons = Season.generate(5)
            circuits = Circuit.generate(25)
            grand_prix = GrandPrix.generate(10, circuits=circuits, seasons=seasons)
            qualifying_races = QualificationRace.generate(10, grand_prix=grand_prix)
            drivers = Driver.generate(40)
            constructors = Constructor.generate(10)
            driver_entries = DriverEntry.generate(drivers=drivers, constructors=constructors, seasons=seasons)

        # we have to gen as many results as there are drivers per race * num of races
        n = DRIVERS_PER_RACE * len(qualifying_races)
        l = UtilList()

        # for every qualifying race
        for qualifying_race in tqdm(qualifying_races, desc="Processing Qualifying Races", unit="race"):
            # get the available drivers
            applicable_driver_entries: UtilList[DriverEntry] = DriverEntry.get_seasons_drivers(driver_entries, qualifying_race.get_season_id())

            # make sure we have AT MINIMUM DRIVERS_PER_RACE drivers
            assert len(applicable_driver_entries) >= DRIVERS_PER_RACE, (f"Not enough drivers. Received {len(applicable_driver_entries)} but expected {DRIVERS_PER_RACE}, "
                                                      f"make sure to generate more before generating qualifying results. {applicable_driver_entries}")


            # pick a really fast time
            gap = 0
            lap_time = FASTEST_QUALIFYING_TIME_SECONDS + fake.random_int(min=0, max=15_000)/1000

            # randomly pick a driver
            de_index_gen = applicable_driver_entries.unique_random_index_gen()
            position = 1
            for dr_index in de_index_gen:
                driver_entry = applicable_driver_entries[dr_index]

                # make a result
                l.append(QualifyingResult(
                    driver_id=driver_entry.driver_id,
                    constructor_id=driver_entry.constructor_id,
                    qualifying_id=qualifying_race.id,
                    best_time=seconds_to_time(lap_time),
                    gap=gap,
                    position=position
                ))

                # find a dt (0 <= dt <= 300/20 s)
                # 300/20s = 15s -> 5-minute avg spread from first to last
                # calc the new gap
                gap = fake.random_int(min=0, max=15_000)/1000

                # calc the new lap time
                lap_time += gap

                # calc the next position
                position += 1

                if position > 20:
                    break

        # check that all quals have a driver and qualifying
        for qual in l:
            assert qual.driver_id is not None
            assert qual.qualifying_id is not None
        assert len(l) == n, f'{len(l)} : {n}'

        return l

if __name__ == "__main__":
    print(QualifyingResult.generate())