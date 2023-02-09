from bs4 import BeautifulSoup
import requests

url = 'https://www.sports-reference.com/cbb/postseason/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

body = soup.find('tbody')

for row in body.find_all('tr'):
    print(row.prettify())
    link = row.find('a')
    print(link.get('href'))
