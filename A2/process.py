# process.py
# --------------
# COMP1405A - Fall2020


## Student: Dominic Rochon
## ID: 101195449
## Comments: A++ for effort?
##
##
##
##



# Make sure the data.csv file is saved in the same directory as this file.
# If you are using VS Code, you must change the settings so that it can find 
# the file when it tries to open it.
# Go to Preferences -> Settings
#       Once in Settings, use the search bar to search for InFileDir
#       Check the box for  "Python -> Terminal : Execute In File Dir"



####
####  add your functions above the main method
####

def findByDomain(domain, data):
    k = 0
    outList = ['hi']
    while k < len(data):
        info = data[k].split(',')
        name = info[0]
        count = 0

        for i in info:
            if domain in i:
                count += 1
        
        outList.append(name + ':' + str(count))
        k += 1

    outList.pop(0)
    return outList

def emailsByAge(lower:int, upper:int, data):
    ages = ['']
    avgNums = [lower]
    k = 0
    while k < len(data):
        info = data[k].split(',')
        ages.append(info[1])
        ages.append(len(info) - 3)
        k += 1

    ages.pop(0)

    for i in range(lower, upper + 1):
        avgNum = 0.0
        for k in range(0,len(ages)-1,2):
            if ages[k] == str(i):
                avgNum += ages[k+1]
        avgNum /= len(data)
        avgNums.append(avgNum)

    return avgNums
        


# This function controls the program
def main():
    fname = 'data.csv'           # filename
    
    print("...opening file " + fname + " for reading")
    file = open(fname, 'r')      # open the file for reading

    print("...reading contents of file")
    data = file.readlines()      # read entire contents of file into list of strings
                                 # each line in the file is one string

    print("...closing file " + fname)
    file.close()                 # close the file now that we are done with it

    print("...data is...")
    for line in data:
        print(line, end='')

    ##
    ## data now has a list as needed for your functions.
    ##

    ## test your findByDomain() and emailsByAge() functions
    #users = findByDomain('carleton.ca', data)
    #print(users)
    #stats = emailsByAge(5,12,data)
    #print(stats)




###########################################################################
#
# Do NOT change the code below this
#
###########################################################################

# This if statement is needed so that when you "run" this program it will 
# automatically call the main function.
# If you load this function as a module it will not call main()
if __name__ == "__main__":
    main()