'''
Dominic Rochon DNA program
COMP1405A - Fall2020
ID: 101195449
I have all the needed functions in here... A+ pls :D
'''

def pair (strand):
    ''' Program checks the inputted letters and assigns matching pair

    a,A,t,T,c,C,g,G are the valid inputs, A goes with T, and C goes with G
    lowercase letters are automatically turned into upper case in their pair

    --- Expected input & output example ---

        strand = 'aCtGg'
        print(pair (strand))

        ...
        TGACC
        ...

    '''

    #Creates string so we can add to it later
    matchStrand = ''

    #Checking letters & assigning pair
    for i in strand:
        if i == 'a' or i == 'A':
            match = 'T'
        elif i == 't' or i == 'T':
            match = 'A'
        elif i == 'c' or i == 'C':
            match = 'G'
        elif i == 'g' or i == 'G':
            match = 'C'
        
        #Recreate matching strand 1 by 1 adding
        matchStrand = matchStrand + match
    
    return matchStrand

def compress (strand):

    ''' Program compresses a strand into a shorter form

    A,T,C,G are what the user is supposed to input, but the program would word with any character
    Program takes repeated letters and shortens it to a number and a letter (the number is how many of those letters there are)
    The program does not compress single letters (A does not become 1A)

    --- Expected input & output example ---

        strand = 'AACCCCTTGAA'
        print(compress (strand))

        ...
        2A4C2TG2A
        ...

    '''
    #Creating string so we can add to it later
    cStrand = ''
    i = 0
    #while loop runs through length of strand
    while i < len(strand):
        num = 1
        sameLetter = True
        while sameLetter: #While loop counts the number of times a certain letter has been repeated
            if not i + num == len(strand) and strand[i] == strand[i+num]:
                num += 1 #Num is the number of repitions of a number
            else:
                sameLetter = False
        
        #Adding to the string, attach a number if a letter is repeated more than once
        if num > 1:
            cStrand = cStrand + str(num) + strand[i] 
        else:
            cStrand = cStrand + strand[i]

        #i goes up by increments of num to prevent reading letters that have been already read
        i += num
    
    return cStrand

def expand(compressedStrand):

    ''' Program expands a strand into a longer form

    A user inputs a number, then a letter, and the program prints out that letter the number amount of times
    Valid inputs are numbers and the letters A,T,C,G although again, this program would work with any characters
    The program also checks if a number has more than one digit! That was the hardest part for me to do

    --- Expected input & output example ---

        strand = '10A2C4G'
        print(expand (strand))

        ...
        AAAAAAAAAACCGGGG
        ...

    '''

    eStrand = ''
    i = 0
    #looping through compressed strand
    while i < len(compressedStrand):
        num = 1
        letterHit = False
        if compressedStrand[i].isnumeric():
            while not letterHit: #This while loop is mainly here to check if the user put in a number longer than 1 digit
                if compressedStrand[i+num].isnumeric():
                    num += 1 #num is how many digits of numbers there are
                else:
                    letterHit = True
            num = int(compressedStrand[i:i+num]) #num changes to become the actual number before the letter
            eStrand = eStrand + compressedStrand[i+len(str(num))] * (num - 1)
        else:
            eStrand = eStrand + compressedStrand[i]

        i += len(str(num)) #i goes up by increments of the number of digits in num

    return eStrand

#Leftovers of what I used to test my programs
#print(expand("3AT12GA"))
#print (compress('AAATTGAA'))