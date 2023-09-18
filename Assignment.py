import datetime


class Assignment:

    def __init__(self, name, due_date, max_score, feedback_text):
        self.name = name
        self.due_date = due_date
        self.max_score = max_score
        self.feedback_text = feedback_text

    def get_name(self):
        return self.name

    def get_due_date(self):
        return self.due_date

    def get_max_score(self):
        return self.max_score

    def get_feedback_text(self):
        return self.feedback_text

    def set_feedback_text(self, text):
        self.feedback_text = text
