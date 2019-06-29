
LENGTH = 4

def distance(wordA,wordB):
    if len(wordA)!=len(wordB):
        return 0
    count = 0
    for i in range(len(wordA)):
        if wordA[i] != wordB[i]:
            count +=1
    return count

def getAllWords():
    lines = open('words.txt','r')
    wordList =[]
    for line in lines:
        line = line.strip('\n')
        if len(line) == LENGTH:
            wordList.append(line)
    lines.close()
    return wordList

def problemA():
    wordList = getAllWords()
    wordList_sub = getAllWords()
    returnList = []
    for i in range(len(wordList)):
        for j in range(len(wordList)):
            if distance(wordList[i],wordList[j]) == 1:
                wordList_sub[i] = ''
                wordList_sub[j] = ''
    for word in wordList_sub:
        if word != '':
            returnList.append(word)
    return returnList
    
def problemB(sWord):
    wordList = getAllWords()
    wordList.remove(sWord)
    m = []
    nbWord = []
    for word in wordList:
        if distance(sWord,word) == 1:
            nbWord.append(word)
    for i in range(len(nbWord)):
        m.append(0)
    for i in range(len(nbWord)):
        for j in range(len(nbWord)):
            if distance(nbWord[i],nbWord[j]) == 1:
                m[j] = max(m[j],m[i]+1)
    return max(m)
    

def problemC():
    wordList = getAllWords()
    m =[]
    for i in range(len(wordList)):
        m.append(0)
    for i in range(len(wordList)):
        for j in range(len(wordList)):
            if distance(wordList[i],wordList[j]) == 1:
                m[j] = max(m[j],m[i] +1)
    return max(m)


