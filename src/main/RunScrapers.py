from Scrapers import TLAScraper

scrapers = {TLAScraper()}


def main():
    for scraper in scrapers:
        scraper.scrape()


if __name__ == '__main__':
    main()
