
class AccountManage :
    def __init__(self):
        self.user_accountlist = []
        self.loanfeature = False
        self.total_bal = 20000000
        self.total_loan = 0
    def add_account( self, aob ) :
        self.user_accountlist.append( aob ) 
        print("           Account created Successfully           ")
    def show_useraccountlist ( self ) :
        print(" -------------   Show All Accounts  ---------------- ")
        print(" UserName ----- Account No ------ Email ----- Address ------- Account Type -------- Balance ----------- ")
        for i in self.user_accountlist :
            print(f"{i.name} ------- {i.account_no}  ------ { i.email } ------- { i.address } -------- { i.account_type } ------- { i.balance }")
        print(" --------------------------------------------------- ")
    def load_feature ( self ) :
        print(f" Loan Feature was { self.loanfeature } ")
        if self.loanfeature == False :
            self.loanfeature = True
        else :
            self.loanfeature = False
        print(f" Load Feature is { self.loanfeature } now  ")