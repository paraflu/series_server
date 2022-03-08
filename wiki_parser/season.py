from typing import Dict, List, Optional
from .episode import Episode


class Season:
    def __init__(self, n: int, num_episodes: int, first_aired: str = None, local_aired: str = None, episodes: List[Episode] = []) -> None:
        """Rappresenta una stagione della serie

        Args:
            n (int): numero della stagione
            num_episodes (int): numero totale di episodi
            first_aired (str, optional): anno della pubblicazione. Defaults to None.
            local_aired (str, optional): anno di pubblicazione in italia. Defaults to None.
            episodes (List[Episode], optional): elenco episodi. Defaults to [].
            """
        self.season_no = n
        self.num_episodes = num_episodes
        self.first_aired = first_aired
        self.local_aired = local_aired
        self.episodes = episodes

    def __str__(self) -> str:
        """Converte la classe in stringa

        Returns:
            str: rappresentazione stringa della classe
        """
        return f'ser {self.season_no} {self.first_aired if self.first_aired else "-"} - {self.local_aired if self.local_aired else "-"}'

    @property
    def last(self, local=True) -> Optional[Episode]:
        """Recupera se presente l'ultimo episodio

        Args:
            local (bool, optional): indica se visualizzare l'ultimo episodio locale o originale. Defaults to True.

        Returns:
            Optional[Episode]: [description]
        """
        if len(self.episodes) > 0:
            list = [e for e in self.episodes if e.first_aired]
            if local:
                list = [e for e in list if e.local_aired]
            return list[-1]
        return None

    def to_dict(self) -> Dict:
        return {
            'season_no': self.season_no,
            'num_episodes': self.num_episodes,
            'first_aired': self.first_aired,
            'local_aired': self.local_aired,
            'episodes': [e.to_dict() for e in self.episodes],
        }

    @property
    def id(self) -> str:
        return f'S{self.season_no:02}'
