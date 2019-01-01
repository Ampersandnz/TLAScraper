from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def scrape(self):
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

    def table_of_contents_url(self):
        return self.TOC_URL

    def table_of_contents_element_id(self):
        return self.TOC_ELEMENT_ID
