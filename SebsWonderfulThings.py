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

def color(colorName):

    colorMap = {
        "black": "\u001b[30m",
        "red": " \u001b[31m",
        "green": " \u001b[32m",
        "yellow": " \u001b[33m",
        "blue": " \u001b[34m",
        "magenta": " \u001b[35m",
        "cyan": " \u001b[36m",
        "white": " \u001b[37m",
        "reset": " \u001b[0m",
        "bright black": " \u001b[30;1m",
        "bright red": " \u001b[31;1m",
        "bright green": " \u001b[32;1m",
        "bright yellow": " \u001b[33;1m",
        "bright blue": " \u001b[34;1m",
        "bright magenta": " \u001b[35;1m",
        "bright cyan": " \u001b[36;1m",
        "bright white": " \u001b[37;1m",
        "background black": " \u001b[40m",
        "background red": " \u001b[41m",
        "background green": " \u001b[42m",
        "background yellow": " \u001b[43m",
        "background blue": " \u001b[44m",
        "background magenta": " \u001b[45m",
        "background cyan": " \u001b[46m",
        "background white": " \u001b[47m",
        "background bright black": " \u001b[40;1m",
        "background bright red": " \u001b[41;1m",
        "background bright green": " \u001b[42;1m",
        "background bright yellow": " \u001b[43;1m",
        "background bright blue": " \u001b[44;1m",
        "background bright magenta": " \u001b[45;1m",
        "background bright cyan": " \u001b[46;1m",
        "background bright white": " \u001b[47;1m"
    }

    if colorName in colorMap:
        colorCode = colorMap.get(colorName)
        print(colorCode)   


