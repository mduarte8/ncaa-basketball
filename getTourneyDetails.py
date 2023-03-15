from bs4 import BeautifulSoup
import requests
import json
import sys
from getTeamId import getTeamId
import time
import random

baseUrl = "https://www.sports-reference.com"

f = open("champions.json", "rb")
jsonObject = json.load(f)
f.close()

# print(jsonObject)

# tourneyObj = jsonObject[0]
# print("tourneyObj is", tourneyObj)

# this accesses the single year key of the current yearObj, turns it into a list and accesses it as the first element in the list
# yearKey = list(tourneyObj.keys())[0]
# # print("year is", yearKey)
# winner = tourneyObj[yearKey]
# print("output is", winner)

# fullUrl = baseUrl + winner['url']
# print("fullUrl is", fullUrl)

# response = requests.get(fullUrl)
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
#
# bracket = soup.find('div', {"id": "brackets"})
# print("type(divisions is)", type(bracket))
# print("len(divisions) is", len(bracket))
# finds the divs which should be the direct children of "brackets" div
# only get the direct children
# divisions = bracket.find_all('div', recursive=False)
# print("divisions is", divisions)
# print(type(divisions)) #this is a ResultSet type

tourneyRounds = ['first', 'second', 'sweet16',
                 'elite8', 'final4', 'championship']

allTourneys = []



for index, tourneyObj in enumerate(jsonObject):
    yearKey = list(tourneyObj.keys())[0]
    # print("year is", yearKey)
    winner = tourneyObj[yearKey]
    fullUrl = baseUrl + winner['url']

    print("YEAR IS", yearKey)
    print(tourneyObj)
    pause_duration = random.randint(1, 5)
    time.sleep(pause_duration)

    response = requests.get(fullUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    bracket = soup.find('div', {"id": "brackets"})
    divisions = bracket.find_all('div', recursive=False)


    gameCounter = 0
    tourneyGames = []
    for division in divisions:

        print("@@@ division.id is", division.get('id'), "@@@" * 30)
        rounds = division.find_all('div', {"class": "round"})
        # print("Division id is", division.get('id'))
        # this is to check for the final four separate page, and corrects the round number since the page resets the rounds to 0 in a separate division div
        # print("rounds is", rounds)
        for index, round in enumerate(rounds):
            roundNum = index + 1 if division.get('id') != "national" else index + 4
            # print("round index issssss", roundNum)
            # print("#"*5, "Round", "#"*5)
            games = round.find_all('div', recursive=False)
            # print("len(games) is", len(games))
            for game in games:
                if not game.has_attr("class"):
                    # print("*"*10, "GAME", "*"*10)
                    # print("game.text is", game.text)
                    teams = game.find_all('div')
                    # print("len(teams is)", len(teams))
                    if len(teams) > 1:
                        gameObj = {"division": division.get('id')}
                        gameCounter += 1
                        gameObj["game_id"] = gameCounter
                        gameObj["round_num"] = roundNum
                        # location of game is stored as a span in the game div
                        try:
                            gameObj["location"] = game.find("span", recursive=False).text
                        except AttributeError:
                            gameObj["location"] = "Not available"
                        for index, team in enumerate(teams):
                            # print("/"*15, "team", "/"*15)
                            # print(team)
                            team_tags = team.find_all('a')
                            team_spans = team.find_all('span')
                            rank = team.span.text  # first span in the div should be the ranking of the team
                            teamObj = {"name": team_tags[0].text, "id": getTeamId(team_tags[0].text), "rank": rank,
                                    "team_url": team_tags[0]['href']}
                            print(teamObj['name'], "'s id is", getTeamId(teamObj['name']))
                            try:
                                teamObj["score"] = team_tags[1].text
                                gameObj["game_url"] = team_tags[1]['href']
                                if team.has_attr("class"):
                                    # print("team class is", team['class'])
                                    if 'winner' in team['class']:
                                        # returns a result set of a tags, as there are both a tags for Team name and Score
                                        # name should be first element found
                                        gameObj["winner"] = teamObj
                                        # score should be 2nd elment found
                                        # gameObj["winner_score"] = team_tags[1].text
                                        print("WINNER WINNER CHICKEN DINNER", team.text)
                                    # print(team.text)
                                    else:
                                        print(
                                            "something wrong should not be able to get to this since team obj needs winner class")
                                else:
                                    gameObj["loser"] = teamObj
                            except IndexError:
                                team_str = "team" + str(index)
                                gameObj[team_str] = teamObj
                            # print("/"*15, "end team", "/"*15)
                        tourneyGames.append(gameObj)
                    # print("*"*10, "end GAME", "*"*10)
            # print("#"*5, "end Round", "#"*5)
        # print("@"*6)
    tourneyDetailObj = {yearKey: tourneyGames}
    allTourneys.append(tourneyDetailObj)
    # print(tourneyGames)

    # body = soup.find('tbody')

with open('allTourneys.json', 'w') as f:
    json.dump(allTourneys, f, indent=2)
