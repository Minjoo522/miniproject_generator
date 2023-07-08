import random

from generators.common.load_data import first_names, last_names

class NameGenerator:
    def __init__(self):
        self.first_names = first_names
        self.last_names = last_names

    def generate(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        full_name = last_name + first_name
        return full_name