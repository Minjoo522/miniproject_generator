import csv
import uuid
import random
from datetime import datetime, timedelta

def load_data(file_path):
    with open(f"{file_path}", "r") as file:
        data = file.read().splitlines()
        return data
    
def read_csv_uuid(file_path):
    uuid_list = []
    with open(f"{file_path}.csv", "r") as file:
        uuids = csv.reader(file)
        next(uuids) # 헤더 스킵
        for uuid in uuids:
            uuid_list.append(uuid[0])
    return uuid_list

# -------------------
# User Generator
# -------------------
class NameGenerator:
    first_names = []
    last_names = []

    def generate(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        full_name = last_name + first_name
        return full_name

class GenderGenerator:
    def generate(self):
        gender = random.choice(["Male", "Female"])
        return gender

class BirthDateAgeGenerator:
    def __init__(self):
        self.__year = random.randint(1980, 2010)
        self.__date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.__month = random.randint(1, 12)

    def generate(self):
        birthday_age = {}
        birthday_age['birth_date'] = self.birthdate_generate()
        birthday_age['age'] = self.age_generate(birthday_age['birth_date'])
        return birthday_age

    def birthdate_generate(self):
        is_leap = self.__year % 4 == 0 and (self.__year % 100 or self.__year % 400)
        if self.__month == 2 and is_leap:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, self.__date[self.__month - 1])
        birth_date = f"{self.__year}-{self.__month:02d}-{day:02d}"
        return birth_date

    def age_generate(self, str_birth_date):
        current_date = datetime.datetime.today()
        birth_date = datetime.datetime.strptime(str_birth_date, "%Y-%m-%d")
        age = current_date.year - birth_date.year
        if current_date.month < birth_date.month:
            age -= 1
        elif current_date.month == birth_date.month and current_date.day < birth_date.day:
            age -= 1
        return age
    
class UserGenerator:
    def __init__(self):
        self.name_generator = NameGenerator()
        self.gender_generator = GenderGenerator()
        self.birthdate_age_generator = BirthDateAgeGenerator()
        self.address_generator = AddressGenerator()
    
    def generate(self):
        birth_date_age = self.birthdate_age_generator.generate()
        user_id = uuid.uuid4()
        name = self.name_generator.generate()
        gender = self.gender_generator.generate()
        birth_date = birth_date_age['birth_date']
        age = birth_date_age['age']
        address = self.address_generator.generate()
        return User(user_id, name, gender, birth_date, age, address)
    

class User:
    def __init__(self, id, name, gender, birth_date, age, address):
        self.id = id
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"Id : {self.id} Name : {self.name} Gender : {self.gender} Birth Date : {self.birth_date} Age : {self.age} Address : {self.address}"


# -------------------
# Common Generator
# -------------------
class AddressGenerator():
    cities = []
    gus = []
    roads = ["로", "길"]
    ADDRESS_MAX = 99

    def generate(self):
        city = random.choice(self.cities)
        gu = random.choice(self.gus)
        road = random.choice(self.roads)
        road_number = random.randint(1, self.ADDRESS_MAX)
        building_number = random.randint(1, self.ADDRESS_MAX)
        full_address = f"{city} {gu} {road_number}{road} {building_number}"
        return full_address
    
# -------------------
# Store Generator
# -------------------
class StoreNameTypeGenerator:
    cafe_types = []
    cafe_districts = []
    BRANCH_MAX = 20

    def generate(self):
        cafe_info = {}
        cafe_info['type'] = self.type_generate()
        district = self.distrtict_generate()
        branch = random.randint(1, self.BRANCH_MAX)
        cafe_info['name'] = f"{cafe_info['type']} {district}{branch}호점"
        return cafe_info
    
    def type_generate(self):
        cafe_type = random.choice(self.cafe_types)
        return cafe_type
    
    def distrtict_generate(self):
        cafe_district = random.choice(self.cafe_districts)
        return cafe_district
    
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

class Store:
    def __init__(self, id, name, type, address):
        self.id = id
        self.name = name
        self.type = type
        self.address = address

    def __str__(self):
        return f"Id : {self.id} Name : {self.name} Type : {self.type} Address : {self.address}"

# -------------------
# Item Generator
# -------------------

class ItemGenerator:
    def __init__(self):
        self.item_types = {
            "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }

    def generate(self):
        # id, name, type, price
        item_id = uuid.uuid4()
        item_type = random.choice(list(self.item_types.keys()))
        item_subtype = random.choice(list(self.item_types[item_type].keys()))
        item_name = f"{item_subtype} {item_type}"
        item_price = self.item_types[item_type][item_subtype]
        return Item(item_id, item_name, item_type, item_price)

class Item:
    def __init__(self, id, name, type, price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
    
    def __str__(self):
        return f"Id : {self.id} Name : {self.name} Type : {self.type} Price : {self.price}"

# ----------------------------------
# Order Generator
# 생성된 users와 stores가 있어야 사용 가능
# ----------------------------------

class OrderGenerator:
    users = []
    stores = []

    def generate(self):
        id = uuid.uuid4()
        order_at = self.date_generate()
        store_id = random.choice(self.stores)
        user_id = random.choice(self.users)
        return print(id, order_at, store_id, user_id)
    
    def date_generate(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 12, 31)

        time_diff = end - start
        random_seconds = random.randint(0, time_diff.total_seconds())
        random_date = start + timedelta(seconds=random_seconds)
        return random_date
    
class Order:
    def __init__(self, id, order_at, store_id, user_id):
        self.id = id
        self.order_at = order_at
        self.store_id = store_id
        self.user_id = user_id

    def __str__(self):
        return f"Id : {self.id} Order At : {self.order_at} Store Id : {self.store_id} User Id : {self.user_id}"
    
# ----------------------------------
# Order Generator
# 생성된 orders, items가 있어야 사용 가능
# ----------------------------------

class OrderItemGenerator:
    orders = []
    items = []

    def generate(self):
        id = uuid.uuid4()
        order_id = random.choice(self.orders)
        item_id = random.choice(self.items)
        return Order(id, order_id, item_id)

class Order:
    def __init__(self, id, order_id, item_id):
        self.id = id
        self.order_id = order_id
        self.item_id = item_id
    
    def __str__(self):
        return f"Id : {self.id} Order Id : {self.order_id} Item Id : {self.item_id}"


if __name__ == "__main__":
    NameGenerator.first_names = load_data('src/first_names.txt')
    NameGenerator.last_names = load_data('src/last_names.txt')
    AddressGenerator.cities = load_data("src/cities.txt")
    AddressGenerator.gus = load_data("src/gus.txt")
    StoreNameTypeGenerator.cafe_types = load_data("src/cafe_types.txt")
    StoreNameTypeGenerator.cafe_districts = load_data("src/cafe_districts.txt")
    OrderGenerator.stores = read_csv_uuid("store")
    OrderGenerator.users = read_csv_uuid("user")
    OrderItemGenerator.orders = read_csv_uuid("order")
    OrderItemGenerator.items = read_csv_uuid("item")

    print(OrderItemGenerator().generate())