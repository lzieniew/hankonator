import pyforms
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlButton import  ControlButton
from pyforms.gui.controls.ControlTextArea import ControlTextArea
import docx

from base import Saver
from generation import Stage1


class Stage1Window(pyforms.BaseWidget):

    def __init__(self, project):
        super(Stage1Window, self).__init__('Etap 1')
        self.set_margin(20)

        self._topic_edit_text = ControlTextArea('Temat')
        self._objective_edit_text = ControlTextArea('Cel')
        self._range_edit_text = ControlTextArea('Zakres')
        self._users_edit_text = ControlTextArea(u'Użytkownicy')
        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_action

        self._project = project

        self.stage = self._project.stages[1]

        self.populate()

    def populate(self):
        if self.stage is not None:
            self._topic_edit_text.value = self.stage.topic
            self._objective_edit_text.value = self.stage.objective
            self._range_edit_text.value = self.stage.range
            self._users_edit_text.value = self.stage.users

    def __save_action(self):
        if self._project.stages[1] is None:
            self.stage = Stage1()
            self._project.add_stage(self.stage)
        self.stage.topic = self._topic_edit_text.value
        self.stage.objective = self._objective_edit_text.value
        self.stage.range = self._range_edit_text.value
        self.stage.users = self._users_edit_text.value
        Saver.get_saver().save()
        self.parent.populate_buttons()
