from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList

from base import Stage3

class Stage3Window(BaseWidget):
    def __init__(self, project, erd):
        super(Stage3Window, self).__init__('Etap 3')

        self._categories_list = ControlList()
        self._save_button = ControlButton('Zapisz etap 3')

        self._project = project
        self.erd = erd

        self._save_button.value = self.__save_action

        self._categories_list.readonly = True

        for entity in self.erd.entities:
            self._categories_list += [repr(entity)]

    def __save_action(self):
        self._project.stages.append(Stage3(self.erd))
