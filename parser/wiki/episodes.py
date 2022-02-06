from bs4 import BeautifulSoup
import requests


class Episode(object):
    def __init__(self, baseurl: str):
        # self._baseurl = baseurl
        self._baseurl = 'https://it.wikipedia.org/wiki/9-1-1_(serie_televisiva)#Episodi'

    def get(self):
        response = requests.get(self._baseurl)
        data = response.text
        r = BeautifulSoup(data, 'lxml')
