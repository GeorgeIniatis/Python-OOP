import statistics

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        return statistics.mean(grades)




if __name__ == "__main__":
    s1 = Student("George", 18, 85)
    s2 = Student("John", 17, 74)
    s3 = Student("Mike", 18, 32)
    s4 = Student("Spongebob", 16, 64)
    s5 = Student("Patrick", 19, 18)

    c1 = Course("Maths", 10)
    c1.add_student(s1)
    c1.add_student(s2)
    c1.add_student(s3)
    c1.add_student(s4)
    c1.add_student(s5)

    print(c1.get_average_grade())
