import urllib.request
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from Chapter import Chapter


class Scraper(ABC):
    @abstractmethod
    def scrape(self):
        chapters = self.get_chapters()

        for chapter in chapters:
            pass
            # Scrape its contents

        # Build output document
        pass

    def get_chapters(self):
        soup = self.get_table_of_contents_as_soup()
        all_links = self.get_links_from_soup(soup)
        all_chapters = Scraper.links_to_chapters(all_links)
        filtered_chapters = self.filter_chapters(all_chapters)
        return filtered_chapters

    @staticmethod
    def get_links_from_soup(soup):
        links = soup.find_all('a')
        return links

    def get_table_of_contents_as_soup(self):
        full_toc_page = Scraper.get_page_as_soup(self.table_of_contents_url())
        toc_soup = full_toc_page.find(id=self.table_of_contents_element_id())
        return toc_soup

    @staticmethod
    def get_page_as_soup(url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    @staticmethod
    def links_to_chapters(links):
        chapters = []

        for link in links:
            chapters.append(Chapter(link.get_text(), link.get('href')))

        return chapters

    @abstractmethod
    def filter_chapters(self, all_chapters):
        pass

    @abstractmethod
    def table_of_contents_url(self):
        pass

    @abstractmethod
    def table_of_contents_element_id(self):
        pass


class TLAScraper(Scraper):
    TOC_URL = "https://forums.spacebattles.com/threads/the-last-angel.244209/"
    TOC_ELEMENT_ID = "post-9354450"

    def scrape(self):
        pass

    def filter_chapters(self, all_chapters):
        filtered_chapters = []

        for chapter in all_chapters:
            if "Chapter" in chapter.title or "Epilogue" in chapter.title:
                filtered_chapters.append(chapter)

        return filtered_chapters

    def table_of_contents_url(self):
        return self.TOC_URL

    def table_of_contents_element_id(self):
        return self.TOC_ELEMENT_ID
