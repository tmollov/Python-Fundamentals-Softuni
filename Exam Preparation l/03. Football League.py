import re
from functools import reduce
rTeam = r"(\w+)"
rScore = r"[0-9]:[0-9]"
        
def Winner(score1,score2):
    if score1 > score2:
        return 3
    elif score1 == score2:
        return 1
    return 0
teamsDic = dict()
decryptKey = input()

while True:
    line = input()
    if line == "final":
        break
    
    teams = list(map(lambda x: x.upper()[::-1],
                re.findall(f"{re.escape(decryptKey)}{rTeam}{re.escape(decryptKey)}",line)))
    if len(teams) == 1:
        continue
    score = list(map(int,re.findall(rScore,line)[0].split(":")))
    w1 = Winner(score[0],score[1])
    w2 = Winner(score[1],score[0])
    if teamsDic.__contains__(teams[0]):
        teamsDic[teams[0]][0] += w1 
        teamsDic[teams[0]][1] += score[0]
    else :
        teamsDic.__setitem__(teams[0],[w1,score[0]])
        
    if teamsDic.__contains__(teams[1]):   
        teamsDic[teams[1]][0] += w2 
        teamsDic[teams[1]][1] += score[1]
    else :
        teamsDic.__setitem__(teams[1],[w2,score[1]])
        


leagueStanding = sorted(teamsDic,key=lambda x: teamsDic[x][0],reverse=True).sort(key=lambda a,b: len(a) < len(b))
topGoals = sorted(teamsDic,key=lambda x: teamsDic[x][1],reverse=True)[:3]
print("League standings:")
i = 1
for team in leagueStanding:
    print(f"{i}. {team} {teamsDic[team][0]}")
    i+=1  

print("Top 3 scored goals:")
for team in topGoals:
    print(f"- {team} -> {teamsDic[team][1]}")
    
    
    
    
    teams = {}
 
    key = input()
    while True:
        command = input()
        if command == "final":
            break
        team_1_encrypted, team_2_encrypted, result = command.split()
        goals_team_1, goals_team_2 = (int(item) for item in result.split(":"))
        team1 = ((team_1_encrypted.split(key))[1].split(key)[0])[::-1].upper()
        team2 = ((team_2_encrypted.split(key))[1].split(key)[0])[::-1].upper()
        team1_score_points = 0
        team2_score_points = 0
        if goals_team_1 == goals_team_2:
            team1_score_points = 1
            team2_score_points = 1
        elif goals_team_1 > goals_team_2:
            team1_score_points = 3
        elif goals_team_2 > goals_team_1:
            team2_score_points = 3
     
        if team1 not in teams:
            teams[team1] = []
            teams[team1] += [team1_score_points, goals_team_1]
        else:
            a = teams[team1]
            a[0] += team1_score_points
            a[1] += goals_team_1
            teams[team1] = a
        if team2 not in teams.keys():
            teams[team2] = []
            teams[team2] += [team2_score_points, goals_team_2]
        else:
            a = teams[team2]
            a[0] += team2_score_points
            a[1] += goals_team_2
            teams[team2] = a
     
    place = 1
    print("League standings:")
    for key, value in sorted(sorted(teams.items(), key=lambda kv: kv[0]), key=lambda key_: key_[1][0], reverse=True):
        print(f"{place}. {key} {value[0]}")
        place += 1
     
    counter = 0
     
    print("Top 3 scored goals:")
    for key, value in sorted(sorted(teams.items(), key=lambda kv: kv[0]), key=lambda key_: key_[1][1], reverse=True):
        print(f"- {key} -> {value[1]}")
        counter += 1
        if counter == 3:
            break