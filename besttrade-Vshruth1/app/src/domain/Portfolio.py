'''
Create a Portfolio class that mimics the portfolio object
'''

class Portfolio():
    def __init__(self, account_id: int, ticker: str, quantity: int ,id:int=-1):
        self.account_id = account_id
        self.ticker = ticker
        self.quantity = quantity
        self.id = id
    
    def __str__(self):
        return f'[id:{self.id},account_id:{self.account_id}, ticker:{self.balance}, quantity:{self.quantity}]'
        