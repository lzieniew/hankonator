from pyforms import BaseWidget
from pyforms.gui.controls.ControlTextArea import ControlTextArea


class Stage2Window(BaseWidget):

    def __init__(self, project):
        super(Stage2Window, self).__init__('Etap 2')
        self.set_margin(20)

        self._reality_description_text_edit = ControlTextArea('Szczegółowy opis wycinka rzeczywistości')
        self._dictionary_text_edit = ControlTextArea('Słownik pojęć')
        self._users_text_edit = ControlTextArea('Użytkownicy i zakres uprawnień')
        self._functional_requirements_text_edit = ControlTextArea('Wymagania funkcjonalne')
        self._nonfunctional_requirements_text_edit = ControlTextArea('Wymagania niefunkcjonalne')
        self._existing_database_text_edit = ControlTextArea('Analiza isniejącej bazy danych')
        self._cost_text_edit = ControlTextArea('Analiza kosztów')

        self._project = project
