import json
from getTeamId import getTeamId, addTeam

f = open("allTourneys.json", "r+")
tourneys = json.load(f)

print(tourneys[0])

g = open("teamIds.json", "r+")
teamIds = json.load(g)

def getTextIdFromUrl(urlString):
    urlArray = urlString.split("/")
    return urlArray[3] #school-unique text identified should be after 3rd slash, where split will create empty index at 0 given leading slash

def addNewTeam(teamName, teamTextId, teamUrl):
    newTeam = {"id": len(teamIds) + 1, "name": teamName, "textId": teamTextId, "url":teamUrl}
    teamIds.append(newTeam)
    return len(teamIds) + 1


def checkTeamId(teamName, teamTextId, teamUrl):
    teamObj = next((team for team in teamIds if team['textId'] == teamTextId), None)
    print(teamObj)
    print("length of JSON object is", len(teamIds))
    if teamObj:
        return teamObj['id']
    else:
        print("Team", teamTextId, "not found")
        return addNewTeam(teamName, teamTextId, teamUrl)

for year in tourneys:
    print("*"*50)
    # print(year)
    for tourney in year.values():
        print("*" * 50)
        # print(tourney)
        for game in tourney:
            teams = ["winner", "loser"]
            for team in teams:
                currentTeam = game[team]
                teamName = currentTeam["name"]
                url = currentTeam["team_url"]
                textId = getTextIdFromUrl(url)
                currentTeam["id"] = checkTeamId(teamName, textId, url)

                # if getTeamId(textId):
                #     currentTeam["id"] = getTeamId(textId)
                # else:
                #     addTeam(currentTeam["name"], textId, url)

    # print(year)
f.seek(0)
json.dump(tourneys, f, indent=2)
f.truncate()
f.close()


g.seek(0)
json.dump(teamIds, g, indent=2)
g.truncate()
g.close()


