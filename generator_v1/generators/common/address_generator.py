import random
from generators.generator import Generator

class AddressGenerator(Generator):
    cities = []
    gus = []
    roads = ["로", "길"]
    ADDRSS_MAX = 99

    def generate(self):
        city = random.choice(self.cities)
        gu = random.choice(self.gus)
        road = random.choice(self.roads)
        road_number1 = random.randint(1, self.ADDRSS_MAX)
        road_number2 = random.randint(1, self.ADDRSS_MAX)
        return f"{city} {gu} {road_number1}{road} {road_number2}"