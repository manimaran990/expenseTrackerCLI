import unittest
from app.categorizer import Categorizer

class TestCategorizer(unittest.TestCase):
    def setUp(self):
        self.categorizer = Categorizer()

    def test_get_category_existing(self):
        category = self.categorizer.get_category('parantha')
        self.assertEqual(category, 'food')

    def test_get_category_non_existing(self):
        category = self.categorizer.get_category('NonExistingCategory')
        self.assertEqual(category, 'other')

    def test_add_category(self):
        self.categorizer.add_category('Transportation', 'Travel')
        category = self.categorizer.get_category('Transportation')
        self.assertEqual(category, 'travel')

    def test_remove_category(self):
        self.categorizer.add_category('Entertainment', 'Leisure')
        self.categorizer.remove_category('Entertainment')
        category = self.categorizer.get_category('Entertainment')
        self.assertEqual(category, 'other')

    def test_save_categories(self):
        self.categorizer.add_category('Entertainment', 'Leisure')
        self.categorizer.save_categories()

        # Reload the categorizer to check if the categories are saved
        new_categorizer = Categorizer()
        category = new_categorizer.get_category('Entertainment')
        self.assertEqual(category, 'leisure')

if __name__ == '__main__':
    unittest.main()