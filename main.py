from bs4 import BeautifulSoup
import requests


URL = 'https://www.ufc.com/rankings'
LEARNING_URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Web+Developer&txtLocation=Canada"
html_text = requests.get(LEARNING_URL).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('li', class_="clearfix job-bx wht-shd-bx")
publish_date = jobs.find('span', class_='sim-posted').span.text.strip()
comp = jobs.find('h3', class_="joblist-comp-name").text.replace(" ", "")
skills = jobs.find('span', class_="srp-skills").text.strip()
print(f'''
Company Name: {comp}
Required Skills: {skills}
date: {publish_date}
''')
