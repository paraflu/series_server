from api.models.episode import Episode
from app import db

from ..wiki_parser import Season as ViewSeason


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_no = db.Column(db.Integer)
    num_episodes = db.Column(db.Integer)
    first_aired = db.Column(db.String(60), nullable=True)
    local_aired = db.Column(db.String(60), nullable=True)
    serie_id = db.Column(db.Integer, db.ForeignKey('serie.id'), nullable=False)
    episodes = db.relationship('Episode', backref='season', lazy=True)

    @staticmethod
    def convert(the_season: ViewSeason):
        ret = Season(
            season_no=the_season.season_no,
            num_episodes=the_season.num_episodes,
            first_aired=the_season.first_aired,
            local_aired=the_season.local_aired,
        )
        for episode in the_season.episodes:
            ret.episodes.append(Episode.convert(episode))
        return ret

    def __repr__(self):
        return '<Season %r>' % self.id

    def as_dict(self):
        return {
            "id": self.id,
            "num_episodes": self.num_episodes,
            "first_aired": self.first_aired,
            "local_aired": self.local_aired,
            "episodes": [e.as_dict() for e in self.episodes]
        }
