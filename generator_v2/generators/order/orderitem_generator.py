import uuid
import random

from models.orderitem import OrderItem
from generators.order.read_csv_uuid import order_uuids, item_uuids

class OrderItemGenerator:
    def __init__(self):
        self.orders = order_uuids
        self.items = item_uuids

    def generate(self):
        id = uuid.uuid4()
        order_id = random.choice(self.orders)
        item_id = random.choice(self.items)
        return OrderItem(id, order_id, item_id)