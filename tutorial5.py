def isRectangle(inList):
    lens = []
    for k in range(len(inList)):
        lens.append(len(inList[k]))
    
    for i in range(len(inList)):
        if not lens[0] == lens[i]:
            return False
    return True

def isNumericalHelper(inList):
    for i in inList:
        if i[0] == '-':
            i = i[1:]
        if not i.isdigit():
            return False
    return True

def isMatrix(inList):
    allNumerical = True
    for i in range(len(inList)):
        if(not isNumericalHelper(inList[i])):
            allNumerical = False
    if (isRectangle(inList) == True and allNumerical == True):
        return True
    else:
        return False

def printMatrix(inList):
    if(isMatrix(inList)):
        for i in range(len(inList)):
            print('|', end = ' ')
            for k in range(len(inList[0])):
                print(inList[i][k], end = ' ')
            print('|')
    else:
        print('Error')
        return []

def loadMatrix(fileName):
    matrix = []
    with open(fileName, 'r') as inFile:
        for line in inFile:
            line = line.strip()
            matrix.append( [val for val in line.split(",")] )
    return matrix

def main():
    #This is the main
    #print(isRectangle([[1,3],[4,2],[4,3,5]]))
    #print(isNumericalHelper(['-1.2','-3']))
    #print(isMatrix([['1', '2','5'], ['3', '4','1'], ['3', '4','1']])) #returns True
    #printMatrix([['1','4','5'],['2','4','3'],['2','4','a']])
    printMatrix(loadMatrix('thingy.csv'))

if (__name__ == "__main__"):
    main()