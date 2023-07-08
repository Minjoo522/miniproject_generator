class Item:
    def __init__(self, id, name, type, price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
    
    def __str__(self):
        return f"Id : {self.id} Name : {self.name} Type : {self.type} Price : {self.price}"
