from string import*

name = "Long Nam Tran"

def doubleLetter(string, index):
    return string[:index] + string[index] + string[index:]

def modWholeString(string):
    stringToMod = string
    index = 0
    for i in range (0, len(string)):
        stringToMod = doubleLetter(stringToMod, index)
        index += 2
        print(stringToMod)

modWholeString(name)

