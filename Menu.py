# Menu class (provides an interactive menu with submenus)
class Menu:

    def __init__(self, tracker):
        self.tracker = tracker

    def run(self):
        while True:

            print("\n=== PERSONAL BUDGET TRACKER ===")
            print("Customer:", self.tracker.customer.get_name())
            print("Monthly Income: €{:.2f}".format(self.tracker.customer.get_income()))
            print("\n1. Expenses Menu")
            print("2. Budget Summary")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.expenses_menu()
            elif choice == "2":
                self.summary_menu()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

    # Submenu that appears based on the user's selection
    def expenses_menu(self):
        while True:

            print("\n--- EXPENSES MENU ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Update Expense")
            print("4. Delete Expense")
            print("5. Back")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Expense name: ")
                cost = float(input("Expense cost (€): "))
                self.tracker.add_expense(name, cost)
                print("Expense added successfully.")

            elif choice == "2":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses found.")
                else:
                    print("\n--- EXPENSE LIST ---")
                    for i, exp in enumerate(expenses):
                        print(f"{i+1}. {exp}")

            elif choice == "3":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses to update.")
                    continue

                print("\n--- EXPENSE LIST ---")
                for i, exp in enumerate(expenses):
                    print(f"{i+1}. {exp}")

                index = int(input("Select expense number to update: ")) - 1

                new_name = input("New expense name: ")
                new_cost = float(input("New expense cost (€): "))

                self.tracker.update_expense(index, new_name, new_cost)
                print("Expense updated successfully.")

            elif choice == "4":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses to delete.")
                    continue

                print("\n--- EXPENSE LIST ---")
                for i, exp in enumerate(expenses):
                    print(f"{i+1}. {exp}")

                index = int(input("Select expense number to delete: ")) - 1

                self.tracker.delete_expense(index)
                print("Expense deleted successfully.")

            elif choice == "5":
                break

            else:
                print("Invalid option.")

    def summary_menu(self):

        total = self.tracker.total_expenses()
        left = self.tracker.money_left()

        print("\n--- BUDGET SUMMARY ---")
        print("Total expenses: €{:.2f}".format(total))
        print("Money left: €{:.2f}".format(left))
