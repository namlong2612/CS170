# Assignment 40

#part 1
def countWord(matchWord):
    matchWord = matchWord.lower()
    lines = open("shakespeare.txt", 'r')
    count = 0
    for line in lines:
        line = line.split()
        for word in line:
            if word.lower() == matchWord:
                count += 1
    return count



#part 2
def wordsStartThe():
    
    words = open("shakespeare.txt", 'r')
    wordstring = words.read()
    wordList = wordstring.split()
    for word in wordList:
        if word[:3] == 'the':
            print(word)
            
