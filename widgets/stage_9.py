from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from generation import Stage9
from base import Saver


class Stage9Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage9Window, self).__init__('Etap 9')
        self.set_margin(40)

        self._save_button = ControlButton('Zapisz')

        self.erd = erd
        self._project = project

        self._save_button.value = self.__save_action

        self._project = project

        self.stage = self._project.get_stage(9)

        self.formset = ['Wszystko już gotowe, naciśnij zapisz', '_save_button']

    def __save_action(self):
        if self._project.stages[9] is None:
            self.stage = Stage9(self.erd)
            self._project.add_stage(self.stage)
        Saver.get_saver().save()
        self.parent.populate_buttons()


class CategoryCombo(ControlCombo):

    def __init__(self, categories, edit_description):
        super(CategoryCombo, self).__init__()

        self.categories = categories
        self.edit_description = edit_description

    def activated_event(self, index):
        category = self.categories[index]
        self.edit_description.value = category.description


