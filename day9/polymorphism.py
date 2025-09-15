class Student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%") 


student1 = Student("Madhav", 11, 90)
student1.student_details()
student2 = Student("Arjun", 10, 85)


class GraduateStudent(Student):
    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage)
        self.stream = stream

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% and from stream {self.stream}")


grad_student1 = GraduateStudent("X", 12, 96, 'PCM')
grad_student1.student_details()
