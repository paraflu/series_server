from app import db


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_episodes = db.Column(db.Integer)
    first_aired = db.Column(db.String(60), nullable=True)
    local_aired = db.Column(db.String(60), nullable=True)
    serie_id = db.Column(db.Integer, db.ForeignKey('serie.id'), nullable=False)
    episodes = db.relationship('Episode', backref='season', lazy=True)

    def __repr__(self):
        return '<Season %r>' % self.id
