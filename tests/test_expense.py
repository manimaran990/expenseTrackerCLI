# File: test_expense.py
import unittest
from app.expense import Expense

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.expense = Expense('Rent', 'Housing', 500.0, 'USD', 'DB', '2022-01-01')

    def test_currency(self):
        self.assertEqual(self.expense.currency, 'USD')
        self.assertRaises(ValueError, setattr, self.expense, 'currency', 'EUR')

    def test_transaction(self):
        self.assertEqual(self.expense.transaction, 'DB')
        self.assertRaises(ValueError, setattr, self.expense, 'transaction', 'INVALID')

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            Expense('Rent', 'Housing', 500.0, 'EUR', 'DB', '2022-01-01')

    def test_invalid_transaction(self):
        with self.assertRaises(ValueError):
            Expense('Rent', 'Housing', 500.0, 'USD', 'INVALID', '2022-01-01')

if __name__ == '__main__':
    unittest.main()