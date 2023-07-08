import uuid
from generators.store.storename_generator import StoreNameGenerator
from generators.common.address_generator import AddressGenerator
from generators.generator import Generator

class StoreGenerator(Generator):
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = StoreNameGenerator().generate()
        self.type = self.name.split(" ")[0]
        self.address = AddressGenerator().generate()

    def generate(self):
        store = [self.id, self.name, self.type, self.address]
        return store