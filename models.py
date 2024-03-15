from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30), nullable = False)
    parole = db.Column(db.String(30), nullable = False)

    def set_parole(self, parole):
        self.parole = generate_password_hash(parole)

    def check_parole(self, parole):
        return check_password_hash(self.parole, parole)