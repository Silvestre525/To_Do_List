from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notas.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo de la tabla Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nulleable = False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Tareas: {self.text} {self.complete}>"

with app.app_context():
    db.create_all()
    