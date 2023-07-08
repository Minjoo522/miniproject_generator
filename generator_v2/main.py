# Generators
from generators.common.address_generator import AddressGenerator
from generators.user.name_generator import NameGenerator
from generators.store.storename_generator import StoreNameTypeGenerator
from generators.order.order_generator import OrderGenerator
from generators.order.orderitem_generator import OrderItemGenerator

def load_data(file_path):
    with open(f"{file_path}", "r") as file:
        data = file.read().splitlines()
        return data

if __name__ == "__main__":
    NameGenerator.first_names = load_data('src/first_names.txt')
    NameGenerator.last_names = load_data('src/last_names.txt')
    AddressGenerator.cities = load_data("src/cities.txt")
    AddressGenerator.gus = load_data("src/gus.txt")
    StoreNameTypeGenerator.cafe_types = load_data("src/cafe_types.txt")
    StoreNameTypeGenerator.cafe_districts = load_data("src/cafe_districts.txt")

    print(OrderItemGenerator().generate())