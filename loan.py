loanAmount = input("What is the total loan amount?\n")
monthlyPay = input("What is the montly payment amount?\n")
loan = int(loanAmount)
pay = int(monthlyPay)
monthTotal = (loan//pay)
print (f"It'll take {monthTotal} months to pay the loan.")