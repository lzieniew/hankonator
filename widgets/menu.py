import pyforms
from pyforms.controls import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from generation import Project
from .initial_data_editor import InitialDataEditor

from .stage_1 import Stage1Window
from .stage_2 import Stage2Window
from .stage_3 import Stage3Window
from .stage_4 import Stage4Window
from .stage_6 import Stage6Window
from .stage_7 import Stage7Window
from .stage_8 import Stage8Window
from .stage_10 import Stage10Window
from .stage_11 import Stage11Window
from .stage_12 import Stage12Window

from base import Erd, Entity, Attribute, Relationship, Types


class Menu(pyforms.BaseWidget):
    def __init__(self):
        super(Menu, self).__init__('Hankonator MENU')
        self.set_margin(30)

        self._panel = ControlEmptyWidget()

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

        self.formset = ['_button_erd_reader', ('_button_stage_1', '_button_stage_2', '_button_stage_3',
                                               '_button_stage_4', '_button_stage_5', '_button_stage_6',
                                               '_button_stage_7', '_button_stage_8', '_button_stage_9',
                                               '_button_stage_10', '_button_stage_11', '_button_stage_12',
                                               '_button_stage_13'), '_panel', '_button_generate']

        # logic
        self._project = Project([])
        self.erd = None
        self.transactions = []
        self.rules = []
        self.users = []

        try:
            self.erd = Erd.load()
        except:
            self.erd = Erd()

        # Warning, erd object is created only for testing purposes
        self.erd = Erd()
        self.DEBUG_FUNCTION()


    def __button_stage_1_action(self):
        # switch windows
        win = Stage1Window(self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_2_action(self):
        win = Stage2Window(self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_3_action(self):
        win = Stage3Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_4_action(self):
        win = Stage4Window(self.erd, self._project, self.rules)
        win.parent = self
        self._panel.value = win

    def __button_stage_5_action(self):
        pass

    def __button_stage_6_action(self):
        win = Stage6Window(self.erd, self.transactions, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_7_action(self):
        win = Stage7Window(self.erd, self._project, self.rules)
        win.parent = self
        self._panel.value = win

    def __button_stage_8_action(self):
        win = Stage8Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_9_action(self):
        pass

    def __button_stage_10_action(self):
        win = Stage10Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_11_action(self):
        win = Stage11Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_12_action(self):
        win = Stage12Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_13_action(self):
        pass

    def __button_initial_data_action(self):
        win = InitialDataEditor(self.erd, self.transactions, self.users)
        win.parent = self
        win.show()

    def __button_generate_action(self):
        self._project.generate()

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


        self.erd.entities = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]

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

        self.erd.relationships = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11]


