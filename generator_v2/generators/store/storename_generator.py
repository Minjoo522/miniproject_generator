import random

from generators.common.load_data import cafe_types, cafe_districts

class StoreNameTypeGenerator:
    def __init__(self):
        self.cafe_types = cafe_types
        self.cafe_districts = cafe_districts
        self.BRANCH_MAX = 20

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