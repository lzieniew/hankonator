from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget

from .erd_reader import ErdReader
from .transaction_editor import TransactionsEditor
from .user_editor import UsersEditor
from .perspectives_editor import PerspectivesEditor
from base import Rule, Saver


class InitialDataEditor(BaseWidget):

    def __init__(self, erd, transactions, users, perspectives, rules):
        super(InitialDataEditor, self).__init__('Edytor podstawowych danych projektu')
        self.set_margin(10)

        self.erd = erd
        self.transactions = transactions
        self.users = users
        self.perspectives = perspectives
        self.rules = rules

        self._label = ControlLabel('W tym oknie wpisz podstawowe dane dotyczące Twojego projektu')
        self._erd_button = ControlButton('ERD')
        self._transactions_button = ControlButton('Transakcje')
        self._users_button = ControlButton('Użytkownicy')
        self._perspectives_button = ControlButton('Perspektywy')
        self._panel = ControlEmptyWidget()

        self._erd_button.value = self.__erd_action
        self._transactions_button.value = self.__transactions_action
        self._users_button.value = self.__users_action
        self._perspectives_button.value = self.__perspectives_action

        self.formset = ['_label',
                        ('_erd_button', '_users_button',
                         # '_transactions_button',
                         # perspectives editor commented out for now

                         # '_perspectives_button'
                        ),
                        '_panel']

    def __erd_action(self):
        win = ErdReader(self.erd)
        win.parent = self
        self._panel.value = win

    def __transactions_action(self):
        win = TransactionsEditor(self.erd, self.transactions)
        win.parent = self
        self._panel.value = win

    def __users_action(self):
        win = UsersEditor(self.erd, self.users)
        win.parent = self
        self._panel.value = win

    def __perspectives_action(self):
        win = PerspectivesEditor(self.perspectives, self.users)
        win.parent = self
        self._panel.value = win