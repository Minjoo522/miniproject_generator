import csv
import os

from generators.common.address_generator import AddressGenerator
from generators.user.name_generator import NameGenerator
from generators.store.storename_generator import StoreNameGenerator
from generators.user.user_generator import UserGenerator
from generators.item.item_generator import ItemGenerator
from generators.store.store_generator import StoreGenerator

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

def load_data_menu():
    with open("src/menus.txt", "r") as file:
        menus = []
        datas = file.read().splitlines()
        for data in datas:
            menus.append(data.split(', '))
        return menus

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