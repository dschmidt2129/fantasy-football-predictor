import PFRScraper

def main():
    stat_type = input('enter a stat type (kicking, passing, rushing, receiving): ')
    year = input('enter a year (2020, 2021): ')
    scraper = PFRScraper.PFRScraper()
    scraper.scrape(year, stat_type)

if __name__ == '__main__':
    main()