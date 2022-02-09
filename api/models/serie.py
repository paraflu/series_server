from turtle import title
from app import db

from ..wiki_parser import Serie as ViewSerie
from ..wiki_parser import Season as ViewSeason

from .season import Season

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    seasons = db.relationship('Season', backref='serie', lazy=True)

    @staticmethod
    def convert(viewModel: ViewSerie):
        res =  Serie(title=viewModel.title)
        for season in viewModel.seasons:
            res.seasons.append(Season.convert(season))
        return res

    def __repr__(self):
        return '<Serie %r>' % self.title
