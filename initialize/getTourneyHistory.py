from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.sports-reference.com/cbb/postseason/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

body = soup.find('tbody')

champions = []
championLinks = []

for row in body.find_all('tr'):
    print(row.prettify())
    header = row.find('th')
    link = header.find('a')
    if link:  # need if link exists as last row in table may not have NCAA tourney but NIT tourney which we don't want
        # print("header tag is", header)
        url = link['href']
        # Takes the first column with link of year and NCAA and splits text string into array and grabs first element which should be year e.g. 1980 NCAA will return 1980
        year = header.text.split()[0]
        championTag = row.find('td', {"data-stat": "ncaa_champ"})
        champion = championTag.text
        yearObj = {year: {"champion": champion, "url": url}}
        # print("url is", url)
        # print("url is type", type(url))
        champions.append(yearObj)
        # print("yearObj is", yearObj)
        # print("accessing Obj,", yearObj[year])
        # print("YEAR is", year)
        # print("!!! champion is", champion)
        # print("CHAMP LINK IS", link.get('href'))
        # print("*"*30)
        print("yearObj.champion is", yearObj[year]["champion"])
# print(champions)

with open('../champions.json', 'w') as f:
    json.dump(champions, f, indent=2)
