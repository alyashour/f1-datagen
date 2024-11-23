from datetime import date

from util import SEASONS
from .config import SEASON_MIN_YEAR, GENERATE_COUNTS, CONSTRUCTORS_PER_SEASON, DRIVERS_PER_RACE
from .generate import generate_all

__all__ = ["generate_all"]


# ASSERT CONFIG INTEGRITY
# make sure we dont generate into the future
assert GENERATE_COUNTS[SEASONS] + SEASON_MIN_YEAR <= date.today().year, ("GEN CANNOT GENERATE INTO THE FUTURE, PLEASE GEN LESS YEARS"
                                                                         "OR SET MIN YEAR TO LOWER VALUE")

assert DRIVERS_PER_RACE == CONSTRUCTORS_PER_SEASON * 2, "There must be exactly 2x as many constructors per season as there were drivers."