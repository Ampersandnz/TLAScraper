import unittest

from Scrapers import TLAScraper


class TestTLAScraper(unittest.TestCase):
    def class_exists(self):
        scraper = TLAScraper()
        self.assertIsNotNone(scraper)

    def has_toc_url(self):
        scraper = TLAScraper()
        self.assertIsNotNone(scraper.table_of_contents_url())

    def has_toc_element_id(self):
        scraper = TLAScraper()
        self.assertIsNotNone(scraper.table_of_contents_element_id())


if __name__ == '__main__':
    unittest.main()
