from payment import Payment

class COD(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("paying from cod")