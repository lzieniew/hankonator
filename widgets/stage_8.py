from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlList import ControlList


from base import Stage8


class Stage8Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage8Window, self).__init__()
        self.erd = erd
        self.project = project

        self._entities_relationships_list = ControlList()
        self._save_button = ControlButton('Zapisz etap 8')
        self._entities_relationships_list.readonly = True

        self.populate()


    def populate(self):
        self._entities_relationships_list += ['Encje:']
        for entity in self.erd.entities:
            self._entities_relationships_list += ['\t' + entity.name_singular]
        self._entities_relationships_list += ['Związki:']
        for relationship in self.erd.relationships:
            self._entities_relationships_list += ['\t' + repr(relationship)]

    def __save_action(self):
        self.project.stages.append(Stage8(self.erd))
