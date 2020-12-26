'''
COMP 1405 - Fall 2020
Assignment #3

Name: Dominic Rochon
ID: 101195449
Comments: This is the portion with all my helper functions, also give me A+ pleas
'''

import math
import copy

#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
    return puzzle




#------------------------------------------------------------------#
#------------------------------------------------------------------#


# your functions go here!

'''
Puzzle to string function converts the puzzle to a string and returns that string in a neat grid
Number '0' is transformed into char ' '
Numbers above 9 get printed as letters (a = 10, b = 11, etc.)

Takes in 2-D matrix and outputs a string

For example, an input matrix of 0,3,2,1 is returned as     3 | 2 1
                                1,2,3,4                  1 2 | 3 4
                                2,4,1,3                  ----+----
                                3,1,4,2                  2 4 | 1 3
                                                         3 1 | 4 2
'''
def puzzle_to_string(puzzle):

    #Finding size of puzzle
    puzzleSize = len(puzzle)
    sqrtSize = int(math.sqrt(puzzleSize))

    strPuzzle = ''

    #I need to do a deepcopy here so that edited prints like printing '10' as the letter 'a' don't modify the original puzzle
    copyPuzzle = copy.deepcopy(puzzle)

    #k iterates over size of the puzzle
    for k in range(puzzleSize):

        #This creates the dashes, plus signs that make the table look so neat
        if k % sqrtSize == 0 and not k == (puzzleSize-1) and not k == 0:
            strPuzzle = strPuzzle + '-'*(2*sqrtSize) + '+'
            for p in range(sqrtSize-2):
                strPuzzle = strPuzzle + '-'*((2*sqrtSize)+1) + '+'
            strPuzzle = strPuzzle + '-'*(2*sqrtSize) + '\n'
            
        #i also iterates over size of puzzle, it also makes this loop nested
        for i in range(puzzleSize):
            #If statements that swap numbers for characters if needed
            if copyPuzzle[k][i] > 9:
                copyPuzzle[k][i] = chr(87 + copyPuzzle[k][i])
            if copyPuzzle[k][i] == 0:
                copyPuzzle[k][i] = ' '
            
            #Adding on what this round iterated to the string
            strPuzzle = strPuzzle + str(copyPuzzle[k][i]) + ' '

            #Adding slashes to make table look nice
            if (i+1) % sqrtSize == 0 and not i == (puzzleSize-1):
                strPuzzle = strPuzzle + '| '
        
        strPuzzle = strPuzzle + '\n'
        
    return strPuzzle

'''
I don't know if I should call this a 'helper function' for the functions check_rows, check_columns, and check_subgrids since
all of the work is happening under this function... I just figured those three functions were so similar I could condense their
contents into one neat function.

This funciton checks the validity of a row/col/subgrid depending on what it's being asked to do

Takes in 2-D matrix and an int from 0 to 2 under the variable name "checkType"
If checkType = 0, it checks rows, if checkType = 1, it checks columns and if checkType = 2, it checks subgrids

The function outputs a list of ints, indicating which row/column/subgrid is problematic

For example, an input matrix of 2,3,0,1 with a checkType of 2 (checking subGrids) is returned as [1] since there are two 2's in the first subgrid
                                1,2,3,0
                                0,4,1,3
                                3,1,4,2
'''
def checker(puzzle, checkType):
    invalid = []
    puzzleSize = len(puzzle)
    sqrtSize = int(math.sqrt(puzzleSize))

    for k in range(puzzleSize):
        numHad = []
        for i in range(puzzleSize):
            #numHad is a list of bools that tells the program if it's already seen a number in a row/col/subgrid
            numHad.append(False)

        #Another nested for loop to iterate over the puzzle
        for i in range(puzzleSize):
            #giving definitions of rows and cols differently depending on what the user is checking
            if checkType == 0:
                row = k
                col = i
            #To check columns just reverse the variables you would use as rows/cols for rows
            elif checkType == 1:
                row = i
                col = k
            #It's a little more complicated for subgrids but it's still the same idea as what I did for columns
            elif checkType == 2:
                row = (i // sqrtSize) + (k // sqrtSize)*sqrtSize
                col = (k%sqrtSize)*sqrtSize + (i % sqrtSize)
            
            #The program checks if it's seen a number before (unless it's a 0 or a space)
            if not puzzle[row][col] == ' ' and not puzzle[row][col] == 0:
                if numHad[puzzle[row][col]-1] == True:
                    invalid.append(k+1)
                numHad[puzzle[row][col]-1] = True
    
    return invalid

'''
The three next functions just call the checker function while letting it know what has to be checked
It then returns what the checker function returned
'''
def check_rows(puzzle):
    return checker(puzzle,0)

def check_columns(puzzle):
    return checker(puzzle,1)

def check_subgrids(puzzle):
    return checker(puzzle,2)

'''
This function takes in a 2D matrix (puzzle) and then sees if the user has completed the game or not, then returns a corresponding bool
'''
def gameSolved(puzzle):
    emptySpaces = 0
    gameSolve = False

    #Nested loop to iterate over whole puzzle
    for i in range(len(puzzle)):
        for k in range(len(puzzle)):
            #Counting number of empty spaces
            if puzzle[i][k] == 0 or puzzle[i][k] == ' ':
                emptySpaces += 1
    #If the board doesn't break any rules and it has no empty spaces, the game is solved
    if legalBoard(puzzle) and emptySpaces == 0:
        gameSolve = True
        
    return gameSolve

'''
This function checks if the current board is legal, it takes in a 2-D list and returns a bool
Basically it just calls the three checking functions and see if any of them output anything that isn't a blank list
'''
def legalBoard(puzzle):
    legal = False
    if len(check_rows(puzzle)) == 0 and len(check_columns(puzzle)) == 0 and len(check_subgrids(puzzle)) == 0:
        legal = True

    return legal

'''
This function takes in a 2-D array, a row int, a col int, and a num int
It then checks if a hypothetical edit that the user wants to make results in a legal board or not
'''
def editPuzzle(puzzle, row, col, num):
    legalEdit = True

    #Deepcopy since we want to make a hypothetical puzzle, and not edit the actual puzzle
    testPuzzle = copy.deepcopy(puzzle)
    testPuzzle[row][col] = num

    #Checks if the puzzle would be legal given the suggested edits
    if legalBoard(testPuzzle):
        puzzle[row][col] = num
    else:
        legalEdit = False
        print('That is invalid')

    return legalEdit
        



#------------------------------------------------------------------#
#------------------------------------------------------------------#