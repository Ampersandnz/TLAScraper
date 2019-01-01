from Scrapers import *

scrapers = {TLAScraper(), TAFScraper(), TLAAScraper(), BitPScraper(), QScraper(), SScraper(), STScraper(), ULtHScraper()}


def main():
    for scraper in scrapers:
        scraper.scrape()


if __name__ == '__main__':
    main()
