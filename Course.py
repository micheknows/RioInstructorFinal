from datetime import datetime


class Course:
    def __init__(self, name, section_number, start_date, end_date):
        self.name = name
        self.section_number = section_number
        self.start_date = start_date
        self.end_date = end_date
        self.students = []
        self.assignments = []

    def get_name(self):
        return self.name

    def get_section_number(self):
        return self.section_number

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def get_assignments(self):
        return self.assignments