#Attempt at writing merge sort by memory!
#OMIGOD IT WORKED IM A COMPUTER GENIUS

def mergeSort(theList):
            
    if len(theList) == 1:
        return theList

    left = mergeSort(theList[:len(theList)//2])
    right = mergeSort(theList[len(theList)//2:])

    return merge(left,right)


def merge(list1, list2):
    newlist = []
    p = 0
    i = 0

    while i < len(list1) and p < len(list2):
        if list1[i] < list2[p]:
            newlist.append(list1[i])
            i += 1
        elif list1[i] > list2[p]:
            newlist.append(list2[p])
            p += 1
    
    if not len(list2[p:]) == 0:
        newlist.extend(list2[p:])
    elif not len(list1[i:]) == 0:
        newlist.extend(list1[i:])
    
    return newlist


meow = [7,6,5,3,9,1,2,10,4,8]
print(mergeSort(meow))