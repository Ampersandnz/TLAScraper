import unittest

from Scrapers import TLAScraper


class TestTLAScraper(unittest.TestCase):
    scraper = TLAScraper()
    GOOGLE_URL = "https://www.google.com/"

    def test_class_exists(self):
        self.assertIsNotNone(self.scraper)

    def test_get_all_links_not_null(self):
        chapters = self.scraper.get_all_links()
        self.assertIsNotNone(chapters)

    def test_get_all_links_correct_count(self):
        chapters = self.scraper.get_all_links()
        self.assertEqual(73, len(chapters))

    def test_get_table_of_contents_not_null(self):
        self.assertIsNotNone(self.scraper.get_table_of_contents())

    def test_get_page_not_null(self):
        self.assertIsNotNone(TLAScraper.get_page_as_soup(self.GOOGLE_URL))

    def test_has_toc_url(self):
        self.assertIsNotNone(self.scraper.table_of_contents_url())

    def test_has_toc_element_id(self):
        self.assertIsNotNone(self.scraper.table_of_contents_element_id())


if __name__ == '__main__':
    unittest.main()
