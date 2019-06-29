#precondition: month <12, numberOfDays <32, startDay<7


def printMonth(month, year, numberOfDays, startDay):
    year = str(year)

    dateRow = ""
    dayRow = " S  M  T  W  T  F  S"
    yearRow = int((len(dayRow) - len(year))/2)*" " + year
    monthRow = int((len(dayRow) - len(month))/2)*" " + month

    dateRow = startDay * "   "
    print(yearRow)
    print(monthRow)
    print(dayRow)
    for day in range(1, numberOfDays + 1): 
        if (day < 10):    
            dateRow += " "
            dateRow += str(day)
        else:
            dateRow += str(day)
        dateRow += " "
        if ((day + startDay) % 7 == 0 ):
            dateRow += "\n"
            print(dateRow)
            dateRow = ""
        if (day == numberOfDays):
            print(dateRow)
