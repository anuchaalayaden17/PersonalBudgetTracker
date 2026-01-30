from Customer import Customer
from Expense import Expense

# BudgetTracker manages all expenses and performs calculations
# It also communicates with Storage to save and load data
class BudgetTracker:

    def __init__(self, storage):
        # Store reference to Storage object (dependency injection)
        self.storage = storage

        # Load saved customer and expenses from JSON
        customer_data, expenses_data = self.storage.load()

        # If there is no saved customer, request user input
        if customer_data is None:
            print("\n--- CUSTOMER DETAILS ---")

            # Get customer name and income
            name = input("Enter customer name: ")
            income = float(input("Enter monthly income (€): "))

            # Create Customer object
            self.customer = Customer(name, income)

            # Initialize empty expense list
            self.expenses = []

            # Add default expenses
            self.add_default_expenses()

            # Save data to file
            self.save()

        else:
            # Load existing customer from file
            self.customer = Customer(customer_data["name"], customer_data["income"])

            # Load saved expenses from file
            self.expenses = []
            for e in expenses_data:
                self.expenses.append(Expense(e["name"], e["cost"]))

    # Adds predefined expenses when no data exists
    def add_default_expenses(self):
        default_expenses = [
            ("House Rent", 1000),
            ("Food", 250),
            ("Transport", 80),
            ("Supplies", 200),
            ("Internet", 50)
        ]

        # Create Expense objects and add them to the list
        for name, cost in default_expenses:
            self.expenses.append(Expense(name, cost))

    # CRUD - CREATE: add new expense
    def add_expense(self, name: str, cost: float):
        self.expenses.append(Expense(name, cost))
        self.save()

    # CRUD - READ: return all expenses
    def view_expenses(self):
        return self.expenses

    # CRUD - UPDATE: update existing expense
    def update_expense(self, index: int, new_name: str, new_cost: float):
        self.expenses[index].set_name(new_name)
        self.expenses[index].set_cost(new_cost)
        self.save()

    # CRUD - DELETE: remove expense
    def delete_expense(self, index: int):
        self.expenses.pop(index)
        self.save()

    # Calculate total expenses
    def total_expenses(self):
        return sum(exp.get_cost() for exp in self.expenses)

    # Calculate remaining money
    def money_left(self):
        return self.customer.get_income() - self.total_expenses()

    # Save customer and expenses to JSON file
    def save(self):
        customer_data = self.customer.to_dict()
        expenses_data = [e.to_dict() for e in self.expenses]
        self.storage.save(customer_data, expenses_data)
