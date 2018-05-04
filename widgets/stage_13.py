from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from generation import Stage5
from base import Saver


class Stage13Window(BaseWidget):

    def __init__(self, project):
        super(Stage13Window, self).__init__('Etap 13')
        self.set_margin(40)

        self._save_button = ControlButton('Zapisz')

        self._project = project

        self._save_button.value = self.__save_action

        self._project = project

        self.stage = self._project.get_stage(5)

        self.formset = ['Generowanie etapu 13 nie zostało jeszcze zaimplementowane - w projekcie znajdzie się tylko nagłówek z tytułem etapu', '_save_button']

    def __save_action(self):
        if self._project.stages[13] is None:
            self.stage = Stage5()
            self._project.add_stage(self.stage)
        Saver.get_saver().save()
        self.parent.populate_buttons()
