


# Monthly interest rate = annualInterestRate / 12
# Minimum monthly payment = minimumMontlyPaymentRate * previousBalance
# Monthly unpaid balance = previousBalance - minimumMonthlyPayment
# Updated balance each month = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balance = 4213
minPayment = 0
month = 0
totalPaid = 0


while True:
    if month < 12:
        minPayment = monthlyPaymentRate * balance
        balance = balance - minPayment
        monthlyInterest = balance * (annualInterestRate / 12)
        balance = balance + monthlyInterest
        month += 1
        totalPaid = totalPaid + minPayment
        print 'Month: ',month
        print 'Minimum monthly payment: ',round(minPayment, 2)
        print 'Remaining balance: ',round(balance, 2)
        lowestPayment = balance / 12
        print 'Lowest Payment: ',lowestPayment
    else:
        print 'Total Paid: ', round(totalPaid, 2)
        print 'Remaining Balance: ', round(balance, 2)
        break