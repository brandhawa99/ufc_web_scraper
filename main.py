from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('https://www.ufc.com/rankings') as response:
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    categories = soup.find_all('h4')
    for cats in categories:
        print(cats.get_text())
