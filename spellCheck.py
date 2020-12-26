'''
Dominic Rochon DNA program
COMP1405A - Fall2020
ID: 101195449

Spellcheck program does the stuff that is asked of me, woohoo!
'''

'''
This load_file function loads in files that are formatted like so:

Word1
Word2
Word3

It returns all the words it read in a list.
'''
def load_file(filename):
    elements = []
    try:
        #Reading the file
        with open(filename, "r") as f:
            for line in f:
                elements.append(line.strip())
    except:
        print('Unable to find ' + filename)
    return elements

'''
This load_file function loads in files that are formatted like this:

Word1,Word2,Word3 OR Word1 Word2 Word3, depending on wether variable 'a' is == "," or " "

It returns all the words it read in two lists
The first list (elements) is all the words read stripped of all periods
The second list (withPeriod) is the same as the first but with the inclusion of periods
'''
def load_split(filename, a):
    withPeriod = []
    elements = [] 
    try:
        with open(filename, "r") as f:
            for line in f:
                #Reading the file differently depending on the value of "a"
                if a == ',':
                    elements.append(line.replace(".", "").strip().split(a))
                elif a == ' ':
                    elements += line.replace(".", "").strip().split(a)
                    withPeriod += line.strip().split(a)
    except:
        print('Unable to find ' + filename)
    
    return elements, withPeriod

'''
This function both records new mistakes and also checks for mistakes, depending on wether the value of "check" is true or false.
I decided to have this one function do these two tasks because the required code and perameters for each are very similar.

When check is false, the program records a mistake by checking if the mistake has been made before.
If this mistake is new, it will append a new list to pastMistakes
If the mistake already exists in pastMistakes, the counter for the number of times that particular mistake is made increases by 1.
What the function returns is irrelevant to when "check" is false

When check is true, the program looks to see if the user has past mistakes that are related to the mispelt word.
The program returns all the past mistakes associated with the mispelt word in a list, which is sorted by most common mistakes to least.
'''
def recordMistake(wrongWord, rightWord, pastMistakes, check = False):
    possibleSuggestions = []
    mistakeAdded = False
    for i in pastMistakes:
        #Checking if the user has made the mistake before
        if i[0] == wrongWord:
            if check:
                #If check is true, append a suggested correct word to the list
                for q in range(len(i)//2):
                    possibleSuggestions.append([(i[1+(q*2)]), (i[2+(q*2)])])
            else:
                #Checking if the user has made the same correction to the wrong word, if so, increase the number of times that correction popped up by 1
                for k in range(len(i)):
                    if i[k] == rightWord:
                        num = int(i[k+1])
                        i[k+1] = str(num + 1)

                        mistakeAdded = True
                #Adding a new correction to the word if it has never been made
                if not mistakeAdded:
                    i.append(rightWord)
                    i.append('1')
                    mistakeAdded = True
    
    #If the program has never seen that wrong word, record the info accordingly
    if not mistakeAdded and not check:
        pastMistakes.append([wrongWord,rightWord,1])

    return (sorted(possibleSuggestions, key = lambda x: x[1], reverse = True))

'''
This function looks to see if any of the user's text aren't in the current list of correctWords.
It then returns all the mismatching words it found, as well as the location of those words.
'''
def spellCheck(inText, correctWords):
    matchFound = False
    spellingErrors = []
    errorLocations = []
    for i in range(len(inText)):
        matchFound = False
        for k in correctWords:
            if inText[i] == k:
                matchFound = True
        
        #Appending to list of errors where the word is not found in the list of correct words, as well as the location of that error
        if not matchFound:
            errorLocations.append(i)
            spellingErrors.append(inText[i])
    
    return [spellingErrors, errorLocations]

'''
This function writes current text to a file
It also re-formats lists of words into proper sentences with a new line for each
''' 
def saveText(outFile, periodText):
    f = open(outFile, "w")
    #Writing to file differently depending on wether or not the string ends with a period.
    for i in periodText:
        if i[-1] == '.':
            f.write(i + '\n')
        else:
            f.write(i + ' ')
    f.close()

'''
This function writes the user's past mistakes to a file as well as writing new correct words into another file.
They are also written on the file correctly formatted
''' 
def saveDictionary(outFile1, outFile2, myWords, pastMistakes):
    #Writing in mywords.txt
    f1 = open(outFile1, "w")
    for i in range(len(myWords)):
        f1.write(myWords[i] + '\n')
    f1.close()

    #Writing in mistakes.txt
    f2 = open(outFile2, 'w')
    for i in pastMistakes:
        for k in range(len(i)-1):
            f2.write(str(i[k]) + ',')
        f2.write(str(i[k+1]))
        f2.write('\n')
    f2.close()

#main function!
def main():
    correctWords = load_file('words.txt')
    myWords = load_file('mywords.txt')
    correctWords.extend(myWords)
    pastMistakes = load_split('mistakes.txt', ',')[0]

    exitProgram = False
    inText = []

    #Program loop
    while not exitProgram:
        inCommand = input('Enter command: ')

        #When user inputs "load"
        if inCommand[:4].lower() == 'load':
            #Takes in words normally, but also another list of words without periods removed
            loadedIn = load_split(inCommand[5:], ' ')
            inText = loadedIn[0]
            textWithPeriods = loadedIn[1]
        
        #When user inputs spell command
        if inCommand.lower() == 'spell':
            info = spellCheck(inText, correctWords)
            newWords = info[0]
            newWordsLoc = info[1]
            #iterating through all the wrong words
            for i in range(len(newWords)):
                suggestion = recordMistake(newWords[i], "", pastMistakes, True)
                if len(suggestion) < 1:
                    suggestion = '[No Suggestions]'
                print('Potential mistake: ' + newWords[i] + "\t" + str(suggestion))
                spellAction = input('Action: ')

                #If user presses enter without inputting anything
                if spellAction == '':
                    correctWords.append(newWords[i])
                    myWords.append(newWords[i])
                else:
                    #When user corrects a wrong word do appending + setting new values + accounting for periods
                    if textWithPeriods[newWordsLoc[i]][-1] == '.':
                        textWithPeriods[newWordsLoc[i]] = spellAction + '.'
                    else:
                        textWithPeriods[newWordsLoc[i]] = spellAction
                    inText[newWordsLoc[i]] = spellAction
                    recordMistake(newWords[i], spellAction, pastMistakes)
                    correctWords.append(spellAction)
                    myWords.append(spellAction)
        
        #When user inputs "save"
        if inCommand[:4].lower() == 'save':
            saveText(inCommand[5:], textWithPeriods)

        #When user wants to quit program
        if inCommand.lower() == 'quit':
            exitProgram = True
            saveDictionary('mywords.txt', 'mistakes.txt', myWords, pastMistakes)

if __name__ == "__main__":
    # execute only if run as a script
    main()