n = int(input("Enter a number: "))

while(n > 1):
    for p in range(4):
        if p == 0:
            for x in range(n+1):
                for y in range(x): 
                    print('Q', end = '')
                print('\n', end = '') 
            print('-'*n, end = '')
        elif p == 1:
            for x in range(n+1):
                print(' '*(n-x), end = '')
                for y in range(x): 
                    print('Q', end = '')
                print('\n', end = '') 
            print('-'*n)
        elif p == 2:
            for x in range(n):
                for y in range(n-x): 
                    print('Q', end = '')
                print('\n', end = '') 
            print('-'*n)
        elif p == 3:
            for x in range(n):
                print(' '*x, end = '')
                for y in range(n-x): 
                    print('Q', end = '')
                print('\n', end = '') 
            print('-'*n)

    n = int(input("Enter a number: "))

    
print("goodbye")