from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def scrape(self):
        pass


class TLAScraper(Scraper):
    def scrape(self):
        pass
