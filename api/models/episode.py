from datetime import datetime
from typing import Dict
from app import db
from ..wiki_parser import Episode as ViewEpisode


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String(120), nullable=False)
    local_title = db.Column(db.String(120), nullable=True)
    first_aired = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=True)
    local_aired = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=True)
    season_id = db.Column(db.Integer, db.ForeignKey(
        'season.id'), nullable=False)

    @staticmethod
    def convert(the_episode: ViewEpisode):
        return Episode(
            original_title=the_episode.original_title,
            local_title=the_episode.local_title,
            first_aired=the_episode.first_aired,
            local_aired=the_episode.local_aired
        )

    def __repr__(self):
        return '<Episode %r>' % self.original_title

    def as_dict(self) -> Dict:
        return {
            "id": self.id,
            "original_title": self.original_title,
            "local_title": self.local_title,
            "first_aired": self.first_aired,
            "local_aired": self.local_aired,
        }
