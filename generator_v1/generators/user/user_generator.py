import uuid
from generators.user.birthdate_generator import BirthDateGenerator
from generators.user.name_generator import NameGenerator
from generators.user.gender_generator import GenderGenerator
from generators.common.address_generator import AddressGenerator
from generators.generator import Generator

class UserGenerator(Generator):
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = NameGenerator().generate()
        self.gender = GenderGenerator().generate()
        self.birthdate = BirthDateGenerator().generate()['birth_date']
        self.age = BirthDateGenerator().generate()['age']
        self.address = AddressGenerator().generate()

    def generate(self):
        user = [str(self.id), self.name, self.gender, self.birthdate, self.age, self.address]
        return  user