class Announcement:

    def __init__(self, title, body_text, attachment=None, course_type=None):
        self.title = title
        self.body_text = body_text
        self.attachment = attachment
        self.course_type = course_type

    def get_title(self):
        return self.title

    def get_body_text(self):
        return self.body_text

    def get_attachment(self):
        return self.attachment

    def get_course_type(self):
        return self.course_type

    def set_course_type(self, course_type):
        self.course_type = course_type