import csv

class Categorizer:
    def __init__(self):
        self.__datafile = 'data/categories.csv'
        self.__categories = {}
        self.read_categories()

    def read_categories(self):
        with open(self.__datafile, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first line
            for row in reader:
                category, name = row
                self.__categories[name] = category

    def get_category(self, name: str) -> str:
        for key, value in self.__categories.items():
            if key in name.lower():
                return self.__categories.get(key)
        return "other"
    
    def add_category(self, name: str, category: str):
        name = name.lower()
        category = category.lower()
        self.__categories[name] = category

    def remove_category(self, name: str):
        name = name.lower()
        self.__categories.pop(name, None)

    def save_categories(self):
        with open(self.__datafile, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['category', 'name'])
            for name, category in self.__categories.items():
                name = name.lower()
                category = category.lower()
                writer.writerow([category, name])
    
    
        