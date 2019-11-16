secretWord = str(input("Enter Secret Word: "))
lettersGuessed = input("Enter Guessed Letter/s: ")

def isWordGuessed (secretWord, lettersGuessed):
    for letter in secretWord:
        ans = letter in lettersGuessed
        if ans == ("False"):
            break
        return ans
print (isWordGuessed(secretWord,lettersGuessed))