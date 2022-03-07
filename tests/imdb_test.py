import unittest

from imdbstore import IMDBStore, Serie


class TestIMDB(unittest.TestCase):
    def test_query(self):
        st = IMDBStore()

        movies = st.search('911')
        self.assertIsNotNone(movies)
        self.assertNotEqual(0, len(movies))

        self.assertIn('tv series', [m['kind'] for m in movies])

        first = movies[0]
        st.update(first)

        self.assertNotEqual(0, len(first['episodes']))


class TestSerieIMDB(unittest.TestCase):
    def test_matrix(self):
        s = Serie('0133093')
        self.assertIsNotNone(s)
        self.assertIsNone(s.episodes)

    def test_911(self):
        db = IMDBStore()
        res = db.search('911', episode_parse=True, limit=1)
        it = res[0]
        self.assertIsNotNone(it)
        self.assertIn('tv series', it.kind)
        self.assertIsNotNone(it['episodes'])
        self.assertNotEqual(0, len(it['episodes']))
        self.assertEqual(len(it['episodes']), len(it.episodes))

        self.assertNotEqual(0, it.seasons_no)
        self.assertNotEqual(0, it.season(1))


if __name__ == '__main__':
    unittest.main()
