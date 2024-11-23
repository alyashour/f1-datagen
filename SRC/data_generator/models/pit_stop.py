import random

from data_generator.config import PIT_STOP_MEAN_COUNT, PIT_STOP_STD_DEVIATION
from data_generator.models.race_result import RaceResult
from data_generator.models.model import Model
from util import UtilList

LAPS = 55

def _random_pit_time():
    t = random.gauss(PIT_STOP_MEAN_COUNT, PIT_STOP_STD_DEVIATION)
    return round(t, 6)

class PitStop(Model):
    def __init__(self, race_id, driver_id, lap_number, time_in_pit):
        super().__init__()
        self.race_id = race_id
        self.driver_id = driver_id
        self.lap_number = lap_number
        self.time_in_pit = time_in_pit

    @classmethod
    def generate(cls, n=1, race_results=None):
        if race_results is None:
            race_results = RaceResult.generate()

        l = UtilList()
        for race_result in race_results:
            pit_stop_laps=random.sample(range(1, LAPS + 1), race_result.total_pit_stops)
            for i in range(race_result.total_pit_stops):
                l.append(PitStop(
                    race_id=race_result.race_id,
                    driver_id=race_result.driver_id,
                    lap_number=pit_stop_laps.pop(),
                    time_in_pit=_random_pit_time()
                ))

        return l

if __name__ == "__main__":
    # print(PitStop.generate(1))
    for i in range(10):
        print(_random_pit_time())