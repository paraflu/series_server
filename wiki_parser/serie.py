from typing import Dict


class Serie:
    def __init__(self, title: str, url: str):
        """Inizializzo la classe serie

        Args:
            title (str): titolo della serie
            url (str): url dal quale i dati sono stati parsati
        """
        self.title = title
        self.url = url
        self.seasons = []
        self.image = None

    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'seasons': [s.to_dict() for s in self.seasons],
            'url': self.url,
            'image': self.image,
            'imdb_id': self.imdb_id,
            'imdb': self.imdb.to_dict()
        }
