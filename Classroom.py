from Stud import Student

class Classroom:
    def __init__(self, list = []):
        self.list = list
        self.student

    def addStudent(self, student):
        self.list.append(student)

    def showClassroom(self):
        for stud in self.list:
            stud.showStudent()
