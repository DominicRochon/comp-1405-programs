# crypto.py
# --------------
# COMP1405A - Fall2020

## Student: Dominic Rochon  
## ID: 101195449
## Comments: Gibe me A+ pls
##
##
##
##



def decrypt(ciphertext: str, shift: int, alphabet: str) -> str:
    '''Decrypts the given ciphertext using the shift cipher with the provided shift and alphabet.
      
       pre-condition: alphabet has no repeated characters in it
    '''
    
    size = len(alphabet)
    
    # Create a look up table for decryption using a dictionary 
    # (we'll learn about them later!)
    # Each letter will be mapped to its position in the alphabet list
    lookUp = dict()  # empty dictionary
    for index in range(size):
        lookUp[alphabet[index]] = index

    # decrypt the message character by character 
    # storing the resulting characters in a list
    # use list cmprehension to create this list
    # (we'll learn about that later!)
    plaintext = [ alphabet[(lookUp[c]-shift) % size] for c in ciphertext]

    # join all the elements of the list together (and output result)
    return "".join(plaintext)


def encrypt (message, shift, alphabet):

    cryptMessage = ''

    for k in message:
        i = 0
        while i < len(alphabet):
            if k == alphabet[i]:
                laps = (shift+i)//len(alphabet)
                shift -= laps*len(alphabet)
                cryptMessage = cryptMessage + alphabet[i+shift]
            i+=1
    
    return cryptMessage

def passwordIsValid (passwd):

    anUpper = False
    aLower = False
    valid = True
    numDig = 0
    numSpecial = 0

    digit = '0123456789'
    specialChar = '!@#$%^_.'

    for k in passwd:
        for i in digit:
            if k == i:
                numDig += 1

    for k in passwd:
        for i in specialChar:
            if k == i:
                numSpecial += 1

    for k in passwd:
        if k.isupper():
            anUpper = True
        elif k.islower():
            aLower = True

    if len(passwd) < 5:
        valid = False
    elif numDig < 2:
        valid = False
    elif numSpecial < 1:
        valid = False
    elif not anUpper or not aLower:
        valid = False
    elif not passwd[0].isalpha() and not passwd[0] == '_':
        valid = False
    
    return valid

#These are things I used to test the different functions
#print(passwordIsValid('H22#lLO'))
#print(decrypt(encrypt('abcxyz', 2, "abcdefghijklmnopqrstuvwxyz"), 2, "abcdefghijklmnopqrstuvwxyz"))
