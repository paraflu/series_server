from datetime import datetime
from typing import Dict


class Episode:
    def __init__(self, season_no: int, n: int, original_title: str, local_title: str, first_aired: datetime = None, local_aired: datetime = None):
        """Inizializza un episodio

        Args:
            season_no (int): numero della serie
            n (int): numero dell'episodio
            original_title (str): titolo originale
            local_title (str): titolo locale
            first_aired (datetime, optional): data rilascio originale. Defaults to None.
            local_aired (datetime, optional): data rilascio locale. Defaults to None.
        """
        self.season_no = season_no
        self.episode_no = n
        self.original_title = original_title
        self.local_title = local_title
        self.first_aired = first_aired
        self.local_aired = local_aired

    @property
    def id(self):
        return f'S{self.season_no:02}E{self.episode_no:02}'

    def __str__(self) -> str:
        return f'#{self.id} {self.original_title} - {self.local_title} - {self.first_aired.isoformat() if self.first_aired else "-"} - {self.local_aired.isoformat() if self.local_aired else "-"}'

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'season_no': self.season_no,
            'episode_no': self.episode_no,
            'original_title': self.original_title,
            'local_title': self.local_title,
            'first_aired': self.first_aired.isoformat() if self.first_aired else None,
            'local_aired': self.local_aired.isoformat() if self.local_aired else None,
        }
