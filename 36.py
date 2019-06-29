from string import*

def decipherCharacter(char, keyChar):
    offset = ord(keyChar) - ord('A')
    charCode = ord(char)
    newCharCode = charCode - offset
    if newCharCode < ord('A'):
        newCharCode = newCharCode + numberOfLettersInAlphabet
    newChar = chr(newCharCode)
    return newChar

def filterLettersPass(aString):
    newString = ""
    for ch in aString:
        if ch in ascii_letters:
            newString = newString + ch
    return newString


def decipher(key):
    messageToDecipher = "YLA TYDNXV FKL TIUZIJ MV WUK UG KNMO FPDJ LAX EUNFTAEFS HM M JKSV XEETPCZ. POWD XIILJ"
    key = filterLettersPass(key)
    key = key.upper()
    upcaseMessageToDecipher = messageToDecipher.upper()

    decipheredMessage = ""
    for index in range(len(upcaseMessageToDecipher)):
        char = upcaseMessageToDecipher[index]
        keyChar = key[index % len(key)]
        if char in ascii_uppercase:
            newChar = decipherCharacter(char, keyChar)
        else:
            newChar = char
        decipheredMessage = decipheredMessage + newChar
    print(decipheredMessage)


numberOfLettersInAlphabet = 26

decipher("THE HARVARD OF THE MIDWEST")
