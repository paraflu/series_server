from app import db


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String(120), nullable=False)
    local_title = db.Column(db.String(120), nullable=True)
    first_aired = db.Column(db.Datetime, nullable=True)
    local_aired = db.Column(db.Datetime, nullable=True)
    season_id = db.Column(db.Integer, db.ForeingKey(
        'season.id'), nullable=False)

    def __repr__(self):
        return '<Episode %r>' % self.original_title
