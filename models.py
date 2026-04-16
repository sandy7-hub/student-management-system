from flask_sqlalchemy import SQLAlchemy
import models

db = SQLAlchemy()

class  Student (db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String(100))
    age = db.Column (db.Integer)
    course= db.Column (db.String(200))
    


    
