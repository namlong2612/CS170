def write():
    outfile = open("asg43.txt", 'w')
    for number in range (1, 100 +1):
        outfile.write(str(number) + ' ' + 'I WILL NOT TEXT AND DRIVE' + '\n' )
    outfile.close()
