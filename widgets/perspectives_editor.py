from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from base import Perspective, Saver

class PerspectivesEditor(BaseWidget):

    def __init__(self, perspectives, users):
        super(PerspectivesEditor, self).__init__()
        self.set_margin(20)

        self.perspectives = perspectives
        self.users = users

        self._perspectives_list = ControlList()
        self._add_perspective_button = ControlButton('Dodaj perspektywę')
        self._edit_perspective_button = ControlButton('Edytuj perspektywę')
        self._remove_perspective_button = ControlButton('Usuń perspektywę')

        self._add_perspective_button.value = self.__add_perspective_action
        self._edit_perspective_button.value = self.__edit_perspective_action
        self._remove_perspective_button.value = self.__remove_perspective_action

        self._perspectives_list.readonly = True

        self.formset = ['_perspectives_list',
                        ('_add_perspective_button', '_edit_perspective_button', '_remove_perspective_button')]

        self.populate()

    def populate(self):
        self._perspectives_list.clear()
        for perspective in self.perspectives:
            self._perspectives_list += [perspective.name]

    def __add_perspective_action(self):
        win = PerspectiveEditor(self.perspectives)
        win.parent = self
        win.show()

    def __edit_perspective_action(self):
        index = self._perspectives_list.selected_row_index
        if index is not None:
            win = PerspectiveEditor(self.perspectives, perspective=self.perspectives[index])
            win.parent = self
            win.show()

    def __remove_perspective_action(self):
        index = self._perspectives_list.selected_row_index
        if index is not None:
            del self.perspectives[index]
            self.populate()

class PerspectiveEditor(BaseWidget):

    def __init__(self, perspectives, perspective=None):
        super(PerspectiveEditor, self).__init__()
        self.perspectives = perspectives

        if perspective is not None:
            self.perspective = perspective
        else:
            self.perspective = Perspective('', [], None)

        self._name_edit_text = ControlText('Nazwa perspektywy')
        self._save_button = ControlButton('Zapisz')
        self._save_button.value = self.__save_action

        self.populate()

    def populate(self):
        self._name_edit_text.value = str(self.perspective)

    def __save_action(self):
        self.perspective.name = self._name_edit_text.value
        if self.perspective not in self.perspectives:
            self.perspectives.append(self.perspective)
        Saver.get_saver().save()
        self.close()
        self.parent.populate()
