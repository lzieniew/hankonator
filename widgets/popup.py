from pyforms import BaseWidget

from pyforms.gui.controls.ControlText import ControlText
from pyforms.gui.controls.ControlButton import ControlButton

class Popup(BaseWidget):

    def __init__(self, message):
        super(Popup, self).__init__()
        self._button = ControlButton('OK')
        self._button.value = self.__button_action

        self.formset = [message, '_button']

    def __button_action(self):
        self.close()
