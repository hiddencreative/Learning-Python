def isWordGuessed(secretWord, lettersGuessed):
    word=set(secretWord)
    guess = set(lettersGuessed)
    match = word & guess
    answer = word - match
    if len(answer) == 0:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    guess=set(lettersGuessed)
    answer=[]
    for i in range(len(secretWord)):
        if secretWord[i] in guess:
            answer.append(str(secretWord[i]))
        else:
            answer.append(str('_'))

    return ' '.join(answer)



def getAvailableLetters(lettersGuessed):
    import string
    guess=set(lettersGuessed)
    alpha=set(string.ascii_lowercase)
    lettersRemain=alpha-guess
    answer=list(lettersRemain)
    answer.sort()
    return ''.join(answer)



def hangman(secretWord):
    lettersGuessed=[]
    mistakesMade=0
    guessCounter=8
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ str(len(secretWord))+ ' letters long'
    print '-----------------------------------'
    while mistakesMade < 8:
        print 'You have ' + str(guessCounter-mistakesMade) + ' guesses left.'
        print 'Available Letters: ' + str(getAvailableLetters(lettersGuessed))
        letter=raw_input('Please guess a letter:' ).lower()
        if letter in ''.join(lettersGuessed):
            lettersGuessed.append(letter)
            mistakesMade=mistakesMade
            print "Oops! You've already guessed that letter: "+ str(getGuessedWord(secretWord, lettersGuessed))
            print '-----------------------------------'
        elif letter in secretWord:
            lettersGuessed.append(letter)
            mistakesMade=mistakesMade
            print 'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
            print '-----------------------------------'
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
                break
        else:
            mistakesMade +=1
            lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed))
            print '-----------------------------------'
    else:
        print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) +'.'
secretWord = 'blueberry'
