from getTeamId import *


testTeam = {"name": "Stanford Cardinal", "textId": "stanford", "teamUrl": "/some/stuff/here"}
testTeam = {"name": "Stanford Poopers", "textId": "stanford-pratters", "teamUrl": "/some/stuff/here"}


print(testTeam);

if getTeamId(testTeam["textId"]):
    print("success")
    print(getTeamId(testTeam["textId"]))
else:
    addTeam(testTeam['name'], testTeam["textId"], testTeam["teamUrl"])