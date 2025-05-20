import unittest

import solution


class TestWikiParser(unittest.TestCase):

    def test_next_page(self):
        link = solution.wiki_animal_parser(solution.WIKI_URL)
        self.assertTrue(type(link), str)
        self.assertTrue(solution.BASE_URL in link)


if __name__ == '__main__':
    unittest.main()
