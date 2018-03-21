import pyforms
from pyforms.gui.controls.ControlToolBox import ControlToolBox
from pyforms.gui.controls.ControlButton import ControlButton


class ErdReader(pyforms.BaseWidget):

    def __init__(self):
        super(ErdReader, self).__init__('ERD reader')

        self._entity_editor = ControlToolBox()
        self.value = [ControlToolBox('aaa')]

        self._add_entity_button = ControlButton(u'Dodaj encję')

        self.formset = ['Witam', 'aaa', 'bbb', 'ccc', '_add_entity_button']
        for i in range(100):
            self.formset.append('dupa')
