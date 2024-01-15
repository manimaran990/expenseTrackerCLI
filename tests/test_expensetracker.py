import unittest
from app.expensetracker import ExpenseTracker
from app.expense import Expense
from app.filehandler import FileHandler
import pandas as pd
import os

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.filename = 'data/test.csv'
        self.filter_columns = ['date', 'tr_name', 'debit', 'credit', 'card_number']
        self.expense_tracker = ExpenseTracker(self.filename, self.filter_columns)

    def test_add_expense(self):
        expense = Expense('2022-01-01', 'Test', '100', '0', '1234')
        self.expense_tracker.add_expense(expense)
        self.assertEqual(len(self.expense_tracker.expense_data), 1)

    def test_process_data(self):
        expense = Expense('2022-01-01', 'Test', '100', '0', '1234')
        self.expense_tracker.add_expense(expense)
        df = self.expense_tracker.process_data(self.filter_columns)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)

    def tearDown(self):
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()