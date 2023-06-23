import random
import csv
import os

# abstractmethod
from generators.generator import Generator

# common generator
from generators.common.address_generator import AddressGenerator

# user generators
from generators.user.name_generator import NameGenerator
from generators.user.gender_generator import GenderGenerator
from generators.user.birthdate_generator import BirthDateGenerator

# store generator
from generators.store.storename_generator import StoreNameGenerator

# -------------------
# Genereator Classes
# -------------------
class ItemGenerator(Generator):
    menus = []

    def generate(self):
        menu = random.choice(self.menus)
        print(menu)
        return Item(menu)

class Item:
    def __init__(self, menu):
        self.menu = menu

    def __str__(self):
        return f"Menu: {self.menu[0]}\nType: {self.menu[1]}\nPrice: {self.menu[2]}\n"

def load_data_menu():
    with open("src/menus.txt", "r") as file:
        menus = []
        datas = file.read().splitlines()
        for data in datas:
            menus.append(data.split(', '))
        return menus

class UserGenerator(Generator):
    def __init__(self):
        self.birthday_generator = BirthDateGenerator()
        self.name = NameGenerator().generate()
        self.gender = GenderGenerator().generate()
        self.birthdate = self.birthday_generator.generate()
        self.age = self.birthday_generator.age_generate()
        self.address = AddressGenerator().generate()

    def generate(self):
        user = [self.name, self.gender, self.birthdate, self.age, self.address]
        return  User(user)
    
class User:
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f"Name: {self.user[0]}\nGender: {self.user[1]}\nBirthday: {self.user[2]}\nAge: {self.user[3]}\nAddress: {self.user[4]}\n"

class StoreGenerator(Generator):
    def __init__(self):
        self.name = StoreNameGenerator().generate()
        self.type = self.name.split(" ")[0]
        self.address = AddressGenerator().generate()

    def generate(self):
        return [self.name, self.type, self.address]
    
class Store:
    def __init__(self, store):
        self.store = store
    
    def __str__(self):
        return f"Cafe Name: {self.store[0]}\nType: {self.store[1]}\nAddress: {self.store[2]}\n"

# -------------------
# Input Functions
# -------------------
def input_data_type():
    map = ["user", "store", "item"]
    data_type = ""
    data_type = input("데이터 유형을 입력하세요 (User, Store 또는 Item): ").lower().strip()
    if not (data_type in map):
        print("지원하지 않는 데이터 타입입니다.")
        data_type = input_data_type()
    return data_type

def input_number():
    num = 0
    num = input("생성할 데이터 개수를 입력하세요: ")
    if num.isdecimal() and int(num) > 0:
        number = int(num)
    else:
        print("1 이상의 정수를 입력해 주세요.")
        number = input_number()
    return number

def input_format():
    format = input("아웃풋 타입을 입력하세요(console or csv): ").lower().strip()
    if format == "console" or format == "csv":
        return format
    else:
        print("지원하지 않는 아웃풋 타입입니다.")
        format = input_format()

# -------------------
# Generate Functions
# -------------------
def generate_data(number, data_type):
    map = {
        "user": UserGenerator,
        "store": StoreGenerator,
        "item": ItemGenerator
    }
    if data_type in map:
        generator = map[data_type]
        data = generate_data_append(generator, number)
    return data

def generate_data_append(generator, number):
    data = [generator().generate() for _ in range(number)]
    return data

# -------------------
# Print Functions
# -------------------
def print_data(format, data):
    if format == "console":
        print_console(data)
    if format == "csv":
        save_csv(data)

def print_console(data):
    for item in data:
        print(item)

def save_csv(data):
    with open(f"{current_dir}/{data_type}.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# -------------------
# Load_data
# -------------------
def load_data(file_path):
    with open(f"{file_path}", "r") as file:
        data = file.read().splitlines()
    return data

# -------------------
# Main
# -------------------
if __name__ == "__main__":
    current_dir = os.getcwd()
    AddressGenerator.cities = load_data("src/cities.txt")
    AddressGenerator.gus = load_data("src/gus.txt")

    NameGenerator.first_names = load_data("src/first_names.txt")
    NameGenerator.last_names = load_data("src/last_names.txt")

    StoreNameGenerator.cafe_types = load_data("src/cafe_types.txt")
    StoreNameGenerator.cafe_districts = load_data("src/cafe_districts.txt")

    ItemGenerator.menus = load_data_menu()
    
    data_type = input_data_type()
    number = input_number()
    format = input_format()
    data = generate_data(number, data_type)
    print_data(format, data)