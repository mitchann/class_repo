import random

def randomLoan():
    loanOne = round(random.randint(500, 2000), -1)
    randomTerm = random.randint(36, 72)
    return loanOne, randomTerm
    
loanAmount, loanTime = randomLoan()
loanAmountTwo, loanTimeTwo = randomLoan()
loanAmountThree, loanTimeThree = randomLoan()

print (f"Loan 1 - Loan:{loanAmount} Time: {loanTime} months.")
print (f"Loan 2 - Loan:{loanAmountTwo} Time: {loanTimeTwo} months.")
print (f"Loan 3 - Loan:{loanAmountThree} Time: {loanTimeThree} months.")

userOption = int(input("Select a loan option: "))

try:
    if userOption != 1 or userOption != 2 or userOption != 3:
        raise ValueError()
except ValueError:
    print ("Invalid choice")
    exit()

if userOption == 1:
    userTotal = (loanAmount * loanTime) 
    print(f"This loan costs {userTotal}.\n")
if userOption == 2:
    userTotal = (loanAmountTwo * loanTimeTwo)
    print(f"This loan costs {userTotal}.\n")
if userOption == 3:
    userTotal = (loanAmountThree * loanTimeThree)
    print(f"This loan costs {userTotal}.\n")
    
costOne = loanAmount * loanTime
costTwo = loanAmountTwo * loanTimeTwo
costThree = loanAmountThree * loanTimeThree
    
lowest_cost = min(costOne, costTwo, costThree)
    
if userTotal == lowest_cost:
    print("You chose the cheapest option!") 
