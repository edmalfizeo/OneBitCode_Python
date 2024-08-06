from Projects import app, db
from flask import render_template, request, redirect, url_for
from Projects.list_films import result_films
from Projects.book import Book


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

@app.route('/books', methods=["GET", "POST"])
def list_book():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    all_books = Book.query.paginate(page=page, per_page=per_page)
    return render_template(
        "books.html",
        books=all_books
    )

@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            price = request.form['price']
            
            print(f"Title: {title}, Description: {description}, Price: {price}")
            
            new_book = Book(title=title, description=description, price=price)
            db.session.add(new_book)
            print("Book added to session")
            
            print(f"Session new: {db.session.new}")
            db.session.commit()
            print("Book committed to database")
            
            return redirect(url_for('list_book'))
        except Exception as e:
            db.session.rollback()
            print(f"Error adding book: {e}")
    return render_template('new_book.html')

@app.route('/<int:id>/update_book', methods=["GET", "POST"])
def update_book(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        try:
            book.title = request.form['title']
            book.description = request.form['description']
            book.price = request.form['price']
            
            Book.query.filter_by(id=id).update({
                'title': book.title,
                'description': book.description,
                'price': book.price
            })

            db.session.commit()
            return redirect(url_for('list_book'))
        except Exception as e:
            db.session.rollback()
            print(f"Error updating book: {e}")
    return render_template(
        'update_book.html',
        book=book
    )

@app.route('/<int:id>/delete_book', methods=["GET", "POST"])
def delete_book(id):
    book=Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('list_book'))
