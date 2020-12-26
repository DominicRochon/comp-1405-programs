import sudoku

'''
COMP 1405 - Fall 2020
Assignment #3

Name: Dominic Rochon
ID: 101195449
Comments: Sudoku program with challenge implemented (loads in puzzles of any size)
For puzzles larger than 9x9 where the user needs to input a number above 9, they can do so, but it will show as a letter

For example: 10 --> 'a'
The user cannot input the letter 'a', only numbers are permitted

All of this is done of cource with the help of functions I imported from sudoku.py

Give me A+ plees? :D
'''
def main():
    totalEdits = 0
    badEdits = 0
    goodEdit = True
    inStr = ''

    #Loading file
    fileName = input('Please enter a file name: ')
    puzzle = sudoku.load_puzzle(fileName)
    
    #This goes so long as the game hasn't been solved and the user hasn't inputted "quit"
    while not inStr.lower() == 'quit' and not sudoku.gameSolved(puzzle):

        #Checks if edit user wants is allowed
        if goodEdit:
            print('\nYour puzzle: ')
            print(sudoku.puzzle_to_string(puzzle))
        else:
            badEdits += 1

        totalEdits += 1

        #Where the input happens
        if len(puzzle) > 9:
            print("You loaded in a board larger than 9x9, numbers inputted larger than nine will show as letters")
        inStr = input('Enter move row,col,number(quit to exit): ')

        #Slicing the input string into numbers to be used in a helper function
        if inStr[0].isnumeric():
            ins = inStr.split(',')
            goodEdit = sudoku.editPuzzle(puzzle,int(ins[0]),int(ins[1]),int(ins[2]))
    
    #Displays if the game was solved
    if sudoku.gameSolved(puzzle):
        print(sudoku.puzzle_to_string(puzzle))
        print('\nYou solved the puzzle!')
    #Displays if user quit the game
    else:
        #I need to decrement total edits by 1 since the program counts the input "quit" as an entered number
        totalEdits -= 1
        print('\nYou did not complete the puzzle')

    print ('You entered ' + str(totalEdits) + ' numbers in total')
    print ('You entered ' + str(badEdits) + ' invalid number(s)')
    


#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()