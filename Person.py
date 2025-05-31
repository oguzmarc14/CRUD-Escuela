#Person.py

class Person:
    def __init__(self, id:int, name:str, lastName:str):
        self.id = id
        self.name = name
        self.lastName = lastName

    # translate method name to EN
    def mostrar(self):
        print(f"ID: {self.id} Name: {self.name} Last name: {self.lastName}")
