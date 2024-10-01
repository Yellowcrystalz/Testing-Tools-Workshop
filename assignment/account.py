class Account:
    def __init__(self, id: str, balance: int):
        self.id = id
        self.balance = balance
    
    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Cannot deposit a negative amount")

        self.balance += amount

    def withdrawl(self, amount: int):
        if amount <= 0:
            raise ValueError("Cannot withdrawl a negative amount")
        elif amount > self.balance:
            raise ValueError("Insuffecient funds")

        self.balance -= amount
    
    def get_balance(self):
        return self.balance