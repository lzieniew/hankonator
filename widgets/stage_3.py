from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList

from generation import Stage3
from base import Saver


class Stage3Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage3Window, self).__init__('Etap 3')
        self.set_margin(20)

        self._categories_list = ControlList()
        self._save_button = ControlButton('Zapisz')

        self.erd = erd
        self._project = project

        self._save_button.value = self.__save_action

        self._categories_list.readonly = True

        for entity in self.erd.entities:
            self._categories_list += [repr(entity)]

        self._project = project

        self.stage = self._project.get_stage(3)


    def __save_action(self):
        if self._project.stages[3] is None:
            self.stage = Stage3(self.erd)
            self._project.add_stage(self.stage)
        Saver.get_saver().save()
        self.parent.populate_buttons()
