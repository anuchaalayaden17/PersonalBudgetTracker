# Menu class controls all user interaction in the system
# It displays menus, validates input, and calls BudgetTracker methods
class Menu:

    def __init__(self, tracker):
    # Store reference to BudgetTracker so Menu can access expense logic
    # menu does not calculate. It calls BudgetTracker, which shows abstraction
        self.tracker = tracker

    # Main menu of the application
    def run(self):
        while True:
            print("\n===WELCOME TO PERSONAL BUDGET TRACKER ===")
            print("Customer:", self.tracker.customer.get_name())
            print("Monthly Income: €{:.2f}".format(self.tracker.customer.get_income()))
            print("\n1. Expenses Menu")
            print("2. Budget Summary")
            print("3. Exit")

            # Keep asking until the user enters a valid menu option
            while True:
                choice = input("Choose an option: ")

                if choice in ["1", "2", "3"]:
                    break
                else:
                    print("Please choose 1, 2 or 3.")

            # Navigate based on user choice
            if choice == "1":
                self.expenses_menu()
            elif choice == "2":
                self.summary_menu()
            elif choice == "3":
                print("Goodbye!")
                break

    # Expenses submenu
    def expenses_menu(self):
        while True:

            print("\n--- EXPENSES MENU ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Update Expense")
            print("4. Delete Expense")
            print("5. Back")

            # Validate submenu choice
            while True:
                choice = input("Choose an option: ")

                if choice in ["1","2","3","4","5"]:
                    break
                else:
                    print("Choose between 1 and 5.")

            # CREATE EXPENSE
            if choice == "1":

                # Validate expense name (letters only)
                while True:
                    name = input("Expense name: ").strip()
                    if name.replace(" ","").isalpha():
                        break
                    else:
                        print("Letters only.")

                # Validate expense cost (positive number)
                while True:
                    try:
                        cost = float(input("Expense cost (€): "))
                        if cost > 0:
                            break
                        else:
                            print("Must be positive.")
                    except:
                        print("Enter a valid number.")

                # Add expense through BudgetTracker
                self.tracker.add_expense(name, cost)
                print("Expense added successfully.")

            # READ EXPENSES
            elif choice == "2":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses found.")
                else:
                    print("\n--- EXPENSE LIST ---")
                    for i, exp in enumerate(expenses):
                        print(f"{i+1}. {exp}")

            # UPDATE EXPENSE
            elif choice == "3":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses to update.")
                    continue

                for i, exp in enumerate(expenses):
                    print(f"{i+1}. {exp}")

                # Validate index selection
                while True:
                    try:
                        index = int(input("Select expense number: ")) - 1
                        if 0 <= index < len(expenses):
                            break
                        else:
                            print("Invalid number.")
                    except:
                        print("Enter a number.")

                # Validate new name
                while True:
                    new_name = input("New expense name: ")
                    if new_name.replace(" ","").isalpha():
                        break
                    else:
                        print("Letters only.")

                # Validate new cost
                while True:
                    try:
                        new_cost = float(input("New expense cost (€): "))
                        if new_cost > 0:
                            break
                        else:
                            print("Must be positive.")
                    except:
                        print("Enter a number.")

                self.tracker.update_expense(index, new_name, new_cost)
                print("Expense updated.")

            # DELETE EXPENSE
            elif choice == "4":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses to delete.")
                    continue

                for i, exp in enumerate(expenses):
                    print(f"{i+1}. {exp}")

                # Validate index
                while True:
                    try:
                        index = int(input("Select expense number: ")) - 1
                        if 0 <= index < len(expenses):
                            break
                        else:
                            print("Invalid number.")
                    except:
                        print("Enter a number.")

                self.tracker.delete_expense(index)
                print("Expense deleted.")

            elif choice == "5":
                break

    # Display budget summary
    def summary_menu(self):
        total = self.tracker.total_expenses()
        left = self.tracker.money_left()

        print("\n--- BUDGET SUMMARY ---")
        print("Total expenses: €{:.2f}".format(total))
        print("Money left: €{:.2f}".format(left))
