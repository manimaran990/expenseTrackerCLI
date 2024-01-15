from datetime import datetime

class Expense:
    def __init__(self, date: str, name: str, amount: float, currency: str, transaction: str):
        self.__name = name
        self.__category = None
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
        if value is None or value.upper() not in ['CAD', 'INR', 'USD']:
            raise ValueError("currency should be 'CAD', 'INR', or 'USD'")
        self.__currency = value.strip().upper()

    @property
    def transaction(self):
        return self.__transaction
    
    @transaction.setter
    def transaction(self, value):
        if value is None or value.lower() not in ['credit', 'debit', 'cash']:
            raise ValueError("transaction should be in 'credit', 'debit' or 'cash'")
        self.__transaction = value.strip().lower()

    def get_dict(self):
        return {
            'name': self.__name,
            'amount': self.__amount,
            'debit': self.__amount if self.__transaction == 'debit' else '',
            'credit': self.__amount if self.__transaction == 'credit' else '',
            'transaction': self.__transaction,
            'date': self.__date
        }

        
    


