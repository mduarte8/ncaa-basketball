from bs4 import BeautifulSoup
import requests
import json

# Returns a result set of beatuiful soup objects, each element representing a row in /cbb/seasons/men/####-year


def getSchoolsTable(suffix_url):
    # uses 2023 school stats page to get school season stat tbody
    baseUrl = "https://www.sports-reference.com"

    response = requests.get(baseUrl + suffix_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    body = soup.find('tbody')
    rows = body.find_all('tr')

    return rows
