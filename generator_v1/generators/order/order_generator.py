import uuid
from generators.generator import Generator
from generators.store.store_generator import StoreGenerator
from generators.user.user_generator import UserGenerator

class OrderGenerator(Generator):
    def __init__(self):
        self.id = uuid.uuid4()
        self.order_at = "" # TODO: 날짜, 시간 나오게
        self.store_id = StoreGenerator().generate()[0]
        self.user_id = UserGenerator().generate()[0]

    def generate(self):
        return 