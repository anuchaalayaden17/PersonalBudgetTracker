from abc import ABC, abstractmethod

# Transaction is an abstract base class
# It defines a template for all transaction types
class Transaction(ABC):

    def __init__(self, amount: float):
        # Store transaction amount
        self._amount = amount

    # Returns transaction amount
    def get_amount(self):
        return self._amount

    # Abstract method that must be implemented by child classes
    @abstractmethod
    def to_dict(self):
        pass
