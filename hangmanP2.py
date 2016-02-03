def getGuessedWord(secretWord, lettersGuessed):
    guess = set(lettersGuessed)
    answer=[]
    for i in range(len(secretWord)):
        if secretWord[i] in guess:
            answer.append(str(secretWord[i]))
        else:
            answer.append(str('_'))
    return ' '.join(answer)