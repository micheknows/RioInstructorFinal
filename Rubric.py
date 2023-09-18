class Rubric:

    def __init__(self):
        self.rows = []

    def get_rows(self):
        return self.rows

    def add_row(self, row):
        self.rows.append(row)

    def calculate_score(self):
        total = 0
        for row in self.rows:
            if row.get_yes_no():
                total += row.get_points()
        return total

class RubricRow:

    def __init__(self, criteria, yes_no, points):
        self.criteria = criteria
        self.yes_no = yes_no
        self.points = points

    def get_criteria(self):
        return self.criteria

    def get_yes_no(self):
        return self.yes_no

    def get_points(self):
        return self.points

    def set_yes_no(self, yes_no):
        self.yes_no = yes_no