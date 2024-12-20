from faker import Faker

from data_generator.models.model import Model

fake = Faker()
fake.unique.clear()

def _gen_name():
    return (fake.unique.sentence(2)).title()[:-1] # [:-1] is to remove the period

class Constructor(Model):
    def __init__(self):
        super().__init__()
        self.country = fake.country()
        self.name = _gen_name()
        self.date_of_first_debut = fake.date_between_dates()
        self.total_championships = 0
        self.total_race_entries = 0
        self.total_race_wins = 0
        self.total_points = 0
        
    @classmethod
    def generate(cls, n=1):
        l = super().generate(n)
        if len(l) > 0:
            l[0].name = 'Mercedes'
        if len(l) > 1:
            l[1].name = 'Ferrari'
        return l



if __name__ == "__main__":
    print(Constructor.generate(5))
    