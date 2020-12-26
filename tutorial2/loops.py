def countingUp(start, stop):
    counter = start 
    while (counter <= stop):
        print(counter)
        counter += 1

def countingDown  (start, stop):
    counter = start
    while (counter >= stop):
        print(counter)
        counter -= 1

startNum = int(input("starting number: "))
stopNum = int(input("stopping number: "))

if startNum < stopNum:
    countingUp(startNum, stopNum)
else:
    countingDown(startNum, stopNum)