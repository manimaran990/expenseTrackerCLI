# expensetracker
from expense import Expense
from filehandler import FileHandler
import pandas as pd
from categorizer import Categorizer
from tabulate import tabulate

class ExpenseTracker:
    def __init__(self, filename, filter_columns):
        self.__filehandler = FileHandler(filename)
        data_list = self.__filehandler.read_csv()
        self.expense_data = data_list if data_list is not None else None #read and append to list
        self.__proc_df = self.process_data(filter_columns)
        self.__summary_df = None

    def add_expense(self, expense: Expense):
        self.expense_data.append(expense.get_dict())
        self.process_data(filter_columns)

    def process_data(self, filter_columns: list):
        df = pd.DataFrame(self.expense_data)
        df['amount'] = df.apply(lambda row: float(row['debit']) if row['debit'] != '' else float(row['credit']) if row['credit'] != '' else None, axis=1)
        df['amount'] = df['amount'].astype(float)
        df['transaction'] = df.apply(lambda row: 'debit' if row['debit'] != '' else 'credit' if row['credit'] != '' else None, axis=1)
        df = df[filter_columns]
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date', ascending=True)
        
        categorizer = Categorizer()  # Create an instance of the Categorizer class
        df['category'] = df.apply(lambda row: categorizer.get_category(row['name']), axis=1)  # Add category column
        
        self.__proc_df = df
        return df

    def get_processed_data(self):
        return self.__proc_df

    def view_by_date(self, date: str):
        year, month = map(int, date.split('-'))
        return self.__proc_df[(self.__proc_df['date'].dt.year == year) & (self.__proc_df['date'].dt.month == month)]
    
    def get_summary(self):
        self.__summary_df = self.__proc_df.groupby('category').agg({'amount': ['count', 'sum']}).reset_index()
        self.__summary_df.columns = ['category', 'count', 'total_amount']
        return self.__summary_df

    def print_summary(self):
        print(f"{'Summary':=^50}")
        print()
        self.get_summary()
        print(tabulate(self.__summary_df, headers='keys', tablefmt='psql', showindex=False))


    def top_categories(self):
        print(f"{'Top Categories':=^50}")
        print()
        self.get_summary()
        sorted_df = self.__summary_df.sort_values(by='total_amount', ascending=False)
        print(tabulate(sorted_df, headers='keys', tablefmt='psql', showindex=False))


filter_columns = ['date', 'name', 'amount', 'transaction']
et = ExpenseTracker("data/cibc.csv", filter_columns)
et.print_summary()
# print(et.top_categories())
# print(et.get_processed_data())
# print(et.view_by_date('2024-01'))

# add new expense
# expense = Expense('2022-01-01', 'Test', 100.00, 'CAD', 'debit')
# et.add_expense(expense)
# print(et.get_processed_data())