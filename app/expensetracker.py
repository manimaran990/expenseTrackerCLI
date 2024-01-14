# expensetracker
from expense import Expense
from filehandler import FileHandler
import pandas as pd

class ExpenseTracker:
    def __init__(self):
        self.expense_data = []

    def add_expense(self, expense: Expense):
        self.expense_data.append(expense)

    def view_by_date(self, date: str):
        pass

    def get_summary(self):
        pass

    def top_categories(self):
        pass