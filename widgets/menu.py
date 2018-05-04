# -*- coding: utf-8 -*-
import pyforms
from pyforms.controls import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlProgress import ControlProgress
from generation import Project
from widgets.stage_5 import Stage5Window
from .initial_data_editor import InitialDataEditor

from .stage_1 import Stage1Window
from .stage_2 import Stage2Window
from .stage_3 import Stage3Window
from .stage_4 import Stage4Window
from .stage_6 import Stage6Window
from .stage_7 import Stage7Window
from .stage_8 import Stage8Window
from .stage_9 import Stage9Window
from .stage_10 import Stage10Window
from .stage_11 import Stage11Window
from .stage_12 import Stage12Window

from base import Erd, Entity, Attribute, Relationship, Types, Saver


class Menu(pyforms.BaseWidget):

    PROGRESS_BAR = None

    def __init__(self):
        super(Menu, self).__init__('Hankonator MENU')
        self.set_margin(30)

        self._panel = ControlEmptyWidget()
        self._progress_bar = ControlProgress(defaultValue=0, min=0, max=100)
        Menu.PROGRESS_BAR = self._progress_bar
        self._progress_bar.value = 67

        # buttons
        self._button_erd_reader = ControlButton('Wczytaj ERD')
        self._button_stage_1 = ControlButton('Etap 1')
        self._button_stage_2 = ControlButton('Etap 2')
        self._button_stage_3 = ControlButton('Etap 3')
        self._button_stage_4 = ControlButton('Etap 4')
        self._button_stage_5 = ControlButton('Etap 5')
        self._button_stage_6 = ControlButton('Etap 6')
        self._button_stage_7 = ControlButton('Etap 7')
        self._button_stage_8 = ControlButton('Etap 8')
        self._button_stage_9 = ControlButton('Etap 9')
        self._button_stage_10 = ControlButton('Etap 10')
        self._button_stage_11 = ControlButton('Etap 11')
        self._button_stage_12 = ControlButton('Etap 12')
        self._button_stage_13 = ControlButton('Etap 13')
        self._button_generate = ControlButton('GENERUJ!')

        # button's actions
        self._button_erd_reader.value = self.__button_initial_data_action
        self._button_stage_1.value = self.__button_stage_1_action
        self._button_stage_2.value = self.__button_stage_2_action
        self._button_stage_3.value = self.__button_stage_3_action
        self._button_stage_4.value = self.__button_stage_4_action
        self._button_stage_5.value = self.__button_stage_5_action
        self._button_stage_6.value = self.__button_stage_6_action
        self._button_stage_7.value = self.__button_stage_7_action
        self._button_stage_8.value = self.__button_stage_8_action
        self._button_stage_9.value = self.__button_stage_9_action
        self._button_stage_10.value = self.__button_stage_10_action
        self._button_stage_11.value = self.__button_stage_11_action
        self._button_stage_12.value = self.__button_stage_12_action
        self._button_stage_13.value = self.__button_stage_13_action
        self._button_generate.value = self.__button_generate_action

        self.formset = ['_button_erd_reader', '_progress_bar', ('_button_stage_1', '_button_stage_2', '_button_stage_3',
                                               '_button_stage_4', '_button_stage_5', '_button_stage_6',
                                               '_button_stage_7', '_button_stage_8', '_button_stage_9',
                                               '_button_stage_10', '_button_stage_11', '_button_stage_12',
                                               '_button_stage_13'), '_panel', '_button_generate']

        self.mainmenu = [
            {'Ustawienia': [
                {'Resetuj dane (widoczne przy następnym uruchomieniu)': self.__menu_reset_action},
                {'Wczytaj przykładowy projekt: ': self.__menu_load_project_action}
            ]}
        ]

        saver = Saver.get_saver()

        # logic
        self._project = saver.project
        self.erd = saver.erd
        self.transactions = saver.transactions
        self.rules = saver.rules
        self.users = saver.users
        self.perspectives = saver.perspectives

        self.populate_buttons()

    def populate_buttons(self):
        self._progress_bar.value = self._project.get_stage_count() / 13 * 100

        self._button_stage_1.label = 'Etap 1' if self._project.get_stage(1) is None else 'Etap 1 - Zrobiony'
        self._button_stage_2.label = 'Etap 2' if self._project.get_stage(2) is None else 'Etap 2 - Zrobiony'
        self._button_stage_3.label = 'Etap 3' if self._project.get_stage(3) is None else 'Etap 3 - Zrobiony'
        self._button_stage_4.label = 'Etap 4' if self._project.get_stage(4) is None else 'Etap 4 - Zrobiony'
        self._button_stage_5.label = 'Etap 5' if self._project.get_stage(5) is None else 'Etap 5 - Zrobiony'
        self._button_stage_6.label = 'Etap 6' if self._project.get_stage(6) is None else 'Etap 6 - Zrobiony'
        self._button_stage_7.label = 'Etap 7' if self._project.get_stage(7) is None else 'Etap 7 - Zrobiony'
        self._button_stage_8.label = 'Etap 8' if self._project.get_stage(8) is None else 'Etap 8 - Zrobiony'
        self._button_stage_9.label = 'Etap 9' if self._project.get_stage(9) is None else 'Etap 9 - Zrobiony'
        self._button_stage_10.label = 'Etap 10' if self._project.get_stage(10) is None else 'Etap 10 - Zrobiony'
        self._button_stage_11.label = 'Etap 11' if self._project.get_stage(11) is None else 'Etap 11 - Zrobiony'
        self._button_stage_12.label = 'Etap 12' if self._project.get_stage(12) is None else 'Etap 12 - Zrobiony'
        self._button_stage_13.label = 'Etap 13' if self._project.get_stage(13) is None else 'Etap 13 - Zrobiony'

    def __button_stage_1_action(self):
        self.populate_buttons()
        # switch windows
        win = Stage1Window(self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_2_action(self):
        self.populate_buttons()
        win = Stage2Window(self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_3_action(self):
        self.populate_buttons()
        win = Stage3Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_4_action(self):
        self.populate_buttons()
        win = Stage4Window(self.erd, self._project, self.rules)
        win.parent = self
        self._panel.value = win

    def __button_stage_5_action(self):
        self.populate_buttons()
        win = Stage5Window(self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_6_action(self):
        self.populate_buttons()
        win = Stage6Window(self.erd, self.transactions, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_7_action(self):
        self.populate_buttons()
        win = Stage7Window(self.erd, self._project, self.rules)
        win.parent = self
        self._panel.value = win

    def __button_stage_8_action(self):
        self.populate_buttons()
        win = Stage8Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_9_action(self):
        self.populate_buttons()
        win = Stage9Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_10_action(self):
        self.populate_buttons()
        win = Stage10Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_11_action(self):
        self.populate_buttons()
        win = Stage11Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_12_action(self):
        self.populate_buttons()
        win = Stage12Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_13_action(self):
        self.populate_buttons()
        pass

    def __button_initial_data_action(self):
        self.populate_buttons()
        win = InitialDataEditor(self.erd, self.transactions, self.users, self.perspectives, self.rules)
        win.parent = self
        win.show()

    def __button_generate_action(self):
        # preparations
        self.prepare_entities()
        self.prepare_rules()

        self._project.generate()

    def __menu_reset_action(self):
        from os import remove
        try:
            remove('save.pickle')
        except FileNotFoundError as e:
            print(e)

    def __menu_load_project_action(self):
        self.DEBUG_ACTUALL_PROJECT()

    # preparation functions, called right before generation, to assure proper order and numeration

    def prepare_rules(self):
        counter = 1
        for rule in self.rules:
            rule.id = counter
            counter += 1
        self.rules.sort(key=lambda rule: rule.id)

    def prepare_entities(self):
        counter = 1
        for entity in self.erd.entities:
            entity.id = counter
            counter += 1
        self.erd.entities.sort(key=lambda entity: entity.id)

    def prepare_relationships(self):
        counter = 1
        for relationship in self.erd.relationships:
            relationship.id = counter
            counter += 1
        self.erd.relationships.sort(key=lambda rel: rel.id)


    def DEBUG_ACTUALL_PROJECT(self):
        e1 = Entity('Arkusz', 'Arkusze', [Attribute('IdA', Types.INT, True, 'Unikalny identyfikator Arkusza nadawany automatycznie przez system, np. 1. '),
                                          Attribute('Ocena', Types.INT_POSITIVE, False, 'Ilość punktów zdobyta przez uczestnika konkursu wprowadzana przez sprawdzającego, np. 30.')])
        e2 = Entity('Pytanie', 'Pytania', [Attribute('IdP', Types.INT, True, ' Unikalny identyfikator Pytania nadawany automatycznie przez system, np. 4. '),
                                           Attribute('Pytanie', Types.STRING, False, 'Treść pytania, np. Co oznacza skrót FIFO?'),
                                           Attribute('Odpowiedź', Types.STRING, False,  '(ang. First in, First out) żądania są przetwarzane sekwencyjnie wg kolejki.')])
        e3 = Entity('Uczestnik', 'Uczestnicy', [Attribute('NrAlbumu', Types.INT, True, 'Unikalny identyfikator Uczestnika nadawany automatycznie przez system, np. 3. '),
                                                Attribute('Nazwisko', Types.STRING, False, 'Nazwisko uczestnika, np. Kowalski. '),
                                                Attribute('Imię', Types.STRING, False, 'Imię uczestnika, np. Adam. ')])
        e4 = Entity('Konkurs', 'Konkursy', [Attribute('IdK', Types.INT, True, 'Unikalny identyfikator Konkursu nadawany automatycznie przez system, np. 2. '),
                                            Attribute('Nazwa', Types.STRING, False, 'Nazwa konkursu, np.  Electron.'),
                                            Attribute('Data', Types.DATE, False, 'Data realizacji konkursu, np. 14/05/2018.')])
        e5 = Entity('Organizator', 'Organizatorzy', [Attribute('IdO', Types.INT, True, 'Unikalny identyfikator Organizatora nadawany automatycznie przez system, np. 6. '),
                                                     Attribute('Nazwisko', Types.STRING, False, 'Nazwisko organizatora, np. Szymański.'),
                                                     Attribute('Imię', Types.STRING, False, 'Imię organizatora, np. Dawid.')])
        e6 = Entity('Sprawdzający', 'Sprawdzający', [Attribute('IdS', Types.INT, True, 'Unikalny identyfikator Sprawdzającego nadawany automatycznie przez system, np. 5.'),
                                                     Attribute('Nazwisko', Types.STRING, False, 'Nazwisko sprawdzającego, np. Nowak.'),
                                                     Attribute('Imię', Types.STRING, False, 'Imię sprawdzającego, np. Mateusz')])
        e7 = Entity('PytanieNaArkuszu', 'PytaniaNaArkuszu', [Attribute('IdPnA', Types.INT, True, 'Unikalny identyfikator PytaniaNaArkuszu, np. 70.')], is_strong=True)

        self.erd.entities = [e1, e2, e3, e4, e5, e6, e7]

        r1 = Relationship('NależyDo', left_entity='Konkurs', left_quantity='1,1', right_entity='Arkusz', right_quantity='0,N')
        r2 = Relationship('Zawiera', left_entity='Arkusz', left_quantity='1,1', right_entity='PytanieNaArkuszu', right_quantity='0,N')
        r3 = Relationship('Uczestniczy', left_entity='Konkurs', left_quantity='1,1', right_entity='Uczestnik', right_quantity='0,N')
        r4 = Relationship('Wypełnia', left_entity='Arkusz', left_quantity='0,N', right_entity='Uczestnik', right_quantity='0,1')
        r5 = Relationship('Jest', left_entity='Pytanie', left_quantity='1,1', right_entity='PytanieNaArkuszu', right_quantity='0,N')
        r6 = Relationship('Tworzy', left_entity='Arkusz', left_quantity='0,N', right_entity='Organizator', right_quantity='1,1')
        r7 = Relationship('Sprawdza', left_entity='Sprawdzający', left_quantity='0,1', right_entity='Arkusz', right_quantity='0,N')

        self.erd.relationships = [r1, r2, r3, r4, r5, r6, r7]

    # TODO change the example, so it doesn't have any N-N relationships
    def DEBUG_FUNCTION(self):
        e1 = Entity('Karetka', 'Karetki', [Attribute('IdK', Types.INT, True), Attribute('Rejestracja', Types.STRING), Attribute('Dost', Types.STRING), Attribute('WaznoscPrzegl', Types.DATE)])
        e2 = Entity('Zgłoszenie', 'Zgłoszenia', [Attribute('IdZ', Types.INT, True), Attribute('AdresZ', Types.STRING), Attribute('PozycjaZ', Types.STRING), Attribute('OpisZ', Types.STRING), Attribute('Czas dod', Types.STRING)])
        e3 = Entity('Dyżur', 'Dyżury', [Attribute('IdD', Types.INT, True), Attribute('PoczDyz', Types.DATE), Attribute('KonDyz', Types.DATE), Attribute('PozycjaDyz', Types.STRING)])
        e4 = Entity('Szpital', 'Szpitale', [Attribute('IdS', Types.INT, True), Attribute('NazwaS', Types.STRING), Attribute('AdresS', Types.STRING), Attribute('PozycjaS', Types.STRING)])
        e5 = Entity('Pracownik medyczny', 'Pracownicy medyczni', [Attribute('IdPS', Types.INT, True), Attribute('ImiePM', Types.STRING), Attribute('NazwiskoPM', Types.STRING), Attribute('LoginPM', Types.STRING), Attribute('HasłoPM', Types.STRING), Attribute('EmailPM', Types.STRING), Attribute('AktywnyPM', Types.BOOL)])
        e6 = Entity('Poszkodowany', 'Poszkodowani', [Attribute('IdP', Types.INT, True), Attribute('OpisPoszk', Types.STRING)])
        e7 = Entity('ICD', 'Schorzenia', [Attribute('IdS', Types.STRING, True), Attribute('NazwaS', Types.STRING)])
        e8 = Entity('Dyspozytor', 'Dyspozytorzy', [Attribute('IdDys', Types.INT, True), Attribute('LoginDys', Types.STRING), Attribute('HasloDys', Types.STRING), Attribute('EmailDys', Types.STRING), Attribute('AktywnyDys', Types.BOOL), Attribute('JestAdminem', Types.BOOL)])
        e9 = Entity('Pracownik szpitala', 'Pracownicy szpitala', [Attribute('IdPS', Types.INT, True), Attribute('LoginPS', Types.STRING), Attribute('HasłoPS', Types.STRING), Attribute('EmailPS', Types.BOOL)])
        e10 = Entity('Rejestr', 'Rejestry', [Attribute('IdR', Types.INT, True), Attribute('JestKierowca', Types.BOOL)])
        e11 = Entity('Wezwanie', 'Wezwania', [Attribute('IdW', Types.INT, True), Attribute('DataWezw',Types.DATE)])
        e12 = Entity('Schorzenie', 'Schorzenia', [Attribute('IdSch', Types.INT, True), Attribute('Uwagi', Types.STRING)])

        self.erd.entities = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]

        for entity in self.erd.entities:
            for attribute in entity.attributes:
                attribute.description = 'Opis ' + attribute.name

        r1 = Relationship('Przydzielona', left_entity='Karetka', left_quantity='1,1', right_entity='Dyżur', right_quantity='0,N')
        r2 = Relationship('RejestrPracownika', left_entity='Pracownik medyczny', left_quantity='1,1', right_entity='Rejestr', right_quantity='0,N')
        r3 = Relationship('RejestrDyżuru', left_entity='Rejestr', left_quantity='0,N', right_entity='Dyżur', right_quantity='1,1')
        r4 = Relationship('Przydzielono', left_entity='Dyżur', left_quantity='0,N', right_entity='Zgłoszenie', right_quantity='0,N')
        r5 = Relationship('WezwanieDyzuru', left_entity='Wezwanie', left_quantity='0,N', right_entity='Dyżur', right_quantity='1,1')
        r6 = Relationship('Zgłasza', left_entity='Dyspozytor', left_quantity='1,1', right_entity='Zgłoszenie', right_quantity='0,N')
        r7 = Relationship('Dotyczy', left_entity='ICD', left_quantity='1,1', right_entity='Schorzenie', right_quantity='0,N')
        r8 = Relationship('KodSchorzenia', left_entity='ICD', left_quantity='1,1', right_entity='Schorzenie', right_quantity='0,N')
        r9 = Relationship('SchorzeniePoszkodowanego', left_entity='Poszkodowany', left_quantity='1,1', right_entity='Schorzenie', right_quantity='0,N')
        r10 = Relationship('Hospitalizowany', left_entity='Poszkodowany', left_quantity='0,N', right_entity='Szpital', right_quantity='0,1')
        r11 = Relationship('PracujeW', left_entity='Pracownik szpitala', left_quantity='0,N', right_entity='Szpital', right_quantity='1,1')

        self.erd.relationships = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11]


