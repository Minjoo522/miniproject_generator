import random
import datetime
from generators.generator import Generator

class BirthDateGenerator(Generator):
    def __init__(self):
        self.__date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.birth_day = ""

    def generate(self):
        year = random.randint(1980, 2010)
        is_leap = year % 4 == 0 and (year % 100 or year % 400)
        month = random.randint(1, 12)
        if month == 2 and is_leap:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, self.__date[month - 1])
        self.birth_day = f"{year}-{month:02d}-{day:02d}"
        return self.birth_day
    
    def age_generate(self):
        current = datetime.datetime.today()
        birth_day = datetime.datetime.strptime(self.birth_day, "%Y-%m-%d")
        age = current.year - birth_day.year
        if current.month > birth_day.month:
            age -= 1
        elif current.month == birth_day.month and current.day < birth_day.day:
            age -= 1
        return age