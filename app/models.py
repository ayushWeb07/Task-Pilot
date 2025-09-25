# import packages
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    # author link
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    
    
    is_completed = db.Column(db.Boolean, default= False)
    
    priority = db.Column(db.String(20), nullable=False)
    
    
    
    



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(100), nullable=False)
    
    password= db.Column(db.String(20), nullable=False)

    