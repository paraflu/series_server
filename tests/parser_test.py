import unittest
from parser.wiki import Episode


class TestParser(unittest.TestCase):

    def test_get(self):
        e = Episode()
        r = e.get()
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
