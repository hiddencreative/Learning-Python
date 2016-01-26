balance = 320000
annualInterestRate = 0.2


monthlyInterestRate = annualInterestRate/12
low = balance/12.0
high = (balance*((1+monthlyInterestRate)**12))/12.0
minimumPay = 0
newBalance = balance

while balance > 0.02 or balance < -0.02:
    balance = newBalance
    minimumPay = (low + high)/2
    for x in range(0,12):
        monthlyUnpaid = balance - minimumPay
        balance = round(monthlyUnpaid + monthlyInterestRate*monthlyUnpaid,2)
    if balance > 0:
        low = minimumPay
    if balance < 0:
        high = minimumPay

print "Lowest Payment: "+str(round(minimumPay,2))