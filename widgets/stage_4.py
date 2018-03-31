from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList

from base import Stage4

class Stage4Window(BaseWidget):
    def __init__(self, project, erd):
        super(Stage4Window, self).__init__('Etap 4')

        self._categories_list = ControlList()
        self._save_button = ControlButton('Zapisz etap 4')

        self._project = project
        self.erd = erd

        self._save_button.value = self.__save_action

        self._categories_list.readonly = True

        for relationship in self.erd.relationships:
            self._categories_list += [repr(relationship)]

    def __save_action(self):
        self._project.stages.append(Stage4(self.erd))
