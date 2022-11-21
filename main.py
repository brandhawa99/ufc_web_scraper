#!/usr/bin/env
from bs4 import BeautifulSoup
import requests
# URL for UFC rankings
UFC_URL = 'https://www.ufc.com/rankings'
# Get ufc rankings page HTML;
html_text = requests.get(UFC_URL).text
soup = BeautifulSoup(html_text, 'lxml')
# get all the different divisions
divisions = soup.find_all('div', class_="view-grouping-content")
for division in divisions:
  # Get division, champion and all the contenders in that division
    champ = division.find('a').text
    division_name = division.find('h4').text
    contenders = division.find_all("tr")
    print('----------')
    print(f"DIVISION: {division_name}")
    print(f"Champion: {champ}")
    for contender in contenders:
      # go through contenders and find their rank name and how their position has changed in current division
        contender_rank = contender.find(
            'td', class_="views-field views-field-weight-class-rank").text
        contender_name = contender.find('div', class_="views-row").a.text
        conteder_change = contender.find(
            'td', class_="views-field views-field-weight-class-rank-change").text
        # only if their rank has changed show
        if "Rank" in conteder_change or "NR" in conteder_change:
            print(
                f"Rank: {contender_rank.strip()}, Name: {contender_name.strip()}, Change: {conteder_change}")
