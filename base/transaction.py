


class Transaction(object):

    ID = 1

    # enums for type of transaction (does it represent add, edit, remove of some entity, or something different)
    ADD = u'Transakcja dodająca instancję encji'
    EDIT = u'Transakcja edytująca instancję encji'
    REMOVE = u'Transakcja usuwająca instancję encji'
    OTHER = u'Inna transakcja'

    def __init__(self, name, type=OTHER, entity=None):
        self.id = Transaction.ID
        Transaction.ID +=1

        self.name = name
        self.type = type
        self.entity = entity

    def __repr__(self):
        return self.name + ': ' + self.type + ' (' + self.entity + ')'
