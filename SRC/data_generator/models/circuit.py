from faker import Faker

from SRC.data_generator.models.model import Model

fake = Faker()
fake.unique.clear()

class Circuit(Model):
    def __init__(self):
        super().__init__()
        self.name = fake.sentence(nb_words=3, variable_nb_words=True)[:-1]
        self.country = fake.country()

if __name__ == "__main__":
    print(Circuit.generate(5))