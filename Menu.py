# Menu class (provides an interactive menu with submenus)
class Menu:

    def __init__(self, tracker):
        self.tracker = tracker

    def run(self):
        while True:
            print("\n===WELCOME TO PERSONAL BUDGET TRACKER ===")
            print("Customer:", self.tracker.customer.get_name())
            print("Monthly Income: €{:.2f}".format(self.tracker.customer.get_income()))
            print("\n1. Expenses Menu")
            print("2. Budget Summary")
            print("3. Exit")

            while True:
                choice = input("Choose an option: ")

                if choice in ["1", "2", "3"]:
                    break
                else:
                    print("Please choose 1, 2 or 3.")

            if choice == "1":
                self.expenses_menu()
            elif choice == "2":
                self.summary_menu()
            elif choice == "3":
                print("Goodbye!")
                break

    # Submenu
    def expenses_menu(self):
        while True:

            print("\n--- EXPENSES MENU ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Update Expense")
            print("4. Delete Expense")
            print("5. Back")

            while True:
                choice = input("Choose an option: ")

                if choice in ["1","2","3","4","5"]:
                    break
                else:
                    print("Choose between 1 and 5.")

            # ADD EXPENSE
            if choice == "1":

                while True:
                    name = input("Expense name: ").strip()
                    if name.replace(" ","").isalpha():
                        break
                    else:
                        print("Letters only.")

                while True:
                    try:
                        cost = float(input("Expense cost (€): "))
                        if cost > 0:
                            break
                        else:
                            print("Must be positive.")
                    except:
                        print("Enter a valid number.")

                self.tracker.add_expense(name, cost)
                print("Expense added successfully.")

            # VIEW
            elif choice == "2":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses found.")
                else:
                    print("\n--- EXPENSE LIST ---")
                    for i, exp in enumerate(expenses):
                        print(f"{i+1}. {exp}")

            # UPDATE
            elif choice == "3":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses to update.")
                    continue

                for i, exp in enumerate(expenses):
                    print(f"{i+1}. {exp}")

                while True:
                    try:
                        index = int(input("Select expense number: ")) - 1
                        if 0 <= index < len(expenses):
                            break
                        else:
                            print("Invalid number.")
                    except:
                        print("Enter a number.")

                while True:
                    new_name = input("New expense name: ")
                    if new_name.replace(" ","").isalpha():
                        break
                    else:
                        print("Letters only.")

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

            # DELETE
            elif choice == "4":
                expenses = self.tracker.view_expenses()

                if len(expenses) == 0:
                    print("No expenses to delete.")
                    continue

                for i, exp in enumerate(expenses):
                    print(f"{i+1}. {exp}")

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

    def summary_menu(self):
        total = self.tracker.total_expenses()
        left = self.tracker.money_left()

        print("\n--- BUDGET SUMMARY ---")
        print("Total expenses: €{:.2f}".format(total))
        print("Money left: €{:.2f}".format(left))
