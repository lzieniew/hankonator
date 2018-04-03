from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from base import Transaction


class TypeCombo(ControlCombo):

    def __init__(self, entity_combo):
        super(TypeCombo, self).__init__()
        self.entity_combo = entity_combo

    def activated_event(self, index):
        if index is not 0:
            self.entity_combo.setVisible(True)
        else:
            self.entity_combo.setVisible(False)


class TransactionsEditor(BaseWidget):

    def __init__(self, erd, transactions):
        super(TransactionsEditor, self).__init__()
        self.set_margin(20)

        self.transactions = transactions
        self.erd = erd

        self._transaction_list = ControlList()
        self._add_transaction_button = ControlButton('Dodaj transakcję')
        self._edit_transaction_button = ControlButton('Edytuj transakcję')
        self._remove_transaction_button = ControlButton('Usuń transakcję')

        self._add_transaction_button.value = self.__add_transaction_action

        self.formset = ['_transaction_list', ('_add_transaction_button', '_edit_transaction_button', '_remove_transaction_button')]

    def populate(self):
        for transaction in self.transactions:
            self._transaction_list += [transaction]

    def __add_transaction_action(self):
        win = TransactionEditor(self.erd, self.transactions)
        win.parent = self
        win.show()


class TransactionEditor(BaseWidget):

    def __init__(self, erd, transactions, transaction=None):
        super(TransactionEditor, self).__init__()
        self.transactions = transactions
        self.erd = erd

        self._name_edit_text = ControlText('Nazwa transakcji')
        self._entity_combo = ControlCombo()
        self._type_combo = TypeCombo(self._entity_combo)
        self._save_button = ControlButton('Zapisz transakcję')
        self._save_button.value = self.__save_action

        self._type_combo.add_item(Transaction.OTHER)
        self._type_combo.add_item(Transaction.ADD)
        self._type_combo.add_item(Transaction.EDIT)
        self._type_combo.add_item(Transaction.REMOVE)

        for entity in self.erd.entities:
            self._entity_combo.add_item(entity.name_singular)

        self._entity_combo.setVisible(False)

        self.formset = ['_name_edit_text', '_type_combo', '_entity_combo', '_save_button']

    def __save_action(self):
        self.transactions.append(Transaction(name=self._name_edit_text.value))

        self.close()
