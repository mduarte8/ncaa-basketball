import json

f = open("teamIds.json", "rb")
teamJsonObject = json.load(f)
f.close()

# print("from GET TEAM ID", teamJsonObject)


def getTeamId(teamTextId):  # takes in the url route of team to id
    team = next((team for team in teamJsonObject if team['textId'] == teamTextId), None)
    print(team)
    if team:
        return team['id']
    else:
        print("Team not found")
        return None


def addTeam(teamName, teamTextId, teamUrl):
    with open("teamIds.json", "r+") as f:
        data = json.load(f)
        newTeam = {"id": len(data) + 1, "name": teamName, "textId": teamTextId, "url":teamUrl}
        data.append(newTeam)
        print("added to team.json")
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

