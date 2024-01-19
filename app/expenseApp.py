from expensetracker import ExpenseTracker

class ExpenseApp:
    def __init__(self, file_name: str, filter_columns: list):
        self.__exp_tracker = ExpenseTracker(file_name, filter_columns)

    def __help(self):
        print("1. Summary")
        print("2. Add expense")
        print("3. Exit")

    def execute(self):
        while True:
            self.__help()
            selection = int(input("Enter selection: "))
            if selection == 1:
                self.__exp_tracker.print_summary()
            elif selection == 2:
                self.__exp_tracker.add_expense()
            elif selection == 3:
                break
            else:
                self.__help()



if __name__ == '__main__':
    filter_columns = ['date', 'name', 'amount', 'transaction']
    et = ExpenseApp("data/cibc.csv", filter_columns)
    et.execute()