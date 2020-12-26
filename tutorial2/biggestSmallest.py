def smallest (a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

def biggest (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def middle (a, b, c, large, small):
    if (large == a or small == a) and (large == c or small == c):
        return b
    elif (large == b or small == b) and (large == a or small == a):
        return c
    else:
        return a

intA = int(input ('Enter an integer: '))
intB = int(input ('Enter another integer: '))
intC = int(input ('Enter another integer: '))
small = smallest(intA, intB, intC)
large = biggest(intA, intB, intC)
mid = middle(intA, intB, intC, large, small)

print (str(small) + ' is the smallest')
print (str(large) + ' is the largest')
print (str(mid) + ' is in between')