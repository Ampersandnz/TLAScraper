import unittest

from Scrapers import Scraper, TLAScraper


class TestScraper(unittest.TestCase):
    GOOGLE_URL = "https://www.google.com/"

    def test_links_to_chapters(self):
        soup = Scraper.get_page_as_soup(self.GOOGLE_URL)
        chapters = Scraper.get_all_links_from_soup(soup)
        self.assertIsNotNone(chapters)
        self.assertEqual(21, len(chapters))

    def test_get_page_as_soup_not_null(self):
        self.assertIsNotNone(Scraper.get_page_as_soup(self.GOOGLE_URL))


class TestTLAScraper(unittest.TestCase):
    tla_scraper = TLAScraper()

    def test_filter_chapters(self):
        soup = self.tla_scraper.get_table_of_contents_as_soup()
        all_links = self.tla_scraper.get_all_links_from_soup(soup)
        all_chapters = Scraper.links_to_chapters(all_links)
        filtered_chapters = self.tla_scraper.filter_chapters(all_chapters)
        self.assertIsNotNone(filtered_chapters)
        self.assertEqual(48, len(filtered_chapters))

    def test_get_all_links_not_null(self):
        soup = self.tla_scraper.get_table_of_contents_as_soup()
        chapters = self.tla_scraper.get_all_links_from_soup(soup)
        self.assertIsNotNone(chapters)

    def test_get_all_links_correct_count(self):
        soup = self.tla_scraper.get_table_of_contents_as_soup()
        chapters = self.tla_scraper.get_all_links_from_soup(soup)
        self.assertEqual(73, len(chapters))

    def test_get_table_of_contents_not_null(self):
        self.assertIsNotNone(self.tla_scraper.get_table_of_contents_as_soup())

    def test_has_toc_url(self):
        self.assertIsNotNone(self.tla_scraper.table_of_contents_url())

    def test_has_toc_element_id(self):
        self.assertIsNotNone(self.tla_scraper.table_of_contents_element_id())


if __name__ == '__main__':
    unittest.main()
