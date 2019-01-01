import unittest

from scraper.TLAScraper import TLAScraper


class TestTLAScraper(unittest.TestCase):
    def class_exists(self):
        scraper = TLAScraper()
        self.assertIsNotNone(scraper)


if __name__ == '__main__':
    unittest.main()
