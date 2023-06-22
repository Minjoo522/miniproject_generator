import random
from generators.generator import Generator

class StoreNameGenerator(Generator):
    cafe_types = []
    cafe_districts = []
    
    def generate(self):
        cafe_type = random.choice(self.cafe_types)
        cafe_district = random.choice(self.cafe_districts)
        return f"{cafe_type} {cafe_district}{random.randint(1, 20)}호점"
