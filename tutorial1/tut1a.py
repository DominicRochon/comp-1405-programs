#  tutorial 1 Sample file turned into age calculation program

name = input("what is your name? ")
birthYear = int(input("what year were you born? "))
currYear = int(input("what is the current year? "))

print(name + " must be " + str(currYear - birthYear - 1) + " or " + str(currYear - birthYear) + " years old")
