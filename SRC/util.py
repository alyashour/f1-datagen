import random
from typing import List, Dict

QUALIFYING_RESULTS = 'qualifying_results'
QUALIFICATION_RACES = 'qualification_races'
DRIVERS = 'drivers'
DRIVER_ENTRIES = 'driver_entries'
CONSTRUCTORS = 'constructors'
MAIN_RACES = 'main_races'
SEASONS = 'seasons'
GRAND_PRIX = 'grand_prix'
CIRCUITS = 'circuits'
PIT_STOPS = 'pit_stops'
RACE_RESULTS = 'race_results'

class UtilList(List):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []

        super().__init__(iterable)

    def unique_random_index_gen(self):
        """Generator that yields unique random indices from a list."""
        indices = list(range(len(self)))  # Create a list of indices
        random.shuffle(indices)         # Shuffle the indices randomly

        for index in indices:           # Yield each index once
            yield index

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self) + "]"

class PrintableDict(Dict):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []

        super().__init__(iterable)

    def __str__(self):
        return "{" + ", ".join(f"\n\t{key}: {value}" for key, value in self.items()) + "\n}"
