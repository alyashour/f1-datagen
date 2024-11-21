from faker import Faker

from SRC.data_generator.config import DRIVERS_PER_RACE, FASTEST_QUALIFYING_TIME_SECONDS
from SRC.util import PrintableList
from util import Model
from SRC.data_generator.models.driver import Driver
from SRC.data_generator.models.qualification_race import QualificationRace

fake = Faker()
fake.unique.clear()

class DriverEntry(Model):
    def __init__(self, driver_id, qualifying_id, best_time, gap, position):
        super().__init__()
        self.driver_id = driver_id
        self.qualifying_id = qualifying_id
        self.best_time = best_time
        self.gap = gap
        self.position = position

    @classmethod
    def generate(cls, drivers=Driver.generate(20), races=QualificationRace.generate(10)):
        # we have to gen as many results as there are drivers per race * num of races
        n = DRIVERS_PER_RACE * len(races)
        l = PrintableList([])

        # make sure we have AT MINIMUM DRIVERS_PER_RACE drivers
        assert len(drivers) >= DRIVERS_PER_RACE, (f"Not enough drivers. Received {len(drivers)} but expected {DRIVERS_PER_RACE}, "
                                                  f"make sure to generate more before generating qualifying results. {drivers}")

        # for every qualifying race
        for qualifying_race in races:
            # pick a really fast time
            gap = 0
            lap_time = FASTEST_QUALIFYING_TIME_SECONDS + fake.random_int(min=0, max=15_000)/1000

            # randomly pick a driver
            dr_index_gen = drivers.unique_random_index_gen()
            position = 1
            for dr_index in dr_index_gen:
                driver = drivers[dr_index]

                # make a result
                l.append(QualifyingResult(
                    driver_id=driver.id,
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

                # calc the new position
                position += 1

        # check that all quals have a driver and qualifying
        for qual in l:
            assert qual.driver_id is not None
            assert qual.qualifying_id is not None
        assert len(l) == n

        return l

if __name__ == "__main__":
    drivers = Driver.generate(20)
    races = QualificationRace.generate(10)
    print(QualifyingResult.generate(drivers=drivers, races=races))