import pyforms
from pyforms.gui.controls.ControlText import ControlText


class Stage1Window(pyforms.BaseWidget):

    def __init__(self):
        super(Stage1Window, self).__init__('Etap 1')

        self._label = ControlText('dupa')