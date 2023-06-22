import random
from generators.generator import Generator

class NameGenerator(Generator):
    first_names = []
    last_names = []

    def generate(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return last_name + first_name