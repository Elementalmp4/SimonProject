file = open("leaderboard.txt")
data = file.read()
data = data.split("\n")

names = []
scores = []

for entry in data:
    temp = entry.split(",")
    names.append(temp[0])
    scores.append(temp[1])


print(names, scores)