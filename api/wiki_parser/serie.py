from typing import Dict


class Serie:
    def __init__(self, title):
        self.title = title
        self.seasons = []

    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'seasons': [s.to_dict() for s in self.seasons]
        }
