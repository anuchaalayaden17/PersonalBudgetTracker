# Customer class (stores customer name and monthly income)
class Customer:

    def __init__(self, name: str, income: float):
        self._name = name
        self._income = income

    def get_name(self):
        return self._name

    def get_income(self):
        return self._income

    def to_dict(self):
        return {"name": self._name, "income": self._income}
