#!/usr/bin/env
from bs4 import BeautifulSoup
import requests

UFC_URL = 'https://www.ufc.com/rankings'
LEARNING_URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Web+Developer&txtLocation=Canada"

# Get ufc rankings page HTML;
html_text = requests.get(UFC_URL).text
soup = BeautifulSoup(html_text, 'lxml')
# get all the different divisions
divisions = soup.find_all('div', class_="view-grouping-content")
for division in divisions:
  # Get champ div name and all the contenders
    champ = division.find('a').text
    division_name = division.find('h4').text
    contenders = division.find_all("tr")
    print('----------')
    print(f"DIVISION: {division_name}")
    print(f"Champion: {champ}")
    for contender in contenders:
      # go through contenders and find their rank name and how their position has changed
        contender_rank = contender.find(
            'td', class_="views-field views-field-weight-class-rank").text
        contender_name = contender.find('div', class_="views-row").a.text
        conteder_change = contender.find(
            'td', class_="views-field views-field-weight-class-rank-change").text
        print(
            f"Rank: {contender_rank.strip()}, Name: {contender_name.strip()}, Change: {conteder_change}")
