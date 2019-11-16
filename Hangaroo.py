def isWordGuessed (secretWord, lettersGuessed):
    for letter in secretWord:
        ans = letter in lettersGuessed
        if ans == ("False"):
            return ans
    
def getGuessedWord(secretWord, lettersGuessed):
    S = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            S = S + letter
        else:
           S = S + '_ '
    return S

def getAvailableLetters(lettersGuessed):
    import string
    alpha = string.ascii_lowercase
    S = ''
    for letter in alpha:
        if letter not in lettersGuessed:
            S = S + letter
    return S

def Hangaroo():
    
    attempts = 3
    lettersGuessed =[]
    
    secretWord = input("Enter the secret word here: ")

    while attempts > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            return print('You are correct!')
        print('You only have ' + str(attempts) + ' attempts left.')
        print('The letters left are: ' + getAvailableLetters(lettersGuessed))
        
        gameInput = input('Guess a letter: ')
        gameInput = str(gameInput)
        gameInput = gameInput.lower()
        if gameInput not in lettersGuessed:
            lettersGuessed.append(gameInput)

            if gameInput in secretWord:
                print("Cool! " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Incorrect!: " + getGuessedWord(secretWord, lettersGuessed))
                attempts -= 1
        else:
            print("Hey! You already guessed that letter!: " + getGuessedWord(secretWord, lettersGuessed))

    return print("You lost! The secret word is " + str(secretWord))