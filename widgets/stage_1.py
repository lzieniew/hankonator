import pyforms
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlButton import  ControlButton
from pyforms.gui.controls.ControlTextArea import ControlTextArea
import docx


class Stage1Window(pyforms.BaseWidget):

    def __init__(self, project):
        super(Stage1Window, self).__init__('Etap 1')

        self._theme_edit_text = ControlTextArea('Temat')
        self._goal_edit_text = ControlTextArea('Cel')
        self._range_edit_text = ControlTextArea('Zakres')
        self._users_edit_text = ControlTextArea(u'Użytkownicy')
        self._save_button = ControlButton('Zapisz')

        self._project = project
