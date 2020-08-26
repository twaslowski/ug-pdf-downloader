import unittest
from src.parsers import search_parser


class UgDataParserTest(unittest.TestCase):
    def test_should_return_false_if_url_contains_pro(self):
        pro_url = "https://www.ultimate-guitar.com/pro/?utm_source=UltimateGuitar&amp;utm_medium=Search&amp" \
                  ";utm_campaign=UG+Search&amp;utm_content=Official+Version&amp;artist=Backstreet%20Boys&amp;song=i" \
                  "%20want%20it%20that%20way"
        self.assertEqual(False, search_parser._song_url_does_not_contain_pro_keyword(pro_url))

    def test_should_return_true_if_url_does_not_contain_pro(self):
        normal_url = "https://tabs.ultimate-guitar.com/tab/backstreet-boys/i-want-it-that-way-chords-17665"
        self.assertEqual(True, search_parser._song_url_does_not_contain_pro_keyword(normal_url))


if __name__ == '__main__':
    unittest.main()
