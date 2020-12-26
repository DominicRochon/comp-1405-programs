def factorialWhile(n):
    k = n
    while(n>1):
        k *= n-1
        n-=1
    
    return k



def factorialFor(n):
    k = 1
    for x in range(1, n+1):
        k *= x
    
    return k

def numberOfVowels(word):
    n = 0
    for x in range(len(word)):
        if (word[x] =='a' or word[x] =='e' or word[x] =='i' or word[x] =='o' or word[x] =='u' or word[x] =='A' or word[x] =='E' or word[x] =='I' or word[x] =='O' or word[x] =='U'):
            n += 1
    
    return n

print(numberOfVowels("Uppercase"))