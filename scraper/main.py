from NBAScraper import NBAScraper
import sys

if __name__ == '__main__':
    scraper_settings = {
        'path': '/Users/cyriltso/Documents/nba_prediction/scraper/chromedriver',
        'xpath': '/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select',
        'url': 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=XXXX-XX&SeasonType=Regular%20Season',
        'table': 'nba-stat-table__overflow',
        'csv_path': '/Users/cyriltso/Documents/nba_prediction'
    }

    store_type = sys.argv[1]
    season_year = sys.argv[2]
    csv_name = sys.argv[3]

    year_url_format = list(season_year.replace("/", "-"))
    del year_url_format[5:7]

    year_formated = "".join(year_url_format)

    season_url = scraper_settings['url'].replace("XXXX-XX", year_formated)

    nba_scraper = NBAScraper()

    team_rank, team_names, team_stats = nba_scraper.data_scraping(
        scraper_settings['path'], scraper_settings['xpath'],
        season_url, scraper_settings['table'])

    df_nba = nba_scraper.data_storage(
        team_rank, team_stats, 
        team_names, season_year)

    nba_scraper.csv_storage(
        df_nba, 
        csv_name, 
        scraper_settings['csv_path'],
        store_type)  


