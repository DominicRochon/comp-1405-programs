divNums = [2,3,4,5,6]

def isDivisibleBy(n, x):
    if n % x == 0:
        print(str(n) + " is divisible by " + str(x))
    else:
        print(str(n) + " is not divisible by " + str(x))

number = int(input("Enter an integer: "))
#number2 = int(input("Enter another integer: ")) we used this in part 3 of the program
for i in range(5):
    answer = isDivisibleBy(number, divNums[i])