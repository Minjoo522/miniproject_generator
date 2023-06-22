import random
from generators.generator import Generator

class GenderGenerator(Generator):
    def generate(self):
        return random.choice(["male", "female"])