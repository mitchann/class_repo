loanAmount = input("What is the total loan amount?\n")
monthlyPay = input("What is the montly payment amount?\n")
noOfMonths = input("How many months will it take?\n")
   
try:
    loan = float(loanAmount)
    pay = float(monthlyPay)
    months = float(noOfMonths)
    if loan < 0 or pay < 0 or months < 0:
        exit() 
except: 
    print("Invalid input.")
    exit()

loan = float(loanAmount)
pay = float(monthlyPay)
months = float(noOfMonths)

if months < (loan/pay):
    print("Loan will not be paid in time.\n")
    print(f"Months: {loan/pay}")
else:
    print("Loan will be paid in time.\n")
    print(f"Months: {loan/pay}")
 