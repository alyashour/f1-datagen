from SRC.data_generator.config import *
from SRC.data_generator.models import *

def generate_all():
    # generate that which doesn't depend on anything first
    data = PrintableDict({
        DRIVERS: Driver.generate(GENERATE_COUNTS[DRIVERS]),
        CONSTRUCTORS: Constructor.generate(GENERATE_COUNTS[CONSTRUCTORS]),
        SEASONS: Season.generate(GENERATE_COUNTS[SEASONS]),
        CIRCUITS: Circuit.generate(GENERATE_COUNTS[CIRCUITS]),
    })

    return data

if __name__ == "__main__":
    data = generate_all()
    print(data)