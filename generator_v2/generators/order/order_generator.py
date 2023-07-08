import uuid
import random
from datetime import datetime, timedelta

from models.order import Order
from generators.generator import Generator
from generators.order.read_csv_uuid import store_uuids, user_uuids

class OrderGenerator(Generator):
    def __init__(self):
        self.stores = store_uuids
        self.users = user_uuids

    def generate(self):
        id = uuid.uuid4()
        order_at = self.date_generate()
        store_id = random.choice(self.stores)
        user_id = random.choice(self.users)
        return Order(id, order_at, store_id, user_id)
    
    def date_generate(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 12, 31)

        time_diff = end - start
        random_seconds = random.randint(0, time_diff.total_seconds())
        random_date = start + timedelta(seconds=random_seconds)
        return random_date