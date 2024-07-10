from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class StudentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    standard = db.Column(db.String(10), nullable=False)
    school = db.Column(db.String(150), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    hindi = db.Column(db.Integer, nullable=False)
    math = db.Column(db.Integer, nullable=False)
    science = db.Column(db.Integer, nullable=False)
    history = db.Column(db.Integer, nullable=False)
    english = db.Column(db.Integer, nullable=False)
