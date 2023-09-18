from Student import Student
from Assignment import Assignment
import datetime

class Submission:

    def __init__(self, student, assignment, date_completed, score):
        self.student = student
        self.assignment = assignment
        self.date_completed = date_completed
        self.score = score

    def get_student(self):
        return self.student

    def get_assignment(self):
        return self.assignment

    def get_date_completed(self):
        return self.date_completed

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
