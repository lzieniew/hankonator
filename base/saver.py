import pickle

from base import Erd, Entity, Relationship, Rule, Transaction, Perspective, User


class Saver(object):

    SAVER_INSTANCE = None

    def __init__(self, erd=None, perspectives=None, rules=None, transactions=None, users=None):
        self.erd = erd
        self.perspectives = perspectives
        self.rules = rules
        self.transactions = transactions
        self.users = users

    def save(self):
        f = open('save.pickle', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def get_saver():
        if Saver.SAVER_INSTANCE is not None:
            return Saver.SAVER_INSTANCE
        else:
            try:
                f = open('save.pickle', 'rb')
                saver = pickle.load(f)
            except Exception:
                saver = Saver(erd=Erd(), perspectives=[], rules=[], transactions=[], users=[])
            Saver.SAVER_INSTANCE = saver
            return saver
