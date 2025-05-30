#Studen.py

from Person import Person

class Student(Person):
    def __init__(self, id:int, name:str, lastName:str, email:str, ausence:int):
        super().__init__(id, name, lastName)
        self.email = email
        self.ausence = ausence

    def showStudent(self):
        print(f"ID: {self.id} Name {self.name} Last Name {self.lastName} Email {self.email} Ausence {self.ausence}")
