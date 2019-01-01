from Scrapers import TLAScraper, TAFScraper, TLAAScraper

scrapers = {TLAScraper(), TAFScraper(), TLAAScraper()}


def main():
    for scraper in scrapers:
        scraper.scrape()


if __name__ == '__main__':
    main()
