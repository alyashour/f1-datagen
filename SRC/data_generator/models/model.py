from util import UtilList

def sequential_id_gen(dflt=1):
    n = dflt
    while True:
        yield n
        n += 1

class Model:
    _id_counters = {}
    def __init__(self):
        cls = self.__class__
        if cls not in Model._id_counters:
            Model._id_counters[cls] = sequential_id_gen()
        self.id = next(Model._id_counters[cls])

    @classmethod
    def generate(cls, n=1):
        return UtilList([cls() for _ in range(n)])

    def __str__(self):
        attributes = vars(self)  # Get all instance attributes as a dictionary
        details = ", ".join(f"{key}: {value}" for key, value in attributes.items())
        return f"{self.__class__.__name__}:({details})"