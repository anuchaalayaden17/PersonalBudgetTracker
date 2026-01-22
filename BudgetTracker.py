from Customer import Customer
from Expense import Expense

# BudgetTracker manages the expenses list (CRUD) and calculates the remaining balance
class BudgetTracker:

    def __init__(self, storage):
        self.storage = storage

        # Load saved customer + expenses from JSON
        customer_data, expenses_data = self.storage.load()

        # If no saved customer, ask user input
        if customer_data is None:
            print("\n--- CUSTOMER DETAILS ---")
            name = input("Enter customer name: ")
            income = float(input("Enter monthly income (€): "))

            self.customer = Customer(name, income)
            self.expenses = []
            self.add_default_expenses()
            self.save()

        else:
            # Load customer from file
            self.customer = Customer(customer_data["name"], customer_data["income"])

            # Load expenses from file
            self.expenses = []
            for e in expenses_data:
                self.expenses.append(Expense(e["name"], e["cost"]))

    def add_default_expenses(self):
        default_expenses = [
            ("House Rent", 1000),
            ("Food", 250),
            ("Transport", 80),
            ("Supplies", 200),
            ("Internet", 50)
        ]

        for name, cost in default_expenses:
            self.expenses.append(Expense(name, cost))

    # CRUD - CREATE
    def add_expense(self, name: str, cost: float):
        self.expenses.append(Expense(name, cost))
        self.save()

    # CRUD - READ
    def view_expenses(self):
        return self.expenses

    # CRUD - UPDATE
    def update_expense(self, index: int, new_name: str, new_cost: float):
        self.expenses[index].set_name(new_name)
        self.expenses[index].set_cost(new_cost)
        self.save()

    # CRUD - DELETE
    def delete_expense(self, index: int):
        self.expenses.pop(index)
        self.save()

    # Calculations
    def total_expenses(self):
        return sum(exp.get_cost() for exp in self.expenses)

    def money_left(self):
        return self.customer.get_income() - self.total_expenses()

    # Save to JSON
    def save(self):
        customer_data = self.customer.to_dict()
        expenses_data = [e.to_dict() for e in self.expenses]
        self.storage.save(customer_data, expenses_data)