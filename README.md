# NBA 2019/2020 season winner prediction

## 1. Introduction

This is a personal project that aims to predict the NBA winner of the 2019/2020 season.

To do this, we will create a scoring algorithm i.e an algorithm that will be able to rank each team probabilities of winning the NBA title.

This project aims to help me to improve my skills in Supervised Learning and to improve my abilities to do manage an entire Data Science entirely (from Data Acquisition to Machine Learning modeling).

## 2. Collecting the data

The data was collected from 1996 to 2019 through the use of webscraping on https://stats.nba.com.

After being scraped, the data got stored in a CSV file, which is very easy to convert to a DataFrame through Pandas.

To use the scraper to collect the data by yourself, follow the instrutions below :

-  Clone this repo in your folder :

```
git clone https://github.com/cyriltso/nba_prediction.git
```

-  Make sure that you have all the needed dependancies.

-  Then, place yourself inside of this repo :

```
cd /your_folder/nba_prediction
```

-  Finally, launch this command (depending on your Python version, if you are under Python 2.X use `python` and if your are under Python 3.X use `python3` at the beginning of the command) :

```
python -m main season_year csv_name
```
OR

```
python3 -m main season_year csv_name
```

Where :
-  `season_year` : the season for which you want to collect the data.
-  `csv_name` : the name of the csv that will contain the extracted data.

For example, if I want to scrape the data related to the 2019/2020 season, I will launch the following command (i'm under Python 3.7.4 64-bit) : 

```
python3 -m main 2019/2020 teams_stats_20192020.csv
```

After launching this command, the `teams_stats_20192020.csv` file will appear in the folder of this script.

## 3. Technical Stack

- Programming language : Python 3.7
- Tools : Visual Studio Code, Jupyter Notebook, Git, Chromedriver (for dynamic website scraping with Selenium)
- Libraries : Pandas, Numpy, Seaborn, Matplotlib, Scikit-Learn, Selenium

## 4. Contents of the repository

- A notebook that contains the analysis, visualization and modeling.
- The NBA Teams Regular Season dataset in a CSV file.
- A Python script containing the scraper algorithm.
- A Python main script allowing the user to use the scraper.
- Python files containing the analysis and modeling parts of the project.

## 5. Warning

To be able to use the scraper, you will need to have a webdriver installed in the same folder than the main.py script (as Selenium uses it to launch the scraping), otherwise, the scraper won't work.
