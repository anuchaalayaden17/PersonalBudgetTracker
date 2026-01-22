from abc import ABC, abstractmethod

# Transaction is an abstract class
class Transaction(ABC):

    def __init__(self, amount: float):
        self._amount = amount

    def get_amount(self):
        return self._amount
#means anotation
    @abstractmethod
    def to_dict(self):
        pass
