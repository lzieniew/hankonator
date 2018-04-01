from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlLabel import ControlLabel

from base import Stage10

class Stage10Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage10Window, self).__init__()
        self.set_margin(20)
        self.erd = erd
        self.project = project

        self._text = ControlLabel('Nie musisz nic robić w tym etapie, po prostu kliknij zapisz :)')

        self._save_button = ControlButton('Zapisz etap 10')
        self._save_button.value = self.__save_action

    def __save_action(self):
        self.project.stages.append(Stage10(self.erd))