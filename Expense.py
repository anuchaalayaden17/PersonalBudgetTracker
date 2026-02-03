from Transaction import Transaction

# Expense class represents a single expense
# here i implemented inheritance. It inherits from Transaction
class Expense(Transaction):

    def __init__(self, name: str, cost: float):
        # Call parent constructor to set amount
        super().__init__(cost)

        # Store expense name
        self._name = name

    # Returns expense name
    def get_name(self):
        return self._name

    # Returns expense cost (amount from parent class)
    def get_cost(self):
        return self._amount

    # Updates expense name
    def set_name(self, new_name: str):
        self._name = new_name

    # Updates expense cost
    def set_cost(self, new_cost: float):
        self._amount = new_cost

    # Convert expense object to dictionary for JSON storage
    #because it returns the name of the expense and the amount that will be saved in the JSON file
    def to_dict(self):
        return {"name": self._name, "cost": self._amount}

    # Here i implemented polymorphism. String is a representation for printing expenses
    def __str__(self):
        return f"{self._name} - €{self._amount:.2f}"
