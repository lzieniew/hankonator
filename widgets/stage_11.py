from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlLabel import ControlLabel

from generation import Stage11
from base import Saver


class Stage11Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage11Window, self).__init__()
        self.set_margin(20)
        self.erd = erd
        self.project = project

        self._label = ControlLabel('W tym etapie nie musisz niczego poprawiać, po prostu kliknij zapisz :)')
        self._save_button = ControlButton('Zapisz')
        self._save_button.value = self.__save_action

    def __save_action(self):
        self.project.stages.append(Stage11(self.erd))
        Saver.get_saver().save()
