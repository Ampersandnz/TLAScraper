import unittest


class TestTLAScraper(unittest.TestCase):
    def class_exists(self):
        def scraper = TLAScraper()
        self.assertIsNotNone(scraper)


if __name__ == '__main__':
    unittest.main()
