import random

class NameGenerator:
    first_names = []
    last_names = []

    def generate(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        full_name = last_name + first_name
        return full_name