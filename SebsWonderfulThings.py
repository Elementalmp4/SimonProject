import os

#Seb's wonderful things - A collection of somewhat handy functions that do stuff

def clear():
    if (os.name == "nt"):
        command = "cls"
    else:
        command = "clear"
        
    clear = lambda: os.system(command)
    clear()

def displayGraphicFromFile(graphicName):
    try:
        with open("graphics/" + graphicName + ".txt") as graphicsFile:
            graphicData = graphicsFile.read()
            print(graphicData)
    except:
        print("Graphics File Missing")