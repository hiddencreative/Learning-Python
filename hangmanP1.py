def isWordGuessed(secretWord, lettersGuessed):
    word = set(secretWord)
    guess = set(lettersGuessed)
    match = word and guess
    answer = word - match
    if len(answer) == 0:
        return True
    else:
        return False