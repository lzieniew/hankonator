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

        self._entities_relationships_list = ControlList()
        self._save_button = ControlButton('Zapisz')

        self._entities_relationships_list.readonly = True
        self._save_button.value = self.__save_action

        self.populate()

        self.formset = ['Etap 7, definicje encji i związków - sprawdz czy wszystkie encje i związki znajdują się na liście, w razie potrzeby popraw błędy w edytorze ERD',
                        '_entities_relationships_list', '_save_button']

    def populate(self):
        self._entities_relationships_list += ['Encje:']
        for entity in self.erd.entities:
            self._entities_relationships_list += ['\t' + repr(entity)]
        self._entities_relationships_list += ['Związki:']
        for relationship in self.erd.relationships:
            self._entities_relationships_list += ['\t' + repr(relationship)]


    def __save_action(self):
        self.project.add_stage(Stage7(self.erd, self.rules))
        Saver.get_saver().save()
        self.parent.populate_buttons()


