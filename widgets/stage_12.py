from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlLabel import ControlLabel

from generation import Stage12
from base import Saver


class Stage12Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage12Window, self).__init__()
        self.set_margin(20)

        self.erd = erd
        self.project = project

        self._label = ControlLabel('Etap 12')
        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_action

        self.formset = ['_label', '_save_button']

    def __save_action(self):
        self.project.add_stage(Stage12(self.erd))
        Saver.get_saver().save()
        self.parent.populate_buttons()