from app import db

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    seasons = db.relationship('Season', backref='serie', lazy=True)

    def __repr__(self):
        return '<Serie %r>' % self.title