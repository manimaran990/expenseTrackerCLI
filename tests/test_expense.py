import unittest
from app.expense import Expense

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.expense = Expense('2022-01-01', 'Test', 100.00, 'USD', 'debit')

    def test_currency(self):
        self.assertEqual(self.expense.currency, 'USD')
        self.assertRaises(ValueError, setattr, self.expense, 'currency', 'EUR')

    def test_transaction(self):
        self.assertEqual(self.expense.transaction, 'debit')
        self.assertRaises(ValueError, setattr, self.expense, 'transaction', 'INVALID')

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            Expense('2022-01-01', 'Test', 100.00, 'EUR', 'debit')

    def test_invalid_transaction(self):
        with self.assertRaises(ValueError):
            Expense('2022-01-01', 'Test', 100.00, 'USD', 'invalid')

    def test_get_dict(self):
        expected_dict = {
            'name': 'Test',
            'amount': 100.00,
            'debit': 100.00,
            'credit': '',
            'transaction': 'debit',
            'date': '2022-01-01'
        }
        self.assertEqual(self.expense.get_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()