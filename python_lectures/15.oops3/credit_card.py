from payment import Payment 

class CreditCard(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("paying from credit card")