#StudentManager.py

from Person import Person
from Student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def createStudent(self, id, name, lastName, email, ausence):
        new = Student(id, name, lastName, email, ausence)
        self.students.append(new)
        print("El estudiante se agrego correctamente")
        return new
    
    def editStudent(self, id=None, name=None, lastName=None, email=None, ausence=None):
        for sharedId in self.students:
            if sharedId.id == id:
                return sharedId
            return None

    def deleteStudent(self, id):
        for sharedId in self.students:
            if sharedId.id == id:
                self.students.remove(sharedId)

    def showStudent(self, student):
        print(f"ID: {student.id} Name {student.name} Last Name {student.lastName} Email {student.email} Ausence {student.ausence}")

gestor = StudentManager()
est1 = gestor.createStudent(1,"marco","antonio","oguzmarc14@gmail.com",5)
gestor.showStudent(est1)
gestor.deleteStudent(1)