from faker import Faker

from SRC.data_generator.models.model import Model

fake = Faker()
fake.unique.clear()

class Constructor(Model):
    def __init__(self):
        super().__init__()
        self.country = fake.country()
        self.name = (fake.unique.sentence(2)).title()[:-1] # [:-1] is to remove the period
        self.date_of_first_debut = fake.date_between_dates()


if __name__ == "__main__":
    print(Constructor())