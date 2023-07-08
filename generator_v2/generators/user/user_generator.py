import uuid

from generators.user.name_generator import NameGenerator
from generators.user.gender_generator import GenderGenerator
from generators.user.birthdate_age_generator import BirthDateAgeGenerator
from generators.common.address_generator import AddressGenerator

from models.user import User
from generators.generator import Generator

class UserGenerator(Generator):
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