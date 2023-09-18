class Student:
    def __init__(self, name):
        self.name = name
        self.enrollments = []

    def get_name(self):
        return self.name

    def get_enrollments(self):
        return self.enrollments

    def enroll_in_course(self, course):
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)


class Enrollment:

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.start_date = course.start_date
        self.end_date = course.end_date

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date