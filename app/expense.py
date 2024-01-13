from datetime import datetime

class Expense:
    def __init__(self, name: str, category: str, amount: float, currency: str, transaction: str, date: str):
        self.__name = name
        self.__category = category
        self.__amount = amount
        self.__currency = None
        self.__transaction = None
        self.__date = date

        self.currency = currency
        self.transaction = transaction

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if value.upper() not in ['CAD', 'INR', 'USD']:
            raise ValueError("currency should be 'CAD', 'INR', or 'USD'")
        self.__currency = value.strip().upper()

    @property
    def transaction(self):
        return self.__transaction
    
    @transaction.setter
    def transaction(self, value):
        if value.upper() not in ['CR', 'DB', 'CASH']:
            raise ValueError("transaction should be in 'CR', 'DB' or 'CASH'")
        self.__transaction = value.strip().upper()

        
    


