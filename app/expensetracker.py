# expensetracker
from expense import Expense
from filehandler import FileHandler
import pandas as pd

class ExpenseTracker:
    def __init__(self, filename: str = "data/cibc.csv"):
        self.__filehandler = FileHandler(filename)
        data_list = self.__filehandler.read_csv()
        self.expense_data = data_list if data_list is not None else None #read and append to list
        self.__proc_df = self.process_data()

    def add_expense(self, expense: Expense):
        self.expense_data.append(expense)

    def process_data(self):
        df = pd.DataFrame(self.expense_data)
        df['amount'] = df['debit'].combine_first(df['credit'])
        df['transaction'] = df.apply(lambda row: 'debit' if pd.notna(row['debit']) else 'credit' if pd.notna(row['credit']) else None, axis=1)
        return df[['date', 'tr_name', 'amount', 'transaction']]
    
    def get_processed_data(self):
        return self.__proc_df

    def view_by_date(self, date: str):
        return self.__proc_df[self.__proc_df['date'].str.contains(date)]

    def get_summary(self):
        pass

    def top_categories(self):
        pass


et = ExpenseTracker()
#print(et.get_processed_data())
print(et.view_by_date('2024-01'))