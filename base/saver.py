

class Saver(object):

    def __init__(self, erd, perspectives, rules, transactions, users):
        self.erd = erd
        self.perspectives = perspectives
        self.rules = rules
        self.transactions = transactions
        self.users = users

    def save(self):
        pass
        # TODO saving to file

    @staticmethod
    def load():
        pass
    # TODO load function return deserialized object