from data_generator.config import *
from data_generator.models import *
from data_generator.models.race_result import RaceResult
from util import PrintableDict


def generate_all():
    # generate that which doesn't depend on anything first
    print('generating base data...')
    data = PrintableDict({
        DRIVERS: Driver.generate(GENERATE_COUNTS[DRIVERS]),
        CONSTRUCTORS: Constructor.generate(GENERATE_COUNTS[CONSTRUCTORS]),
        SEASONS: Season.generate(GENERATE_COUNTS[SEASONS]),
        CIRCUITS: Circuit.generate(GENERATE_COUNTS[CIRCUITS]),
    })

    # generate first level data
    # includes driverEntries, and grand prix
    print('generating first class data...')
    data[DRIVER_ENTRIES] = DriverEntry.generate(
        drivers=data[DRIVERS],
        constructors=data[CONSTRUCTORS],
        seasons=data[SEASONS],
    )
    data[GRAND_PRIX] = GrandPrix.generate(
        circuits=data[CIRCUITS],
        seasons=data[SEASONS]
    )

    # generate second level data
    # includes qualifying race, and main race
    print('generating second class data...')
    data[QUALIFICATION_RACES] = QualificationRace.generate(
        grand_prix=data[GRAND_PRIX]
    )
    data[MAIN_RACES] = MainRace.generate(
        grand_prix=data[GRAND_PRIX]
    )

    # generate third level data
    # includes qualifying result and race results
    print('generating third class data...')
    data[QUALIFYING_RESULTS] = QualifyingResult.generate(
        driver_entries=data[DRIVER_ENTRIES],
        qualifying_races=data[QUALIFICATION_RACES],
        show_progress=True
    )
    data[RACE_RESULTS] = RaceResult.generate(
        races=data[MAIN_RACES],
        driver_entries=data[DRIVER_ENTRIES],
        drivers=data[DRIVERS],
        show_progress=True
    )

    # generate fourth level data
    # includes pit stops
    data[PIT_STOPS] = PitStop.generate(
        race_results=data[RACE_RESULTS]
    )

    print('Done generating data!')
    return data

if __name__ == "__main__":
    data = generate_all()
    print(data)