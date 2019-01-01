import urllib.request
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from Chapter import Chapter


class Scraper(ABC):
    def scrape(self):
        chapters = self.get_chapters()

        print(f"About to scrape the contents of {len(chapters)} chapters")

        full_output = ""

        for chapter in chapters:
            Scraper.scrape_chapter_contents(chapter)
            full_output = full_output + '\n'
            full_output = full_output + chapter.text

        # Build output document
        print(full_output)
        self.write_to_file(full_output)

    def get_chapters(self):
        soup = self.get_toc_as_soup()
        all_links = self.get_links_from_soup(soup)
        all_chapters = Scraper.links_to_chapters(all_links)
        filtered_chapters = self.filter_chapters(all_chapters)
        return filtered_chapters

    @staticmethod
    def get_links_from_soup(soup):
        links = soup.find_all('a')
        return links

    def get_toc_as_soup(self):
        return Scraper.get_post_as_soup(self.get_toc_url(), self.get_toc_element_id())

    @staticmethod
    def get_post_as_soup(url, element_id):
        full_toc_page = Scraper.get_page_as_soup(url)
        toc_soup = full_toc_page.find(id=element_id)
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

    @staticmethod
    def scrape_chapter_contents(chapter):
        post_id = chapter.get_post_id()
        post = Scraper.get_post_as_soup(chapter.url, post_id)
        content = post.find("div", {"class": "messageContent"})
        text = content.prettify()
        chapter.set_body_text(text)

    def write_to_file(self, text):
        file = open(self.get_filename(), "w+")
        file.write(text)
        file.close()

    @abstractmethod
    def filter_chapters(self, all_chapters):
        pass

    @abstractmethod
    def get_toc_url(self):
        pass

    @abstractmethod
    def get_toc_element_id(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass


class TLAScraper(Scraper):
    TOC_URL = "https://forums.spacebattles.com/threads/the-last-angel.244209/"
    TOC_ELEMENT_ID = "post-9354450"
    FILENAME = "The Last Angel.html"

    def filter_chapters(self, all_chapters):
        filtered_chapters = []

        for chapter in all_chapters:
            if "Chapter" in chapter.title or "Epilogue" in chapter.title:
                filtered_chapters.append(chapter)

        return filtered_chapters

    def get_toc_url(self):
        return self.TOC_URL

    def get_toc_element_id(self):
        return self.TOC_ELEMENT_ID

    def get_filename(self):
        return self.FILENAME
