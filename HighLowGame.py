print'Please think of a number between 0 and 100!'
low = 0
high = 100
ans = (high + low) / 2
while True:
    print 'Is your secret number ',ans, '?'
    user_input = raw_input("Enter 'h' to indicate the guess is too high.  Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'h':
        high = ans
        ans = (high + low) / 2
    elif user_input == 'l':
        low = ans
        ans = (high + low) /2
    elif user_input == 'c':
        print 'Game over. Your secret number was: ',ans
        break
    else:
        print 'Sorry, I did not understand your input.'