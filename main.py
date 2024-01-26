# Create a Python Flask web application for managing a list of books. The application should have the following features:

# Define a Book model with the following attributes: id (integer), title (string), author (string), and publication year (integer).
# Create a route /books that displays a list of books. Each book should show its title, author, and publication year.
# Create a route /add_book that allows users to add a new book. Use a simple form to input the title, author, and publication year of the book.
# Use Flask-SQLAlchemy to create a SQLite database. Define the Book model to represent the books.


from flask import Flask, render_template, url_for, request, Response, redirect
from flask_sqlalchemy import SQLAlchemy #import library

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aaldb.db' # we set the configuration
db = SQLAlchemy(app)


# now we define a Book:
class Book(db.Model):
    # We need 5 columns: id, firstname, lastname, email, and role.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String[50], nullable=False) # nullable = False - the property doesn't accept null as a value
    author = db.Column(db.String[50], nullable=False)
    publication_year = db.Column(db.Integer[5], nullable=False)
    
# create the list
    
def create_db():
    with app.app_context():
        db.create_all()  

@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']
        

        new_book = Book(title=title, author=author, publication_year=publication_year)

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-book.html', title='Add a Book')

if __name__ == 'main':
    app.run(port=5001, debug=True) 