from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from base import Stage6, Transaction


class Stage6Window(BaseWidget):

    def __init__(self, erd, transactions):
        super(Stage6Window, self).__init__()
        self.set_margin(20)
        self._transaction_list = ControlList()
        self._transaction_list.readonly = True

        self._add_transaction_button = ControlButton(u'Dodaj transakcję')
        self._remove_transaction_button = ControlButton(u'Usuń transakcję')

        self._add_transaction_button.value = self.__add_trasaction_action
        self._remove_transaction_button.value = self.__remove_transaction_action

        self.formset = ['_transaction_list', ('_add_transaction_button', '_remove_transaction_button')]

        self.erd = erd
        self.transactions = transactions

        self._populate()

    def _populate(self):
        self._transaction_list.clear()
        for transaction in self.transactions:
            self._transaction_list += [transaction.name]

    def __add_trasaction_action(self):
        win = TransactionEditor(self.transactions)
        win.parent = self
        win.show()

    def __remove_transaction_action(self):
        pass


class TransactionEditor(BaseWidget):

    def __init__(self, transactions):
        super(TransactionEditor, self).__init__()
        self.transactions = transactions

        self._name_edit_text = ControlText('Nazwa transakcji')
        # TODO combo box list of types of transactions
        self._type_combo = ControlCombo()
        self._save_button = ControlButton('Zapisz transakcję')
        self._save_button.value = self.__save_action

    def __save_action(self):
        self.transactions.append(Transaction(name=self._name_edit_text.value))
        self.parent._populate()

        self.close()

