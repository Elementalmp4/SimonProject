#Load imports
from SebsWonderfulThings import *   
from Leaderboard import *

#Display up to 10 top players
def showLeaderboard():
    names, scores = getLeaderboardData()
    sortedLeaderboard = sortLeaderboard(names, scores)
    clear()
    print("\033[1;31;40m")
    displayGraphicFromFile("leaderboard")
    print("\033[1;32;40m")
    for i in (range(0,len(sortedLeaderboard)), range(0,10))[len(sortedLeaderboard) >= 10]:
        score, name = sortedLeaderboard[i]
        nameAndScore = name + " - " + score
        print(str(i + 1) + ") " + nameAndScore)
    print("\033[1;33;40m")
    input("Press enter to return to the menu...")

#Game logic
def playGame(gameChoices, gameAnswers):
    clear()
    print("\033[1;31;40m")
    displayGraphicFromFile("guessTheColor")
    correctAnswers = 0
    rounds = len(gameAnswers)
    for roundNumber in range(0, rounds):
        choices = gameChoices[roundNumber]
        answer = gameAnswers[roundNumber]
        print("\033[1;32;40m\nYour colour choices are:\n")
        print(choices)
        userInputAnswer = input("\033[1;33;40mEnter the color you think it is: ")
        if (userInputAnswer == answer):
            correctAnswers += 1
    print("Out of " + str(rounds) + " rounds, you got " + str(correctAnswers) + " colors correct!")

    doLeaderboardChecks(userName, correctAnswers)

    input("Press enter to go back to the main menu!")
    
    mainMenu()

#Parse game files
def parseFile(data):
        choicesArray = []
        answersArray = []
        buffer = ""
        for item in data:
            if (item.startswith("-")):
                answer = item[1: len(item)]
                answersArray.append(answer)
                choicesArray.append(buffer)
                buffer = ""
            else:
                buffer += item + "\n"
        return choicesArray, answersArray

#Get game file data
def readGameData(dataFileName):
    try:
        with open(dataFileName + ".txt", "r") as file:
            fileRawData = file.read()
            filedata = fileRawData.split("\n")
            choices, answers = parseFile(filedata)
            playGame(choices, answers)    
            file.close()      
    except:
       print("A file handling error has occurred. Are all the game files in the right place?")

#Difficulty selector
def difficultyHandler(difficulty):
    if (difficulty == "t"):
        print("Tricky selected")
        readGameData("tricky")
    elif (difficulty == "n"):
        print("Normal selected")
        readGameData("normal")
    elif (difficulty == "s"):
        print("Simple selected")
        readGameData("simple")
    else:
        print("Invalid difficulty.")
        mainMenu()

#Main menu
def mainMenu():
    clear()
    print("\033[1;31;40m")
    displayGraphicFromFile("title")
    print("\033[1;32;40m")
    print("Option 1: Play Game")
    print("Option 2: View Leaderboard")
    print("\033[1;33;40m")
    option = input("Enter a menu option: ")

    #Play game option
    if (option == "1"):
        global userName
        userName = input("Welcome! What is your name?: ")
        if (userName == ""):
            mainMenu()
        difficulty = input("What difficulty would you like to play at? Tricky (T) Normal (N) or Simple (S): ").lower()
        difficultyHandler(difficulty)

    #Show leaderboard option
    elif (option == "2"):
        showLeaderboard()
        mainMenu()    
    else:
        mainMenu()
        
mainMenu()