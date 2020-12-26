import copy

def bucket_Sort(numberListOriginal):
    numberList = copy.deepcopy(numberListOriginal)
    buckets = []
    bucketBrackets = []
    numOfBuckets = len(numberList)
                  
    #Append empty buckets
    for i in range(numOfBuckets):
        bucketBrackets.append((i+1)/numOfBuckets)
        buckets.append([])
        
    #Fill da buckets
    for p in numberList: 
        slot = findBracket(p, bucketBrackets)
        buckets[slot].append(p)
       
    for i in range(numOfBuckets): 
        buckets[i] = insertion(buckets[i]) 
        
    k = 0
    for i in range(numOfBuckets): 
        for j in range(len(buckets[i])): 
            numberList[k] = buckets[i][j] 
            k += 1
    return numberList 

def findBracket(val, bucketBrackets):
    #This is using linear search which isn't as fast as binary but it still keeps the O(n) runtime
    for i in range(len(bucketBrackets)):
        if val < bucketBrackets[i]:
            return i

def insertion(aBucket):
    for i in range (1, len (aBucket)):
        var = aBucket[i]
        num = i - 1
        while (num >= 0 and var < aBucket[num]):
            aBucket[num + 1] = aBucket[num]
            num -= 1
        aBucket[num + 1] = var
    
    return aBucket

x = [0.897, 0.565, 0.676, 
     0.1234, 0.665]
print("Sorted Array is") 
print(bucket_Sort(x)) 
print(x)