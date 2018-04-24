import pickle

from base import Erd
from generation import Project


class Saver(object):

    SAVER_INSTANCE = None
    PROGRESS_BAR = None

    def __init__(self, erd=None, perspectives=None, rules=None, transactions=None, users=None, project=None, categories=None, progress_bar=None):
        self.erd = erd
        self.perspectives = perspectives
        self.rules = rules
        self.transactions = transactions
        self.users = users
        self.project = project

        self.categories = categories

        Saver.PROGRESS_BAR = progress_bar

    def save(self):
        f = open('save.pickle', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()

    @staticmethod
    def get_saver():
        if Saver.SAVER_INSTANCE is not None:
            return Saver.SAVER_INSTANCE
        else:
            try:
                f = open('save.pickle', 'rb')
                saver = pickle.load(f)
            except Exception:
                saver = Saver(erd=Erd(), perspectives=[], rules=[], transactions=[], users=[], categories=[], project=Project())
            Saver.SAVER_INSTANCE = saver
            return saver
