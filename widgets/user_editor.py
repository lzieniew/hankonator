from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from base import User, Saver


class UsersEditor(BaseWidget):

    def __init__(self, erd, users):
        super(UsersEditor, self).__init__()
        self.set_margin(20)

        self.users = users
        self.erd = erd

        self._user_list = ControlList()
        self._add_user_button = ControlButton('Dodaj użytkownika')
        self._edit_user_button = ControlButton('Edytuj użytkownika')
        self._remove_user_button = ControlButton('Usuń użytkownika')

        self._add_user_button.value = self.__add_user_action
        self._edit_user_button.value = self.__edit_user_action
        self._remove_user_button.value = self.__remove_user_action

        self._user_list.readonly = True

        self.formset = ['_user_list', ('_add_user_button', '_edit_user_button', '_remove_user_button')]

        self.populate()

    def populate(self):
        self._user_list.clear()
        for user in self.users:
            self._user_list += [user.name]

    def __add_user_action(self):
        win = UserEditor(self.erd, self.users)
        win.parent = self
        win.show()

    def __edit_user_action(self):
        index = self._user_list.selected_row_index
        if index is not None:
            win = UserEditor(self.erd, self.users, self.users[index])
            win.parent = self
            win.show()

    def __remove_user_action(self):
        index = self._user_list.selected_row_index
        if index is not None:
            del self.users[index]
            self.populate()


class UserEditor(BaseWidget):

    def __init__(self, erd, users, user=None):
        super(UserEditor, self).__init__()
        self.users = users
        self.erd = erd

        if user is not None:
            self.user = user
        else:
            self.user = User('', '')

        self._name_edit_text = ControlText('Nazwa użytkownika')
        self._save_button = ControlButton('Zapisz')
        self._save_button.value = self.__save_action

        self.populate()

    def populate(self):
        self._name_edit_text.value = repr(self.user)

    def __save_action(self):
        self.user.name = self._name_edit_text.value
        if self.user not in self.users:
            self.users.append(self.user)
        Saver.get_saver().save()
        self.close()
        self.parent.populate()
