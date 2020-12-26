month = input ('Which month? ')
valid = True
febMonth = False

if month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
    days = '31'
elif month == 'april' or month == 'june' or month == 'september' or month == 'november':
    days = '30'
elif month == 'february':
    febMonth = True
    curYear = input ('What year is it? ')
    if int(curYear) % 4 == 0:
        leapYr = 'y'
        if int(curYear) % 100 == 0 and int(curYear) % 400 != 0:
            leapYr = 'n'  
    else:
        leapYr = 'n'

    if leapYr == 'y':
        days = '29'
    else:
        days = '28'
else:
    valid = False

if febMonth:
    print (month + " has " + days + " days in " + str(curYear))
elif valid:
    print (month + " has " + days + " days")
else:
    print (month + " is not a valid input")