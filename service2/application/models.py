from application import db

class Weathers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather = db.Column(db.String(5), nullable=False)

class Speeds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    speed = db.Column(db.String(7), nullable=False)
