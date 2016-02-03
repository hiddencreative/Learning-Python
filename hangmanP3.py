def getAvailableLetters(lettersGuessed):
    import string
    guess = set(lettersGuessed)
    alpha = set(string.ascii_lowercase)
    lettersRemain = alpha - guess
    answer = list(lettersRemain)
    answer.sort()
    return ''.join(answer)