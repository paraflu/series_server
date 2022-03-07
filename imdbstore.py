from typing import List
from imdb import Cinemagoer
from imdb.Movie import Movie


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
