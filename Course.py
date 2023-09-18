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


class CourseType:

    def __init__(self, name, ident):
        self.name = name
        self.identifier = ident
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments

# Create some sample course types
java_1 = CourseType('Java I', 'CIS163AA')
java_2 = CourseType('Java II', 'CIS263AA')
mysql = CourseType('MySQL', 'CIS276DA')

coursetypes = {
  'Java I': java_1,
  'Java II': java_2,
  'MySQL': mysql
}

# Add assignments
#java_1.add_assignment(Assignment(...))

# Get assignments for a type
#assignments = java_1.get_assignments()