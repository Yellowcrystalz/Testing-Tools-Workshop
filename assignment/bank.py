from account import Account

class Bank():
    def __init__(self):
        self.accounts_list = {}
    
    def create_account(self, id: str):
        if id in self.accounts_list:
            raise ValueError("That account ID already exists!")
            
        account = Account(id, 0)
        self.accounts_list[id] = account
    
    def get_account(self, id):
        if id not in self.accounts_list:
            raise ValueError("That account ID does not exist!")

        return self.accounts_list[id]