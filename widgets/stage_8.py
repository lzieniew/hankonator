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

        self._entities_relationships_list = ControlList()
        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_action
        self._entities_relationships_list.readonly = True

        self.populate()

        self.formset = ['_entities_relationships_list', '_save_button']


    def populate(self):
        self._entities_relationships_list += ['Encje:']
        for entity in self.erd.entities:
            self._entities_relationships_list += ['\t' + entity.name_singular]
        self._entities_relationships_list += ['Związki:']
        for relationship in self.erd.relationships:
            self._entities_relationships_list += ['\t' + repr(relationship)]

    def __save_action(self):
        self.project.stages.append(Stage8(self.erd))
        Saver.get_saver().save()
