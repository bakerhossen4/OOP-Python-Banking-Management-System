
from user import User
from accountmanage import AccountManage
from action import Action
account_no = 1110000 # default
accob = AccountManage()

def cus_menu () :
    global account_no
    name = input("Enter Your Name : ")
    for i in accob.user_accountlist :
        if i.name == name :
            print(f" Hello {i.name} ")
            while True :
                print(".................................")
                print("          Customer Panel         ")
                print(" 2: Deposit Money ")
                print(" 3: Withdraw Money ")
                print(" 4: Available Balance ")
                print(" 5: View All Transaction History ")
                print(" 6: Take a Loan ( Max 2 times ) ")
                print(" 7: Transfer Money to Another Account No ")
                print(" 8: Back ")
                print("..................................")
                op = int(input("Enter Option : "))
                if op == 2 :
                    amount = int(input("Enter Amount to Deposit : "))
                    i.balance = i.balance + amount
                    accob.total_bal = accob.total_bal + amount
                    actionob = Action( "Deposit", amount )
                    i.transhistorylist.append(actionob)
                    print(f"{amount} TK Deposited. Current Balance : {i.balance}")
                elif op == 3 :
                    amount = int(input("Enter Amount to Withdraw : "))
                    if amount > i.balance :
                        print("Withdrawal amount exceeded")
                    else :
                        i.balance = i.balance - amount
                        accob.total_bal = accob.total_bal - amount
                        actionob = Action( "Withdraw", amount )
                        i.transhistorylist.append(actionob)
                        print(f"TK {amount} has withdrawn. Current Balance : {i.balance}")
                elif op == 4 :
                    print(f"Available Balance : {i.balance}") 
                elif op == 5 :
                    print(" -------------   My Transaction History  ---------------- ")
                    print(" Type ------- Balance  ")
                    for ab in i.transhistorylist :
                        print(f"{ab.trantype} ------- { ab.amount }")
                    print(" --------------------------------------------------- ")
                elif op == 6:
                    print(f"Your have taken {i.loantime} time Loan")
                    if i.loantime == 2 :
                        print("Sorry ! You are not eligible for loan.")
                    else :
                        if accob.loanfeature == True :
                            amountloan = int(input("Enter Loan Amount :"))
                            i.loantime = i.loantime + 1
                            i.balance = i.balance + amountloan
                            accob.total_bal = accob.total_bal - amountloan
                            accob.total_loan = accob.total_loan + amountloan
                            print(f"You have taken {amountloan} TK loan. Current Balance : {i.balance} ")
                        else :
                            print("Sorry ! Current Loan Feature is off.")
                elif op == 7:
                    nameacc = input("Enter Account Name to Transfer : ")
                    flag = False
                    for j in accob.user_accountlist :
                        if j.name == nameacc :
                            amnt = int(input("Enter Amount to Transfer : "))
                            j.balance = j.balance + amnt
                            i.balance = i.balance - amnt
                            actionob = Action( "Transfer", amnt )
                            i.transhistorylist.append(actionob)
                            flag = True
                            print(f"You have Transfered { amnt } TK to { nameacc }. Your Current Balance : {i.balance} ")
                    if flag == False :
                        print("Account does not exist")
                elif op == 8 :
                    break              

def admin_menu() :
    global account_no
    while True:
            print(".............................")
            print("          Admin Panel       ")
            print(" 1: Create an account ")
            print(" 2: Delete an user ")
            print(" 3: Show all User Accounts List ")
            print(" 4: Available Balance in Bank ")
            print(" 5: Total Loan Amount ")
            print(" 6: On/Off the Loan Feature ")
            print(" 7: Back")
            print(".............................")
            op = int(input("Enter Option : "))
            if op == 1:
                name = input("Enter Name : ")
                email = input("Enter Email : ")
                address = input("Enter Address : ")
                account_type = input("Enter Account Type(Savings/Current) [ Press S/C  ]: ")
                if account_type == "S" :
                     account_type = "Savings"
                else :
                     account_type = "Current"
                userob = User( name, email, address, account_type, account_no )
                accob.add_account( userob )
                account_no = account_no + 1
            elif op == 2:
                name = input("Enter Account Name : ")
                for a in accob.user_accountlist :
                    if a.name == name :
                        accob.user_accountlist.remove(a)
                        accob.total_bal = accob.total_bal - a.balance
                        print("Account Deleted Successfully ")
                        break
            elif op == 3 :
                accob.show_useraccountlist()
            elif op == 4: 
                print(f"Available Balance in Bank : {accob.total_bal}")
            elif op == 5 :
                print(f"Total Loan Amount from Bank : {accob.total_loan}")
                 
            elif op == 6 :
                 accob.load_feature( )
            elif op == 7 :
                 break
while True :
    print(".............................")
    print(" Bank Management System")
    print(" 1: Admin Panel ")
    print(" 2: Customer Panel ")
    print(" 3: Exit from System ")
    print(".............................")
    inputVal = int(input("Enter Input : "))
    if inputVal == 1:
        admin_menu()
    elif inputVal == 3:
        break
    elif inputVal == 2 :
         cus_menu()