from enum import Enum
from random import random

from faker import Faker

from data_generator.config import RACES_PER_SEASON
from data_generator.models.model import Model
from data_generator.models.season import Season
from data_generator.models.circuit import Circuit
from util import UtilList


fake = Faker()
fake.unique.clear()

class QualifyingFormat(Enum):
    QUALIFYING = 'qualifying'
    SPRINT = 'sprint'

    def __str__(self):
        return self.value

def rand_format():
    n = random()
    if n < 0.9:
        return QualifyingFormat.QUALIFYING
    else:
        return QualifyingFormat.SPRINT

class GrandPrix(Model):
    def __init__(self, circuit_id, season_id, qual_id, race_id,
                 name=f'{fake.sentence(nb_words=2, variable_nb_words=True)[:-1].title()} GP',
                 qualifying_format=rand_format()):
        super().__init__()
        self.circuit_id = circuit_id
        self.season_id = season_id
        self.qual_id = qual_id
        self.race_id = race_id
        self.name = name
        self.qualifying_format = qualifying_format

    @classmethod
    def generate(cls, n=RACES_PER_SEASON, circuits=None, seasons=None):
        if circuits is None:
            circuits = Circuit.generate(20)
        if seasons is None:
            seasons = Season.generate(10)

        l = UtilList()
        assert len(circuits) >= RACES_PER_SEASON, 'Not enough circuits, cannot generate.'

        for season in seasons:
            count = 0
            for circuit in circuits:
                if count < n:
                    l.append(GrandPrix(
                        circuit_id=circuit.id,
                        season_id=season.id,
                        qual_id=None,
                        race_id=None
                    ))
                    count += 1
                else:
                    break

        return l

if __name__ == "__main__":
    s = Season.generate(1)
    print(GrandPrix.generate(seasons=s))