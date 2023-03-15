from bs4 import BeautifulSoup
import requests
import json
from getSchoolSeasonData import getSchoolsTable


suffix_url = "/cbb/seasons/men/2023-school-stats.html"

teams = []

for school in getSchoolsTable(suffix_url):
    if not school.has_attr("class"):
        headerCol = school.find("th")
        schoolCol = school.find("td", {"data-stat": "school_name"})
        teamObj = {"id": int(headerCol.text), "name": schoolCol.find('a').text}
        teams.append(teamObj)

print(teams)

with open('../teamIds.json', 'w') as f:
    json.dump(teams, f, indent=2)

# if (team.has_attr("class")):
#                         print("team class is", team['class'])
#                         if 'winner' in team['class']:
