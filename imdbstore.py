from typing import Dict, List
from imdb import Cinemagoer
from imdb.Movie import Movie
import dateparser

class IMDBStore(object):
    def __init__(self):
        self._ia = Cinemagoer()

    def searchById(self, id: int) -> Movie:
        return self._ia.get_movie(id)

    def search(self, query: str, episode_parse: bool = False, limit: int = 5) -> List[Movie]:
        res = self._ia.search_movie(query, limit)
        if not episode_parse:
            return res

        return [Serie(it.movieID) for it in res]

    def update(self, serie: Movie):
        return self._ia.update(serie, 'episodes')

    @property
    def episodes(self, serie: Movie):
        return serie['episodes']


class Serie(object):
    def __init__(self, id: int) -> None:
        self._db = Cinemagoer()
        self._it = self._db.get_movie(id)
        if 'tv series' in self._it['kind']:
            self._db.update(self._it, 'episodes')

    @property
    def seasons_no(self) -> int:
        """Numero di stagioni

        Returns:
            int: numero delle stagioni
        """
        return len(self._it.keys())

    def season(self, id: int) -> List[Movie]:
        """recupera gli episodi di una stagione

        Args:
            id (int): numero della stagione

        Returns:
            List[Movie]: elenco di episodi
        """
        return self._it['episodes'][id]

    def __getitem__(self, k: str):
        return self._it[k]

    def __getattr__(self, k):
        return self._it[k]
    
    def to_dict(self) -> Dict:
        episodes = [[{
            'movieID':self['episodes'][serid][ep].movieID,
            'title': self['episodes'][serid][ep]['title'],
            'season': self['episodes'][serid][ep]['season'],
            'episode': self['episodes'][serid][ep]['episode'],
            'firstAired': dateparser.parse(self['episodes'][serid][ep]['original air date']) if 'original air date' in self['episodes'][serid][ep] else None,
            'plot': self['episodes'][serid][ep]['plot'],
            'year': self['episodes'][serid][ep]['year'] if 'year' in self['episodes'][serid][ep] else None,
            
        } for ep in self['episodes'][serid]] for serid in self['episodes'].keys()]
        return {
            'movid_id': self._it.movieID,
            'kind': self['kind'],
            'title': self['title'],
            'episodes': [
                episodes
            ]
        }
