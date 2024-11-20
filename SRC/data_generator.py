# Fake data generation can be completed here. We can use a library called faker if we agree on it.

from faker import Faker #! We can use this library to generate fake data, just an idea; it's not necessary
import csv

fake = Faker()

# with open("fake_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Date of Birth", "Country"])
#     for _ in range(100):
#         writer.writerow([fake.name(), fake.date_of_birth(), fake.country()])