
class User:
    def __init__(self, name, email, address, account_type, account_no):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_no = account_no
        self.loantime = 0
        self.transhistorylist = []
