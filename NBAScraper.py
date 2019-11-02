# Package that allow the user to scrape the teams data from stats.nba.com.
# The user will be able to scrape the teams data from different years by
# changing the value of the url in the dictionnary below.

# Chromedriver must be located in the same folder with the Python script
# file in order to be able to launch the scraping process.

# The scraping code below has been highly inspired by the article from
# Kevin Song available here : http://kevincsong.com/Scraping-stats.nba.com-with-python/

### Importing Libraries

from selenium import webdriver
import pandas as pd 
import os

### Content of the class

class NBAScraper(object):
    """
    Class that allows the user to scrape the data from nba.stats.com
    and to store it inside of a Pandas DataFrame.
    """
    
    def data_scraping(self, path, xpath, url, table):
        """
        Method allowing the user to scrape the data from stats.nba.com.
        All the data will be stored in dedicated lists.

        Parameters:
            - path: location of the webdriver application.
            - xpath: location of the content to scrape on the website.
            - url: website to scrape the data on.
            - table: id of the content to scrape.
        """

        ### Initializing the scraper on the content of the website

        browser = webdriver.Chrome(os.path.join(os.getcwd(), path))
        browser.get(url)
        browser.find_element_by_xpath(xpath)

        self.table = browser.find_element_by_class_name(table)

        ### Storing the scraped data on dedicated lists

        self.team_rank = []
        self.team_names = []
        self.team_stats = []

        for line_rank, lines in enumerate(self.table.text.split('\n')):
            if line_rank == 0:
                lines.split(' ')[0:5]
            else:
                if line_rank % 3 == 1:
                    self.team_rank.append(lines)
                if line_rank % 3 == 2:
                    self.team_names.append(lines)
                if line_rank % 3 == 0:
                    self.team_stats.append([float(i) for i in lines.split(' ')])

        return self.team_rank, self.team_names, self.team_stats
    
    def data_storage(self, rank, stats, names, season):
        """
        Method that allows the user to store the scraped data in a 
        Pandas DataFrame.

        Parameters:
            - rank: data related to the ranks of each team.
            - stats: data related to the statistics of each team.
            - names : data related to the names of each team.
            - season : NBA season scraped.
        """

        ### Storing the scraped data in a dictionnary

        self.data = {
            'season': season,
            'team': names,
            'rank': rank,
            'game_played': [i[0] for i in stats],
            'wins': [i[1] for i in stats],
            'losses': [i[2] for i in stats],
            'wins_ratio': [i[3] for i in stats],
            'minutes_played': [i[4] for i in stats],
            'scoring_average': [i[5] for i in stats],
            'field_goals_made': [i[6] for i in stats],
            'field_goals_attempts': [i[7] for i in stats],
            'field_goals_percentage': [i[8] for i in stats],
            'three_points_made': [i[9] for i in stats],
            'three_points_attempts': [i[10] for i in stats],
            'three_points_percentage': [i[11] for i in stats],
            'free_throws_made': [i[12] for i in stats],
            'free_throws_attempts': [i[13] for i in stats],
            'free_throws_percentage': [i[14] for i in stats],
            'offensive_rebounds': [i[15] for i in stats],
            'defensive_rebounds': [i[16] for i in stats],
            'total_rebounds': [i[17] for i in stats],
            'assists': [i[18] for i in stats],
            'turnovers': [i[19] for i in stats],
            'steals': [i[20] for i in stats],
            'blocks': [i[21] for i in stats],
            'blocks_attempts': [i[22] for i in stats],
            'personal_fouls': [i[23] for i in stats],
            'personal_fouls_drawn': [i[24] for i in stats],
            'plus_minus': [i[25] for i in stats],
        }

        ### Creating a Pandas DataFrame through the dictionnary

        self.df_nba = pd.DataFrame(self.data)
        self.df_nba['rank'] = self.df_nba.index + 1
 
        return self.df_nba
    
    def csv_storage(self, df, file_name, csv_path):
        """
        Method that allows the user to store the DataFrame to a CSV file.

        Parameters:
            - df: DataFrame to store in the CSV file.
            - file_name: name of the CSV file.
            - csv_path: location of the stored CSV file.
        """

        self.df = df
        self.file_name = file_name
        self.csv_path = csv_path
        
        self.df.to_csv(os.path.join(self.csv_path, self.file_name), index=False)