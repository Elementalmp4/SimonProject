#Seb's wonderful leaderboard system
#Modularised because it could be useful one day...

def sortLeaderboard(names, scores):
    nameScorePairs = list(zip(scores, names))
    sortedScoresAndNames = sorted(nameScorePairs)
    return sortedScoresAndNames

def writeLeaderboard(names, scores):
    payload = ""
    for i in range(0, len(names)):
        payload += names[i] + "," + str(scores[i]) + "\n"
    
    with open("leaderboard.txt", "w") as file:
        file.write(payload)

def getLeaderboardData():
    with open("leaderboard.txt") as file:
        data = file.read()
        data = data.split("\n")
        names = []
        scores = []

        for entry in data:
            if entry != "":
                temp = entry.split(",")
                names.append(temp[0])
                scores.append(temp[1])
    
    return names, scores

def doLeaderboardChecks(name, score):
    names, scores = getLeaderboardData()

    if name in names:
        index = names.index(name)
        score = score + int(scores[index])
        scores[index] = str(score)
        print("\nYour leaderboard score has been updated!\n")
    else:
        names.append(name)
        scores.append(score)
        print("\nYou have been added to the leaderboard!\n")
    
    writeLeaderboard(names, scores)

#That special day is coming i can feel it...