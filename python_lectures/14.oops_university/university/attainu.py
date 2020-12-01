from university.university import University


class Attainu(University):
    def __init__(self, name, location, logo):
        super().__init__(name, location)

        self.logo = logo
        self.batches = list()

    def get_isa(self):
        print(f"{self.name}: getting isa for batch.")

    def add_batch(self, batch):
        self.batches.append(batch)

    def print_all_batches(self):
        for batch in self.batches:
            print(batch.name)


