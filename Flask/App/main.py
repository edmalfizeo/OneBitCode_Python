from flask import Flask, render_template, request
from list_films import result_films

app = Flask(__name__)

contents = []
students_data = []
# Localhost:5000/
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("content"):
            contents.append(request.form.get("content"))
    
    return render_template("index.html",
        contents=contents
            )

# Localhost:5000/about
@app.route('/Diary', methods=["GET", "POST"])
def diary():
    if request.method == "POST":
        if request.form.get("student") and request.form.get("grade"):
            student = request.form.get("student")
            grade = request.form.get("grade")
            students_data.append({"student": student, "grade": grade})
    return render_template(
        "diary.html",
        students_data = students_data
                           )

@app.route('/films/<propriedade>')
def list_films(propriedade):
    return render_template(
        "films.html", 
        filmes = result_films(propriedade)
    )