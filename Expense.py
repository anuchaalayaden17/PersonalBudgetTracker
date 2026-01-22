from Transaction import Transaction

# Expense class (Inheritance + Polymorphism)
class Expense(Transaction):

    def __init__(self, name: str, cost: float):
        super().__init__(cost)
        self._name = name

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._amount

    def set_name(self, new_name: str):
        self._name = new_name

    def set_cost(self, new_cost: float):
        self._amount = new_cost

    def to_dict(self):
        return {"name": self._name, "cost": self._amount}

    def __str__(self):
        return f"{self._name} - €{self._amount:.2f}"
