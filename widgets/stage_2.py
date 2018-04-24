from pyforms import BaseWidget
from pyforms.gui.controls.ControlTextArea import ControlTextArea
from pyforms.gui.controls.ControlButton import ControlButton

from base import Saver
from generation import Stage2


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
        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_action

        self._project = project

        self.stage = self._project.stages[2]

        self.populate()

        self.formset = ['_reality_description_text_edit', '_dictionary_text_edit', '_users_text_edit',
                        '_functional_requirements_text_edit', '_nonfunctional_requirements_text_edit',
                        '_existing_database_text_edit', '_cost_text_edit', '_save_button']

    def populate(self):
        if self.stage is not None:
            self._reality_description_text_edit.value = self.stage.reality_description
            self._dictionary_text_edit.value = self.stage.dictionary
            self._users_text_edit.value = self.stage.users
            self._functional_requirements_text_edit.value = self.stage.functional_requirements
            self._nonfunctional_requirements_text_edit.value = self.stage.nonfunctional_requirements
            self._existing_database_text_edit.value = self.stage.existing_database
            self._cost_text_edit.value = self.stage.cost

    def __save_action(self):
        if self._project.stages[2] is None:
            self.stage = Stage2()
            self._project.add_stage(Stage2())
        self.stage.reality_description = self._reality_description_text_edit.value
        self.stage.dictionary = self._dictionary_text_edit.value
        self.stage.users = self._users_text_edit.value
        self.stage.functional_requirements = self._functional_requirements_text_edit.value
        self.stage.nonfunctional_requirements = self._nonfunctional_requirements_text_edit.value
        self.stage.existing_database = self._existing_database_text_edit.value
        self.stage.cost = self._cost_text_edit.value
        Saver.get_saver().save()
        self.parent.populate_buttons()
