# expensetracker
from expense import Expense
from filehandler import FileHandler
import pandas as pd

class ExpenseTracker:
    def __init__(self, filename, filter_columns):
        self.__filehandler = FileHandler(filename)
        data_list = self.__filehandler.read_csv()
        self.expense_data = data_list if data_list is not None else None #read and append to list
        self.__proc_df = self.process_data(filter_columns)

    def add_expense(self, expense: Expense):
        self.expense_data.append(expense.get_dict())
        self.process_data(filter_columns)

    def process_data(self, filter_columns: list):
        df = pd.DataFrame(self.expense_data)
        df['amount'] = df.apply(lambda row: row['debit'] if row['debit'] != '' else row['credit'] if row['credit'] != '' else None, axis=1)
        df['transaction'] = df.apply(lambda row: 'debit' if row['debit'] != '' else 'credit' if row['credit'] != '' else None, axis=1)
        df = df[filter_columns]
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date', ascending=True)
        self.__proc_df = df
        return df
    
    def get_processed_data(self):
        return self.__proc_df

    def view_by_date(self, date: str):
        year, month = map(int, date.split('-'))
        return self.__proc_df[(self.__proc_df['date'].dt.year == year) & (self.__proc_df['date'].dt.month == month)]

    def get_summary(self):
        pass

    def top_categories(self):
        pass


filter_columns = ['date', 'name', 'amount', 'transaction']
et = ExpenseTracker("data/cibc.csv", filter_columns)
# print(et.get_processed_data())
# print(et.view_by_date('2024-01'))

# add new expense
expense = Expense('Rent', 2400.0, 'CAD', 'debit', '2022-01-01')
et.add_expense(expense)
print(et.get_processed_data())