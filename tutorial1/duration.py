days = int(input ('How many days? '))
totalDays = days

years = days // 365
days -= years * 365

months = days // 30
days -= months * 30

weeks = days // 7
days -= weeks * 7

print (str(totalDays) + " days is " + str(years) + " years, " + str(months) + " months, " + str(weeks) + " weeks, " + str(days) + " days.")