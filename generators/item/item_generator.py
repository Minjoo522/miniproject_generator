import uuid
import random
from generators.generator import Generator

class ItemGenerator(Generator):
    menus = []
    id = uuid.uuid4()

    def generate(self):
        item = [str(self.id)]
        menu = random.choice(self.menus)
        return item + menu