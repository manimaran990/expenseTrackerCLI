import unittest
from app.filehandler import FileHandler
import os
import csv

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.filehandler = FileHandler('data/cibc.csv')

    def test_read_csv(self):
        self.filehandler.read_csv()
        data = self.filehandler.get_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_write_csv(self):
        data = [{'date': '2022-01-01', 'tr_name': 'Test', 'debit': 100, 'credit': 0, 'card_number': '1234'}]
        self.filehandler.write_csv(data, ['date', 'tr_name', 'debit', 'credit', 'card_number'])
        self.assertTrue(os.path.exists(self.filehandler._FileHandler__output_file))
        with open(self.filehandler._FileHandler__output_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            self.assertGreater(len(data), 0)

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()