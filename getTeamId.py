import json

f = open("teamIds.json", "rb")
teamJsonObject = json.load(f)
f.close()

# print("from GET TEAM ID", teamJsonObject)


def getTeamId(teamName):  # takes in string of team name
    team = next((team for team in teamJsonObject if team['name'] == teamName), None)
    if team:
        return team['id']
    else:
        newId = len(teamJsonObject) + 1
        addTeam(teamName, newId)
        return newId


def addTeam(teamName, newId):
    with open("teamIds.json", "r+") as f:
        data = json.load(f)
        newTeam = {"id": newId, "name": teamName}
        data.append(newTeam)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

