import random
import datetime
from generators.generator import Generator

class BirthDateGenerator(Generator):
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