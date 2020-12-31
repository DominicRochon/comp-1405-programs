#Attempt at quick sort without the help of the internet
#I cant tell if I did this correctly but I hope so

def quickSort(theList):

    if len(theList) < 2:
        return theList

    splitList = partition(theList)
    #splitList[0] is left, splitList[1] is right

    return quickSort(splitList[0]) + quickSort(splitList[1])

def partition(inList):

    pivot = len(inList) - 1
    i = 0

    while i < pivot:
        if inList[i] > inList[pivot]:
            inList.append(inList[i])
            inList.pop(i)
            pivot -= 1
        else:
            i += 1
    
    left = inList[:pivot]
    right = inList[pivot:]

    return [left,right]
    
#Driver code
meow = [7,6,5,3,9,1,2,10,4,8]
print(quickSort(meow))