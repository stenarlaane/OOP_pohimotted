"""School class which stores information about courses and students."""
from course import Course
from student import Student


class School:


    def __init__(self, name: str):
        self.name = name
        self.courses = []
        self.students = []


    def add_student(self, student: Student):
        if student not in self.students:
            student.set_id(len(self.students) + 1)
            self.students.append(student)


    def add_course(self, course: Course):
       if course not in self.courses:
           self.courses.append(course)


    def add_student_grade(self, student: Student, course: Course, grade: int):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)


    def get_students(self) -> list[Student]:
        return self.students


    def get_courses(self) -> list[Course]:
        return self.courses


    def get_students_ordered_by_average_grade(self) -> list[Student]:
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
    pass
