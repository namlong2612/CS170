# guess-the-number game
# computer does the guessing

def main():
    curRange = range(101)
    while (True):
        curGuess = guess(curRange)
        print('guess: ',curGuess)
        case = input('l for too low, and h for too high, y for correct answer: ')
        if case == 'l':
            curRange = highBoundary(curRange)
        elif case == 'h':
            curRange = lowBoundary(curRange)
        elif case == 'y' :
            print ('the final answer is ',curGuess)
            break    
        

def guess(aRange):
    return (aRange[0] + aRange[-1]) //2

def lowBoundary(aRange):
    mid = len(aRange)//2
    return aRange[:mid]

def highBoundary(aRange):
    mid = len(aRange)//2
    return aRange[mid:]
    
