import urllib.request
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class Scraper(ABC):
    @abstractmethod
    def scrape(self):
        pass

    def get_table_of_contents(self):
        full_toc_page = Scraper.get_page_as_soup(self.table_of_contents_url())
        toc_element = full_toc_page.find(id=self.table_of_contents_element_id())
        return toc_element

    @staticmethod
    def get_page_as_soup(url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        return soup

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

    def table_of_contents_url(self):
        return self.TOC_URL

    def table_of_contents_element_id(self):
        return self.TOC_ELEMENT_ID
