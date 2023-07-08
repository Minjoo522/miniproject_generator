import uuid
from generators.store.storename_generator import StoreNameTypeGenerator
from generators.common.address_generator import AddressGenerator

from models.store import Store

class StoreGenerator:
    def __init__(self):
        self.storename_generator = StoreNameTypeGenerator()
        self.address_generator = AddressGenerator()

    def generate(self):
        name_type = self.storename_generator.generate()
        store_id = uuid.uuid4()
        name = name_type['name']
        type = name_type['type']
        address = self.address_generator.generate()
        return Store(store_id, name, type, address)
