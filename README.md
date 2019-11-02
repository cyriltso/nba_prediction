# NBA Regular Season 2019/2020 Ranking prediction

## 1. Introduction

This is a personal project that aims to predict the NBA teams regular season ranking for the 2019/2020 season.

To do this, we will approach the problem as a multi-class classification, indeed, our target variable to classify will be the rank of all teams (1 to 15).

This project aims to help me to improve my skills in Supervised Learning and especially to help me to handle a target variable with multiple modalities. This project
should also help me to improve my abilities to do manage an entire Data Science entirely (from Data Acquisition to Machine Learning modeling).

## 2. Collecting the data

The data was collected from 1996 to 2019 through the use of webscraping on https://stats.nba.com.

After being scraped, the data got stored in a CSV file, which is very easy to convert to a DataFrame through Pandas.

## 3. Technical Stack

- Programming language : Python 3.7
- Tools : Visual Studio Code, Jupyter Notebook, Git, Chromedriver (for dynamic website scraping with Selenium)
- Libraries : Pandas, Numpy, Seaborn, Matplotlib, Scikit-Learn, Selenium

## 4. Contents of the repository

- A notebook that contains the analysis, visualization and modeling.
- The NBA Teams Regular Season dataset in a CSV file.
- A Python script containing the scraper algorithm.
- A Python main script allowing the user to use the scraper.

## 5. Warning

To be able to use the scraper, you will need to have a webdriver installed in the same folder than the main.py script (as Selenium uses it to launch the scraping), otherwise, the scraper won't work.
