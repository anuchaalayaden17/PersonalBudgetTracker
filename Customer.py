# Customer class represents the user of the budget tracker
# It stores the customer's name and monthly income
class Customer:

    def __init__(self, name: str, income: float):
        # Private attributes for customer details
        self._name = name
        self._income = income

    # Returns customer name
    def get_name(self):
        return self._name

    # Returns customer income
    def get_income(self):
        return self._income

    # Converts customer object to dictionary format for JSON storage
    def to_dict(self):
        return {"name": self._name, "income": self._income}

