# Main function in which we will call the methods in the NBAScraper 
# class in order to store the scraped data in a CSV file.

from NBAScraper import NBAScraper
import sys

if __name__ == '__main__':
    scraper_settings = {
        'path': your_webdriver_pathfile,
        'xpath': '/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select',
        'url': 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season',
        'table': 'nba-stat-table__overflow',
        'season': '2019/2020',
        'csv_path': the_pathfile_for_the_csv,
        'csv_name': name_of_your_csv
    }

    nba_scraper = NBAScraper()

    team_rank, team_names, team_stats = nba_scraper.data_scraping(
        scraper_settings['path'], scraper_settings['xpath'],
        scraper_settings['url'], scraper_settings['table'])

    df_nba = nba_scraper.data_storage(
        team_rank, team_stats, 
        team_names, scraper_settings['season'])

    nba_scraper.csv_storage(df_nba, scraper_settings['csv_name'], scraper_settings['csv_path'])  


