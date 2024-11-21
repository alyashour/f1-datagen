from SRC.util import PrintableList

def sequential_id_gen(dflt=0):
    n = dflt
    while True:
        yield n
        n += 1

id = sequential_id_gen()

class Model:
    def __init__(self):
        self.id = next(id)

    @classmethod
    def generate(cls, n=1):
        return PrintableList([cls() for _ in range(n)])

    def __str__(self):
        attributes = vars(self)  # Get all instance attributes as a dictionary
        details = ", ".join(f"{key}: {value}" for key, value in attributes.items())
        return f"{self.__class__.__name__}:({details})"