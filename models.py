from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


db = SQLAlchemy()



class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    complete = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self):

        return f'<Todo {self.id}: {self.title}>'

