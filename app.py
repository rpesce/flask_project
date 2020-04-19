from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)


@app.route('/')
def tasks():
    if "todos" not in session:
        session['todos'] = []
    return render_template("all-tasks.html", todos=session['todos'])


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add-task.html")
    else:
        todo = request.form.get('task')
        session['todos'].append(todo)
        return redirect('/')


if __name__ == '__main__':
    app.run()
