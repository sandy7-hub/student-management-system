from itertools import product

from flask import Flask, redirect, render_template, request ,redirect, session, url_for
from models import db, Student 
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sandy4@localhost/student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
   

    
@app.route('/', methods=['GET', 'POST'])
def index():
    
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')

    
    if request.method == 'POST':
        search = request.form['search']
        students = Student.query.filter(
            ( Student.name.like(f'%{search}%') )|
            ( Student.course.like(f'%{search}%') )
            
        ).paginate(page=page, per_page=3)
    else:
        students = Student.query.paginate(page=page, per_page=3)

    return render_template('index.html', students=students , search=search)
    
    
@app.route('/add', methods = [ 'GET' , 'POST'])
def add():
    if request.method == 'POST':
        print("details add successfully")
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        student = Student(name=name, age=age, course=course)
        db.session.add(student)
        db.session.commit()

        return redirect('/')

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = Student.query.get(id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.age = request.form['age']
        student.course = request.form['course']

        db.session.commit()
        return redirect('/')
    

    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')        



if __name__ == "__main__":
    app.run(debug=True)
