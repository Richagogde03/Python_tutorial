class Student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage

    def get_percentage(self):
        return self.__percentage


student1 = Student("Keshav", 10, 90)
student2 = Student("Karishma", 12, 89)
print(f"{student1.name}'s percentage is {student1.get_percentage()}%")
