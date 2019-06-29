#part 1

def countThe():
    infile = open("shakespeare.txt", 'r')
    frequencyList = []
    for word in ('the', 'The', 'THE'):
        frequencyList.append((wordList.count(word), word))
    return frequencyList







#part 2
def wordsStartThe():
    infile = open("shakespeare.txt", 'r')
    adict ={}
    words = open("2246.txt", 'r')
    wordstring = words.read()
    wordList = wordstring.split()
    for word in wordList:
        if word[:3] == 'the':
            if word in adict.keys():
                adict[word] += 1
            else:
                adict[word] = 1
    print(adict)
