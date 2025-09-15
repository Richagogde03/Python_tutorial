class Student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")


student1 = Student("Madhav", 11, 90)
student1.student_details()
# user just calling the function he/she dont know about its internal
student2 = Student("Arjun", 10, 85)
