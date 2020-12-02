"""
Inheritance:

Encapsulation:

"""

class Bank:
    def __init__(self, name):
        self.name = name
        self._amount = 0

    def add_amount(self, x):
        self._amount += x

    def get_amount(self):
        return self._amount

class HDFC(Bank):
    def __init__(self):
        name = "HDFC"
        super().__init__(name)

if __name__ == "__main__":
    bank = HDFC()
    bank.add_amount(100)
    print(bank.get_amount())
