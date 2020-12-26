#This is the vowel tutorial exercize that we are doing together :)

def vowelCheck(x):
    if (x == 'a' or x == 'e' or x == 'i' or x =='o' or x=='u'):
        return 1
    elif x == 'y':
        return 2
    else:
        return 0

letter = input("Enter a letter: ")
isVowel = vowelCheck(letter)

if isVowel == 1:
    print (letter + " is a vowel")
elif isVowel == 2:
    print (letter + ' is sometimes a vowel')
else:
    print (letter + " is not a vowel")