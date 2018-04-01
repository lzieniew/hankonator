from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList

from base import Stage7

class Stage7Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage7Window, self).__init__()
        self.set_margin(20)
        self.erd = erd
        self.project = project

        self._entites_list = ControlList()
        self._save_button = ControlButton('Zapisz etap 7')

        self._entites_list.readonly = True
        self._save_button.value = self.__save_action

        self.populate()

    def populate(self):
        for entity in self.erd.entities:
            self._entites_list += [repr(entity)]


    def __save_action(self):
        self.project.stages.append(Stage7(self.erd))


