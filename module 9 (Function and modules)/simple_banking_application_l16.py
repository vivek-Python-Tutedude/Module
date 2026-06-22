'''

banking application 
show balance, withdraw, deposite

'''

balance = 0.0

def check_balance(balance):
    print(f"Your balance is: {balance}")
    print("================================")

    
def deposite(d):
    global balance 
    if d > 0 :
        balance = balance + d
    else:
        print("You cannot deposite the zero or negative amount")
        print("================================")

    

def withdraw(w):
    global balance
    if(w < balance) :
     balance = balance - w
    else :
        print("Your withdraw amount {w} is greater than Your balance {balance}")
        print("================================")




print("Welcome to vivek's Bank!!!")


while True:
    print("1] Check your balance : ")
    print("2] Deposite an amount : ")
    print("3] withdraw an amount : ")
    print("4] quite")
    print("================================")
    
    choice = input("Enter the choice (1 - 4): ")
    print("================================")

    if choice == '1' :
        check_balance(balance)
    
    elif choice == '2' :
        d = float(input("Enter the amount to be deposit : "))
        deposite(d)
        print(f"Your {d} Rs is Deposited in Your account. ")
        print("================================")

        
    elif choice == '3' :
        w = float(input("Enter the amount to be Withdrwal : "))
        withdraw(w)
        print(f"Your {w} Rs is withdraw in Your account. ")
        print("================================")
 
        
    elif choice == '4' :
        break;
    else :
        print("Invalid choice!!! Re-try")
        print("================================")

        
print(f"Your balance is :{balance} ")
print("Thank you for banking with us!")