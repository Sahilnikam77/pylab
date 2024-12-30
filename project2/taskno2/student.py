


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        if not self.grades:
            return None
        return max(self.grades)

    def lowest_grade(self):
        if not self.grades:
            return None
        return min(self.grades)
