import unittest

from Scrapers import Scraper, TLAScraper
from Chapter import Chapter


class TestScraper(unittest.TestCase):
    GOOGLE_URL = "https://www.google.com/"
    PROLOGUE_POST = "https://forums.spacebattles.com/threads/the-last-angel.244209/#post-9354450"

    def test_links_to_chapters(self):
        soup = Scraper.get_page_as_soup(self.GOOGLE_URL)
        chapters = Scraper.get_links_from_soup(soup)
        self.assertIsNotNone(chapters)
        self.assertEqual(21, len(chapters))

    def test_get_page_as_soup_not_null(self):
        self.assertIsNotNone(Scraper.get_page_as_soup(self.GOOGLE_URL))

    def test_scrape_chapter_contents(self):
        chapter = Chapter("Prologue", "https://forums.spacebattles.com/threads/the-last-angel.244209/#post-9354450")
        Scraper.scrape_chapter_contents(chapter)
        self.assertIsNotNone(chapter.text)


class TestTLAScraper(unittest.TestCase):
    tla_scraper = TLAScraper()

    def test_get_chapters(self):
        chapters = self.tla_scraper.get_chapters()
        self.assertIsNotNone(chapters)
        self.assertEqual(48, len(chapters))

    def test_filter_chapters(self):
        soup = self.tla_scraper.get_toc_as_soup()
        all_links = self.tla_scraper.get_links_from_soup(soup)
        all_chapters = Scraper.links_to_chapters(all_links)
        filtered_chapters = self.tla_scraper.filter_chapters(all_chapters)
        self.assertIsNotNone(filtered_chapters)
        self.assertEqual(48, len(filtered_chapters))

    def test_get_links_from_soup_not_null(self):
        soup = self.tla_scraper.get_toc_as_soup()
        chapters = self.tla_scraper.get_links_from_soup(soup)
        self.assertIsNotNone(chapters)

    def test_get_links_from_soup_correct_count(self):
        soup = self.tla_scraper.get_toc_as_soup()
        chapters = self.tla_scraper.get_links_from_soup(soup)
        self.assertEqual(73, len(chapters))

    def test_get_toc_as_soup_not_null(self):
        self.assertIsNotNone(self.tla_scraper.get_toc_as_soup())

    def test_has_toc_url(self):
        self.assertIsNotNone(self.tla_scraper.get_toc_url())

    def test_has_toc_element_id(self):
        self.assertIsNotNone(self.tla_scraper.get_toc_element_id())


if __name__ == '__main__':
    unittest.main()
