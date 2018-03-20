import pyforms
from pyforms.gui.controls.ControlToolBox import ControlToolBox


class ErdReader(pyforms.BaseWidget):

    def __init__(self):
        super(ErdReader, self).__init__('ERD reader')

        self._entity_editor = ControlToolBox()
        self.value = [ControlToolBox('aaa')]
