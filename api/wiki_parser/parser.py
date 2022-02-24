
import re
from datetime import datetime
import locale
from typing import Dict, List, Optional, Union
from bs4 import BeautifulSoup
import requests

import dateparser

from .episode import Episode
from .season import Season
from .serie import Serie
from .exceptions import EpisodeNotFoundException

import logging
logging.basicConfig(level=logging.DEBUG)

locale.setlocale(locale.LC_ALL, 'it_IT')


class Parser(object):
    def __init__(self, baseurl: str):
        # self._baseurl = baseurl
        self._baseurl = baseurl

    def get(self) -> Serie:
        response = requests.get(self._baseurl)
        data = response.text
        r = BeautifulSoup(data, 'lxml')
        table = r.select_one('table.wikitable')
        title = r.select_one('#firstHeading').text
        image = r.select_one('.floatnone > a >img')
        if re.search(r'\(serie televisiva\)', title):
            title = re.sub(r'\(serie televisiva\)', '', title,
                           flags=re.IGNORECASE)
        serie = Serie(title.strip(), self._baseurl)

        serie.image = image['src'] if not image is None else None

        seasons = []
        if table:
            for row in table.find_all('tr')[1:]:
                season = self._parse_row(row)
                if not season is None:
                    seasons.append(season)
        serie.seasons = seasons
        return serie

    def refresh(self, serie: Serie) -> Serie:
        return self.get(serie.url)

    def _parse_date(self, date_str) -> Optional[datetime]:
        if date_str.strip() == '':
            return None
        return dateparser.parse(date_str)

    def _get_episodes(self, link) -> List[Episode]:
        page = requests.get(f'https://it.wikipedia.org{link}')

        doc = BeautifulSoup(page.text, 'lxml')
        table = doc.select_one('table.wikitable')
        if table is None:
            raise EpisodeNotFoundException()
        r_episodes = table.find_all('tr')[1:]

        episodes = []
        count = 1
        for r in [cells.find_all('td') for cells in r_episodes]:
            n = count
            count += 1
            original_title = r[1].text.strip()
            local_title = r[2].text.strip()
            first_aired = None
            local_aired = None
            if len(r) > 3:
                first_aired = self._parse_date(r[3].text.strip())
                if len(r) > 4:
                    local_aired = self._parse_date(r[4].text.strip())

            e = Episode(
                n,
                original_title,
                local_title,
                first_aired,
                local_aired
            )

            # logging.debug(e)
            episodes.append(e)

        return episodes

    def _parse_row(self, row) -> Dict:
        cell = row.find_all('td')
        season = cell[0].text.strip()
        season_link = cell[0].find('a')['href']
        str_episode = cell[1].text.strip()
        if str_episode == "":
            episodes = 0
        else:
            episodes = int(str_episode)
        first_aired = cell[2].text.strip()
        if len(cell) > 3:
            first_aired_it = cell[3].text.strip()

        try:
            s = Season(season, num_episodes=episodes, first_aired=first_aired,
                       local_aired=first_aired_it, episodes=self._get_episodes(season_link))
            logging.debug(s)
            return s
        except EpisodeNotFoundException:
            return None
