from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList


from generation import Stage8
from base import Saver


class Stage8Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage8Window, self).__init__()
        self.set_margin(20)
        self.erd = erd
        self.project = project

        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_action

        self.formset = ['Etap 8 - wszystkie dane są już uzupełnione, wystarczy że naciścniesz zapisz', '_save_button']

    def __save_action(self):
        self.project.add_stage(Stage8(self.erd))
        Saver.get_saver().save()
        self.parent.populate_buttons()
