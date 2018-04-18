from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList

from generation import Stage7
from base import Saver


class Stage7Window(BaseWidget):

    def __init__(self, erd, project, rules):
        super(Stage7Window, self).__init__()
        self.set_margin(20)
        self.erd = erd
        self.project = project
        self.rules = rules

        self._entites_list = ControlList()
        self._save_button = ControlButton('Zapisz')

        self._entites_list.readonly = True
        self._save_button.value = self.__save_action

        self.populate()

        self.formset = ['_entites_list', '_save_button']

    def populate(self):
        for entity in self.erd.entities:
            self._entites_list += [repr(entity)]


    def __save_action(self):
        self.project.add_stage(Stage7(self.erd, self.rules))
        Saver.get_saver().save()
        self.parent.populate_buttons()


