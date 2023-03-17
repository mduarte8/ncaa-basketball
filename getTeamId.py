import json

f = open("teamIds.json", "rb")
teamJsonObject = json.load(f)
f.close()

# print("from GET TEAM ID", teamJsonObject)


def getTeamId(teamTextId):  # takes in the url route of team to id
    team = next((team for team in teamJsonObject if team['textId'] == teamTextId), None)
    print(team)
    print("length of JSON object is", len(teamJsonObject))
    if team:
        return team['id']
    else:
        print("Team",teamTextId, "not found")
        return None


def addTeam(teamName, teamTextId, teamUrl):
    print("adding team", teamName, teamTextId, teamUrl)
    with open("teamIds.json", "r+") as g:
        data = json.load(g)
        newTeam = {"id": len(data) + 1, "name": teamName, "textId": teamTextId, "url":teamUrl}
        data.append(newTeam)
        print("added to team.json")
        g.seek(0)
        json.dump(data, g, indent=2)
        g.truncate()

