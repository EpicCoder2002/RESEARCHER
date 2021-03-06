from RESEARCHER import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.orm import relationship





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    researches = db.relationship('Research', lazy='dynamic', foreign_keys = 'Research.owner')
    
    def __repr__(self):
        return f"{self.full_name}"



class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(20000), nullable=False, unique=True)
    research_subject = db.Column(db.String(20000), nullable=False)
    survey_link = db.Column(db.String(255), nullable=False)
    grade = db.Column(db.String(255), nullable=False) 
    province = db.Column(db.String(255), nullable=False, unique=False)
    level = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f"{self.id}"

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    provinceS = db.Column(db.String(255), nullable=False, unique=False)
  

    def __repr__(self):
        return f"{self.name}"


