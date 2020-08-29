from application import db

class weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weathers = db.Column(db.String(5), nullable=False)

class speed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    speeds = db.Column(db.String(7), nullable=False)

class results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather = db.Column(db.String(5), nullable=False)
    speed = db.Column(db.String(7), nullable=False)
    result = db.Column(db.String(50), nullable=False)