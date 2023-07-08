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