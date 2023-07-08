class Store:
    def __init__(self, id, name, type, address):
        self.id = id
        self.name = name
        self.type = type
        self.address = address

    def __str__(self):
        return f"Id : {self.id} Name : {self.name} Type : {self.type} Address : {self.address}"