from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jacks')
    first, last, github = hackbright.get_student_by_github(github)
    project_grades = hackbright.get_grade_and_project_as_tuples(github)
    html = render_template("student_info.html", first=first, last=last, github=github,
        project_grades=project_grades)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/new-student-form")
def get_new_student_form():
    """Show form for creating a new student."""

    return render_template("create_new_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    github = request.form.get('github')
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    hackbright.make_new_student(first_name, last_name, github)
    html = render_template("new_student_ack.html",
                            github=github,
                            firstname=first_name,
                            lastname=last_name)

    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)


