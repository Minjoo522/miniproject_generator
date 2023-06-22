import random
import csv
import datetime
import os

# ----------------------------
# Genereator Classes - common
# ----------------------------
class AddressGenerator:
    def __init__(self):
        self.cities = load_data("src/cities.txt")
        self.gus = load_data("src/gus.txt")
        self.roads = ["로", "길"]

    def generate(self):
        city = random.choice(self.cities)
        gu = random.choice(self.gus)
        road = random.choice(self.roads)
        road_number1 = random.randint(1, 99)
        road_number2 = random.randint(1, 99)
        return f"{city} {gu} {road_number1}{road} {road_number2}"
    
# ----------------------------
# Genereator Classes - user
# ----------------------------
class NameGenerator:
    def __init__(self):
        self.first_names = load_data("src/first_names.txt")
        self.last_names = load_data("src/last_names.txt")

    def generate(self):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return last_name + first_name

class GenderGenerator:
    def generate(self):
        return random.choice(["male", "female"])

class BirthDateGenerator:
    def __init__(self):
        self.__date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def generate(self):
        year = random.randint(1980, 2010)
        is_leap = year % 4 == 0 and (year % 100 or year % 400)
        month = random.randint(1, 12)
        if month == 2 and is_leap:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, self.__date[month - 1])
        return f"{year}-{month:02d}-{day:02d}"

class AgeGenerator:
    def __init__(self):
        self.__birth_day_str = BirthDateGenerator().generate()

    def generate(self):
        current = datetime.datetime.today()
        birth_day = datetime.datetime.strptime(self.__birth_day_str, "%Y-%m-%d")
        age = current.year - birth_day.year
        if current.month > birth_day.month:
            age -= 1
        elif current.month == birth_day.month and current.day < birth_day.day:
            age -= 1
        return age

# ----------------------------
# Genereator Classes - store
# ----------------------------
class StoreNameGenerator:
    def __init__(self):
        self.cafe_types = load_data("src/cafe_types.txt")
        self.cafe_districts = load_data("src/cafe_districts.txt")
    
    def generate(self):
        cafe_type = random.choice(self.cafe_types)
        cafe_district = random.choice(self.cafe_districts)
        return f"{cafe_type} {cafe_district}{random.randint(1, 20)}호점"

# ----------------------------
# Genereator Classes - item
# ----------------------------
# TODO:
class MenuGenerator:
    def __init__(self):
        self.menus = load_data("src/cafe_districts.txt")

    def generate(self):
        menu = random.choice(self.menus)
        name = menu["name"]
        return name

# -------------------
# Genereator Classes
# -------------------
class UserGenerator:
    def __init__(self):
        self.name = NameGenerator().generate()
        self.gender = GenderGenerator().generate()
        self.birthdate = BirthDateGenerator().generate()
        self.age = AgeGenerator().generate()
        self.address = AddressGenerator().generate()

    def generate(self):
        return [self.name, self.gender, self.birthdate, self.age, self.address]

class StoreGenerator:
    def __init__(self):
        self.name = StoreNameGenerator().generate()
        self.type = self.name.split(" ")[0]
        self.address = AddressGenerator().generate()

    def generate(self):
        return [self.name, self.type, self.address]

# -------------------
# Functions
# -------------------
def generate_user(number):
    users = []
    for _ in range(number):
        user = UserGenerator().generate()
        users.append(user)
    return users

def generate_store(number):
    stores = []
    for _ in range(number):
        store = StoreGenerator().generate()
        stores.append(store)
    return stores

def load_data(file_path):
    with open(file_path, "r") as file:
        data = file.read().splitlines()
    return data

def print_console(data):
    for item in data:
        print(item)

def save_csv(data):
    current_dir = os.getcwd()
    with open(f"{current_dir}/{data_type}.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# -------------------
# Input Functions
# -------------------
def input_data_type():
    data_type = ""
    data_type = input("생성할 데이터 타입을 입력하세요(user or store): ").lower()
    if not (data_type == "user" or data_type == "store"):
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
    format = input("아웃풋 타입을 입력하세요(console or csv): ").lower()
    if format == "console" or format == "csv":
        return format
    else:
        print("지원하지 않는 아웃풋 타입입니다.")
        format = input_format()

def generate_data(number, data_type):
    if data_type == "user":
        data = generate_user(number)
    elif data_type == "store":
        data = generate_store(number)
    return data

def print_data(format, data):
    if format == "console":
        print_console(data)
    if format == "csv":
        save_csv(data)

# -------------------
# Main
# -------------------
# TODO: 정리하기
if __name__ == "__main__":
    data_type = input_data_type()
    number = input_number()
    format = input_format()
    data = generate_data(number, data_type)
    print_data(format, data)
    # first_names = []
    # last_names = []

# TODO: lode_data -> 완료
# TODO: 인풋 처리
# TODO: csv 저장