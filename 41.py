words = open("words.txt",'r')
wordstring = words.read()
wordList = wordstring.split()


## 1. How many 14-letter words are there?
def wordsWith14Letters():
    count = 0
    for word in wordList:
        if len(word) == 14:
            count +=1
    print("There are", count, "14-letter words")



##2. Print all the words which contain ‘fj’
def wordsContainFJ():
    for word in wordList:
        if 'fj' in word:
            print (word)



##3. Print all the words that contain both ‘f’ and ‘j’.
def wordsContainFandJ():
    for word in wordList:
        if ('j' in word) and ('f' in word):
            print (word)



##4. Which words contain at least five ‘e’s?
def wordsContainFiveE():
    for word in wordList:
        numberOfe = 0
        for char in word:
            if char == 'e':
                numberOfe +=1
            if numberOfe >= 5:
                print (word)



##5. What words contain all the vowels a, e, i, o, and u?
def wordsContainVowels():
    for word in wordList:
        if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
            print(word)



## 6.
def wordGame(givenWord):
    wordDict = {}
    for char in givenWord:
        wordDict[char] = 0

    letterList = list(wordDict.keys())

    for char in givenWord:
        if char in letterList:
            wordDict[char] += 1

    return wordDict

letterTracker = wordGame('nominal')
letterList = list(letterTracker.keys())

for word in wordList:
    newLetterTracker = letterTracker.copy()
    wordLength = len(word)
    for char in word:
        if char in letterList:
            if newLetterTracker[char] > 0:
                newLetterTracker[char] -= 1
                wordLength -= 1
        else:
            break
    if wordLength == 0:
        print(word)




