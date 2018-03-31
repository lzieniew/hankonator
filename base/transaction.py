


class Transaction(object):

    ID = 1

    # enums for type of transaction (does it represent add, edit, remove of some entity, or something different)
    ADD = 10
    EDIT = 11
    REMOVE = 12
    OTHER = 13

    def __init__(self, name, type=OTHER, entity=None):
        self.id = Transaction.ID
        Transaction.ID +=1

        self.name = name
        self.type = type
        self.entity = entity
