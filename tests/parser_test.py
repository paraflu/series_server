import unittest

from api.wiki_parser.episodes import Episodes


class TestParser(unittest.TestCase):

    def test_911(self):
        e = Episodes(
            'https://it.wikipedia.org/wiki/9-1-1_(serie_televisiva)#Episodi')
        season = e.get()

        self.assertGreaterEqual(5, len(season))

        serie = season[0]
        self.assertIsNotNone(serie)

    def test_the_good_doctor(self):
        p = Episodes(
            'https://it.wikipedia.org/wiki/The_Good_Doctor_(serie_televisiva)')
        seasons = p.get()
        self.assertGreaterEqual(5, len(seasons))

        self.assertEqual(18, seasons[0].num_episodes)
        self.assertEqual(18, seasons[1].num_episodes)
        self.assertEqual(20, seasons[2].num_episodes)

    def test_lone_star(self):
        p = Episodes('https://it.wikipedia.org/wiki/9-1-1:_Lone_Star')
        seasons = p.get()
        self.assertGreaterEqual(3, len(seasons))
        self.assertEqual(10, seasons[0].num_episodes)
        self.assertEqual(14, seasons[1].num_episodes)
        self.assertEqual(18, seasons[2].num_episodes)


if __name__ == '__main__':
    unittest.main()
