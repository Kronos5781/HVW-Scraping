#! /usr/bin/env python3

from datetime import datetime as dt

from hvwscraper import Scraper


def main():

    # config
    start = dt(year=2024, month=1, day=1)
    stop = dt(year=2024, month=9, day=30)

    # ARBEIT ARBEIT ARBEIT
    scraper = Scraper()
    scraper.scrape(start, stop)


if __name__ == "__main__":
    main()
