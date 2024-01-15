import unittest
from app.expense import Expense

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.expense = Expense('Rent', 500.0, 'USD', 'debit', '2022-01-01')

    def test_currency(self):
        self.assertEqual(self.expense.currency, 'USD')
        self.assertRaises(ValueError, setattr, self.expense, 'currency', 'EUR')

    def test_transaction(self):
        self.assertEqual(self.expense.transaction, 'debit')
        self.assertRaises(ValueError, setattr, self.expense, 'transaction', 'INVALID')

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            Expense('Rent', 500.0, 'EUR', 'debit', '2022-01-01')

    def test_invalid_transaction(self):
        with self.assertRaises(ValueError):
            Expense('Rent', 500.0, 'USD', 'invalid', '2022-01-01')

    def test_get_dict(self):
        expected_dict = {
            'name': 'Rent',
            'amount': 500.0,
            'debit': 500.0,
            'credit': '',
            'transaction': 'debit',
            'date': '2022-01-01'
        }
        self.assertEqual(self.expense.get_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()