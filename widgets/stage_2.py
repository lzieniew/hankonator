from pyforms import BaseWidget
from pyforms.gui.controls.ControlText import ControlText

class Stage2Window(BaseWidget):
    def __init__(self):
        super(Stage2Window, self).__init__('Etap 2')

        self._reality_description_text_edit = ControlText('Szczegółowy opis wycinka rzeczywistości')
        self._dictionary_text_edit = ControlText('Słownik pojęć')
        self._users_text_edit = ControlText('Użytkownicy i zakres uprawnień')
        self._functional_requirements_text_edit = ControlText('Wymagania funkcjonalne')
        self._nonfunctional_requirements_text_edit = ControlText('Wymagania niefunkcjonalne')
        self._existing_database_text_edit = ControlText('Analiza isniejącej bazy danych')
        self._cost_text_edit = ControlText('Analiza kosztów')
