from datetime import datetime
from typing import Dict


class Episode:
    def __init__(self, n: int, original_title: str, local_title: str, first_aired: datetime = None, local_aired: datetime = None):
        self.episode_no = n
        self.original_title = original_title
        self.local_title = local_title
        self.first_aired = first_aired
        self.local_aired = local_aired

    def __str__(self) -> str:
        return f'#{self.n} {self.original_title} - {self.local_title} - {self.first_aired.isoformat() if self.first_aired else "-"} - {self.local_aired.isoformat() if self.local_aired else "-"}'

    def to_dict(self) -> Dict:
        return {
            'episode_no': self.episode_no,
            'original_title': self.original_title,
            'local_title': self.local_title,
            'first_aired': self.first_aired.isoformat() if self.first_aired else None,
            'local_aired': self.local_aired.isoformat() if self.local_aired else None,
        }
