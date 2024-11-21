from faker import Faker

from SRC.data_generator.models.util import Model, sequential_id_gen

fake = Faker()
fake.unique.clear()

class QualificationRace(Model):
    def __init__(self):
        super().__init__()
        self.country = fake.country()
        self.name = (fake.unique.sentence(3)).title()[:-1]
        self.date_of_first_debut = fake.date_between_dates()

if __name__ == "__main__":
    print(QualificationRace.generate(5))