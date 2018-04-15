

class Perspective(object):

    ID = 1

    def __init__(self, name, transactions, user):
        self.id = Perspective.ID
        Perspective.ID += 1
        self.name = name
        self.transactions = transactions
        self.user = user

    def __repr__(self):
        return self.name + repr(self.transactions)

    def __str__(self):
        return self.name