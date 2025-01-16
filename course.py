"""Course class with name and grades."""


class Course:
    """Kursuse klass"""
    
    def __init__(self, name: str):
        """
        Kursuse konstruktor.
        """
        self.name = name
        self.grades = []
        
        
    def add_grade(self, student, grade):
        self.grades.append((student, grade))
        
        
    def get_grades(self):
        return self.grades
    
    
    def get_average_grade(self):
        average_grade = -1
        if len(self.grades) > 0:
            sum_of_grades = 0
            for grade in self.grades:
                sum_of_grades += grade[1]
            average_grade = sum_of_grades / len(self.grades)
        return average_grade
    
    
    def __repr__(self):
        return self.name
        
    
    pass