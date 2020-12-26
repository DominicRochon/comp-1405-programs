def draw(n):
    for x in range(n+1):
        for y in range(x): 
            print(x, end = '')
        print('\n', end = '' )   

drawAnother = 'y'

while drawAnother == 'y':
    goodInput = False
    n = int(input ("Please enter an integer between 1 and 9: "))

    while not goodInput:
        if  0 < n < 10:
            goodInput = True 
        else:
            n = int(input ("Must be between 1 and 9 inclusive: "))

    draw(n)

    drawAnother = input("Would you like to draw another triangle? (y/n) ")

print ("Bye"),k