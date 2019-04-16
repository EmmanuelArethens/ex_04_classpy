from Classroom import Classroom

class Student:
    def __init__(self, firstname, name, age):
        self.firstname = firstname
        self.name = name
        self.age = age

    def calcBirthdate(self):
        bd = 2019 - self.age
        print(bd)

    def showStudent(self):
        print(self.age, self.name, self.firstname)


myName = input()
myFirstname = input()
myAge = input()

myStudent = Student(myName, myFirstname, int(myAge))
myClassroom = Classroom()
myClassroom.addStudent(myStudent)
myClassroom.showClassroom()

'''
Marina = Student('Marina', 'Champredon', 29)
Adrien = Student('Adrien', 'Fulleringer', 26)
Manu = Student('Emmanuel', 'Arethens', 24)
Manu.showStudent()
Manu.calcBirthdate()
Adrien.showStudent()
Adrien.calcBirthdate()
Marina.showStudent()
Marina.calcBirthdate()
'''

