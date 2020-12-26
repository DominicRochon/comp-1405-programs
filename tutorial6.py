#tutorial 6
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'a':4, 'b':5, 'f':6}
dict3 = {'a':46, 'b':5, 'f':62, 'g':46, 't':2}

def display(dict1):
    for k in dict1.keys():
        print(k, "," , dict1[k])

def safeAdd(d, k, v, unsafe = False):
    if not k in d or unsafe:
        d[k] = v

def merge1(dict1,dict2):
    newDict = {}
    for i in dict1:
        newDict[i] = dict1[i]
    for k in dict2:
        newDict[k] = dict2[k]
    return newDict

def merge2(dict1,dict2):
    newDict = {}
    for i in dict1:
        if i in newDict:
            newDict[i].append(dict1[i])
        else:
            newDict[i] = [dict1[i]]
    for k in dict2:
        if k in newDict:
            newDict[k].append(dict2[k])
        else:
            newDict[k] = [dict2[k]]

    return newDict  

def top3(d):
    top3 = []
    for k in range(3):
        curTop = 0
        for i in d:
            if d.get(i) > curTop:
                curTop = d.get(i)
                topKey = i
                
        poppedKey = d.pop(topKey)
        top3.append([poppedKey, topKey])


    return top3


print(top3(dict3))dict3 = {'a':46, 'b':5, 'f':62, 'g':46, 't':2}

def display(dict1):
    for k in dict1.keys():
        print(k, "," , dict1[k])

def safeAdd(d, k, v, unsafe = False):
    if not k in d or unsafe:
        d[k] = v

def merge1(dict1,dict2):
    newDict = {}
    for i in dict1:
        newDict[i] = dict1[i]
    for k in dict2:
        newDict[k] = dict2[k]
    return newDict

def merge2(dict1,dict2):
    newDict = {}
    for i in dict1:
        if i in newDict:
            newDict[i].append(dict1[i])
        else:
            newDict[i] = [dict1[i]]
    for k in dict2:
        if k in newDict:
            newDict[k].append(dict2[k])
        else:
            newDict[k] = [dict2[k]]

    return newDict  

def top3(d):
    top3 = []
    for k in range(3):
        curTop = 0
        for i in d:
            if d.get(i) > curTop:
                curTop = d.get(i)
                topKey = i
                
        poppedKey = d.pop(topKey)
        top3.append([poppedKey, topKey])


    return top3


print(top3(dict3))dict3 = {'a':46, 'b':5, 'f':62, 'g':46, 't':2}

def display(dict1):
    for k in dict1.keys():
        print(k, "," , dict1[k])

def safeAdd(d, k, v, unsafe = False):
    if not k in d or unsafe:
        d[k] = v

def merge1(dict1,dict2):
    newDict = {}
    for i in dict1:
        newDict[i] = dict1[i]
    for k in dict2:
        newDict[k] = dict2[k]
    return newDict

def merge2(dict1,dict2):
    newDict = {}
    for i in dict1:
        if i in newDict:
            newDict[i].append(dict1[i])
        else:
            newDict[i] = [dict1[i]]
    for k in dict2:
        if k in newDict:
            newDict[k].append(dict2[k])
        else:
            newDict[k] = [dict2[k]]

    return newDict  

def top3(d):
    top3 = []
    for k in range(3):
        curTop = 0
        for i in d:
            if d.get(i) > curTop:
                curTop = d.get(i)
                topKey = i
                
        poppedKey = d.pop(topKey)
        top3.append([poppedKey, topKey])


    return top3


print(top3(dict3))dict3 = {'a':46, 'b':5, 'f':62, 'g':46, 't':2}

def display(dict1):
    for k in dict1.keys():
        print(k, "," , dict1[k])

def safeAdd(d, k, v, unsafe = False):
    if not k in d or unsafe:
        d[k] = v

def merge1(dict1,dict2):
    newDict = {}
    for i in dict1:
        newDict[i] = dict1[i]
    for k in dict2:
        newDict[k] = dict2[k]
    return newDict

def merge2(dict1,dict2):
    newDict = {}
    for i in dict1:
        if i in newDict:
            newDict[i].append(dict1[i])
        else:
            newDict[i] = [dict1[i]]
    for k in dict2:
        if k in newDict:
            newDict[k].append(dict2[k])
        else:
            newDict[k] = [dict2[k]]

    return newDict

def top3(d):
    top3 = []
    for k in range(3):
        curTop = 0
        for i in d:
            if d.get(i) > curTop:
                curTop = d.get(i)
                topKey = i
                
        poppedKey = d.pop(topKey)
        top3.append([poppedKey, topKey])


    return top3


print(top3(dict3))