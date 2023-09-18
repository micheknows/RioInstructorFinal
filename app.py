from flask import Flask, render_template, request, redirect, url_for
import models
import datetime

app = Flask(__name__)

courses = {}
students = {}
announcements = {}
assignments = {}
submissions = {}
rubrics = {}


@app.route('/')
def index():
    return render_template('index.html',
        students=students,
        courses=courses,
        announcements=announcements
    )

@app.route('/courses')
def courses_index():
    return render_template('courses/index.html', courses=courses)


@app.route('/courses/new', methods=['GET', 'POST'])
def courses_new():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        course = models.Course(name, number, start_date, end_date)
        courses[name] = course

        return redirect(url_for('courses_index'))

    return render_template('courses/new.html')


@app.route('/students')
def students_index():
    return render_template('students/index.html', students=students)


@app.route('/students/new', methods=['GET', 'POST'])
def students_new():
    if request.method == 'POST':
        name = request.form['name']

        student = models.Student(name)
        students[name] = student

        return redirect(url_for('students_index'))

    return render_template('students/new.html')


@app.route('/enroll', methods=['POST'])
def enroll_student():
    name = request.form['name']
    course = request.form['course']

    student = students[name]
    course = courses[course]

    enrollment = models.Enrollment(student, course)
    student.enrollments.append(enrollment)

    return redirect(url_for('index'))


@app.route('/announcements/new', methods=['GET', 'POST'])
def announcements_new():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        course_type = request.form['course_type']

        announcement = models.Announcement(title, text, None, course_type)
        announcements[title] = announcement

        return redirect(url_for('index'))

    return render_template('announcements/new.html', courses=courses)


@app.route('/submit_assignment', methods=['POST'])
def submit_assignment():
    # Handle form submission
    return redirect(url_for('index'))

# Additional routes for assignments, submissions, rubrics, etc

if __name__ == '__main__':
    app.run()