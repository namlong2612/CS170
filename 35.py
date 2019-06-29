def translator(content):
    acc=""
    for ch in content:
        if ch == 'A':
            acc += '.-'
        if ch == 'B':
            acc += '-...'
        if ch == 'C':
            acc += '-.-.'
        if ch == 'D':
            acc += '-..'
        if ch == 'E':
            acc += '.'
        if ch == 'F':
            acc += '..-.'
        if ch =='G':
            acc += '--.'
        if ch == 'H':
            acc += '....'
        if ch == 'I':
            acc += '..'
        if ch == 'J':
            acc += '.---'
        if ch == 'K':
            acc += '-.-'
        if ch == 'L':
            acc += '.-..'
        if ch == 'M':
            acc += '--'
        if ch == 'N':
            acc += '-.'
        if ch == 'O':
            acc += '---'
        if ch == 'P':
            acc += '.--.'
        if ch == 'Q':
            acc += '--.-'
        if ch == 'R':
            acc += '.-.'
        if ch == 'S':
            acc += '...'
        if ch == 'T':
            acc += '-'
        if ch == 'U':
            acc += '..-'
        if ch == 'V':
            acc += '...-'
        if ch == 'W':
            acc += '.--'
        if ch == 'X':
            acc += '-..-'
        if ch == 'Y':
            acc += '-.--'
        if ch == 'Z':
            acc += '--..'
        if ch == '1':
            acc += '.----'
        if ch == '2':
            acc += '..---'
        if ch == '3':
            acc += '...--'
        if ch == '4':
            acc += '....-'
        if ch == '5':
            acc += '.....'
        if ch == '6':
            acc += '-....'
        if ch == '7':
            acc += '--...'
        if ch == '8':
            acc += '---..'
        if ch == '9':
            acc += '----.'
        if ch == '0':
            acc += '-----'
        if ch == '.':
            acc += '.-.-.-'
        if ch == ' ':
            acc += ' '
        acc += '   '
    return acc

content ='THE 1234 FOXES JUMP OVER 567890 THE LAZY DOGS.'
demo = translator(content)
print("The Morse Code translation of", content,"is", demo)
