def gradeConvert(grade: float) -> str:
    if grade >= 80:
        grade = 'A'
    elif grade >= 70:
        grade = 'B'
    elif grade >= 60:
        grade = 'C'
    elif grade >= 50:
        grade = 'D'
    else:
        grade = 'F'

    return grade

def degreeConvert(degrees: float) -> float:
    degrees -= 30
    degrees /= 2
    return degrees

def currencyConvert(cads: float) -> float:
    cads *= 0.75
    return cads

def binaryConvert(num: int) -> int:
    num = bin(num)
    num = int(num[2:])
    return num

def sarcasmConvert(word: str):
    wordL = []
    wordL[:0] = word
    i = 0
    wordL.append(wordL[-1])

    while i < len(wordL):
        if i%3 == 1:
            wordL[i] = wordL[i].upper()
        else:
            wordL[i] = wordL[i].lower()
        i += 1

    seperator = ''
    return seperator.join(wordL)

name = input ("What's your name? ")
print('\nHi ' + name + ', welcome to the personal unit converter program!')
print('Please choose a conversion you would like to perform')
print('1 - Percent to letter grade')
print('2 - Fahrenheit to celcius')
print('3 - Canadian dollar to American')
print('4 - Decimal to binary')
print('5 - Convert to sarcasm')

choice = input ('Choice: ')
print('\n')

if choice == '1':
    grade = float(input ('Enter your grade: '))
    letterGrade = gradeConvert(grade)
    print (str(grade) + "% = " + letterGrade)

if choice == '2':
    degreesF = float(input ('Enter degrees in fahrenheit: '))
    degreesC = degreeConvert(degreesF)
    print (str(degreesF) + " degrees fahrenheit = " + str(degreesC) + " degrees celcius")

if choice == '3':
    cads = float(input ('Enter amount of money in CAD: '))
    amerDollars = currencyConvert(cads)
    print (str(cads) + " CAD is equivalent to " + str(amerDollars) + " US dollars")

if choice == '4':
    number = int(input ('Enter an integer: '))
    binNum = binaryConvert(number)
    print (number + " in binary is " + str(binNum))

if choice == '5':
    word = input('Enter a word: ')
    wordSarcasm = sarcasmConvert(word)
    print (word + " said sarcastically is " + wordSarcasm)


print ('\nBye ' + name)