import random

from generators.common.load_data import cities, gus

class AddressGenerator():
    def __init__(self):
        self.cities = cities
        self.gus = gus
        self.roads = ["로", "길"]
        self.ADDRESS_MAX = 99

    def generate(self):
        city = random.choice(self.cities)
        gu = random.choice(self.gus)
        road = random.choice(self.roads)
        road_number = random.randint(1, self.ADDRESS_MAX)
        building_number = random.randint(1, self.ADDRESS_MAX)
        full_address = f"{city} {gu} {road_number}{road} {building_number}"
        return full_address