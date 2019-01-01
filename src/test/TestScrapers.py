import unittest

from Scrapers import Scraper, TLAScraper


class TestScraper(unittest.TestCase):
    GOOGLE_URL = "https://www.google.com/"

    def test_links_to_chapters(self):
        soup = Scraper.get_page_as_soup(self.GOOGLE_URL)
        chapters = Scraper.get_all_links_from_toc(soup)
        self.assertIsNotNone(chapters)
        self.assertEqual(12, len(chapters))

    def test_get_page_as_soup_not_null(self):
        self.assertIsNotNone(Scraper.get_page_as_soup(self.GOOGLE_URL))


class TestTLAScraper(unittest.TestCase):
    tla_scraper = TLAScraper()

    def test_get_all_links_not_null(self):
        chapters = self.tla_scraper.get_all_links_from_toc()
        self.assertIsNotNone(chapters)

    def test_get_all_links_correct_count(self):
        chapters = self.tla_scraper.get_all_links_from_toc()
        self.assertEqual(73, len(chapters))

    def test_get_table_of_contents_not_null(self):
        self.assertIsNotNone(self.tla_scraper.get_table_of_contents())

    def test_has_toc_url(self):
        self.assertIsNotNone(self.tla_scraper.table_of_contents_url())

    def test_has_toc_element_id(self):
        self.assertIsNotNone(self.tla_scraper.table_of_contents_element_id())


if __name__ == '__main__':
    unittest.main()
