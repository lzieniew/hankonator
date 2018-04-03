from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget

from .erd_reader import ErdReader
from .transaction_editor import TransactionsEditor


class InitialDataEditor(BaseWidget):

    def __init__(self, erd, transactions):
        super(InitialDataEditor, self).__init__('Edytor podstawowych danych projektu')
        self.set_margin(10)

        self.erd = erd
        self.transactions = transactions

        self._label = ControlLabel('W tym oknie wpisz podstawowe dane dotyczące Twojego projektu')
        self._erd_button = ControlButton('ERD')
        self._transactions_button = ControlButton('Transakcje')
        self._users_button = ControlButton('Użytkownicy')
        self._panel = ControlEmptyWidget()
        self._save_button = ControlButton('Zapisz dane')

        self._erd_button.value = self.__erd_action
        self._transactions_button.value = self.__transactions_action

        self.formset = ['_label',
                        ('_erd_button', '_transactions_button', '_users_button'),
                        '_panel',
                        '_save_button']

    def __erd_action(self):
        win = ErdReader(self.erd)
        win.parent = self
        self._panel.value = win

    def __transactions_action(self):
        win = TransactionsEditor(self.erd, self.transactions)
        win.parent = self
        self._panel.value = win

    def __users_action(self):
        pass

    def __save_acton(self):
        self.close()
