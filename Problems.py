

balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 10
newBalance = balance - 10

while newBalance > 0:
    monthlyPayment += 10
    newBalance = balance
    month = 0

    while month < 12 and newBalance > 0:
        newBalance -= monthlyPayment
        interest = monthlyInterestRate * newBalance
        newBalance += interest
        month += 1
    newBalance = round(newBalance,2)
print 'Lowest Payment:', monthlyPayment
