secretWord = str(input("Enter the secret word: "))
lettersGuessed = input("Enter list of letters: ")

def getGuessedWord(secretWord, lettersGuessed):
    S = " "
    for letter in secretWord:
        if letter in lettersGuessed:
            S = S + letter
        else:
            S = S + "_ "
    return S
print (getGuessedWord(secretWord,lettersGuessed))