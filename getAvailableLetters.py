lettersGuessed = input("Enter a list of letters: ")
def getAvailableLetters(lettersGuessed):
    import string
    Alpha = string.ascii_lowercase
    S = ''
    
    for letter in Alpha:
        if letter not in lettersGuessed:
            S = S + letter
    return S
print (getAvailableLetters(lettersGuessed))