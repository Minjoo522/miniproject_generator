import random

class GenderGenerator:
    def generate(self):
        gender = random.choice(["Male", "Female"])
        return gender