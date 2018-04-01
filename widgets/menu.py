import pyforms
from pyforms.controls import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from generation import Project
from .erd_reader import ErdReader

from .stage_1 import Stage1Window
from .stage_2 import Stage2Window
from .stage_3 import Stage3Window
from .stage_4 import Stage4Window
from .stage_6 import Stage6Window
from .stage_7 import Stage7Window
from .stage_8 import Stage8Window

from base import Stage1, Stage2, Erd, Entity, Attribute, Relationship, Stage8, Types


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
        self._button_generate = ControlButton('GENERATE!')

        # button's actions
        self._button_erd_reader.value = self.__button_erd_action
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

        try:
            self.erd = Erd.load()
        except:
            self.erd = Erd()

        # Waring, erd object is created only for testing purposes
        self.erd = Erd()
        # e1 = Entity('Arkusz', 'Arkusze', [Attribute('id', 'int'), Attribute('data', 'date')])
        # e2 = Entity('Użytkownik', 'Użytkownicy', [Attribute('Imię', 'string'), Attribute('Nazwisko', 'string'), Attribute('id', 'int')])
        # e3 = Entity('Organizator', 'Organizatorzy', [Attribute('Imię', 'string'), Attribute('Nazwisko', 'string'), Attribute('id', 'int')])
        # self.erd.entities = [e1, e2, e3]
        # r1 = Relationship(left_entity='Arkusz', left_quantity='0,N', name='Przydzielony', right_quantity='0,1', right_entity='Użytkownik')
        # self.erd.relationships = [r1]
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
        win = Stage4Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_5_action(self):
        pass

    def __button_stage_6_action(self):
        win = Stage6Window(self.erd, self.transactions, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_7_action(self):
        win = Stage7Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_8_action(self):
        win = Stage8Window(self.erd, self._project)
        win.parent = self
        self._panel.value = win

    def __button_stage_9_action(self):
        pass

    def __button_stage_10_action(self):
        pass

    def __button_stage_11_action(self):
        pass

    def __button_stage_12_action(self):
        pass

    def __button_stage_13_action(self):
        pass

    def __button_erd_action(self):
        win = ErdReader(self)
        win.parent = self
        self._panel.value = win

    def __button_generate_action(self):
        self._project.generate()

    def DEBUG_FUNCTION(self):
        e1 = Entity('Karetka', 'Karetki', [Attribute('IdK', Types.INT), Attribute('Rejestracja', Types.STRING), Attribute('Dost', Types.STRING), Attribute('WaznoscPrzegl', Types.DATE)])
        e2 = Entity('Zgłoszenie', 'Zgłoszenia', [Attribute('IdZ', Types.INT), Attribute('AdresZ', Types.STRING), Attribute('PozycjaZ', Types.STRING), Attribute('OpisZ', Types.STRING), Attribute('Czas dod', Types.STRING)])
        e3 = Entity('Dyżur', 'Dyżury', [Attribute('IdD', Types.INT), Attribute('PoczDyz', Types.DATE), Attribute('KonDyz', Types.DATE), Attribute('PozycjaDyz', Types.STRING)])
        e4 = Entity('Szpital', 'Szpitale', [Attribute('IdS', Types.INT), Attribute('NazwaS', Types.STRING), Attribute('AdresS', Types.STRING), Attribute('PozycjaS', Types.STRING)])
        e5 = Entity('Pracownik medyczny', 'Pracownicy medyczni', [Attribute('IdPS', Types.INT), Attribute('ImiePM', Types.STRING), Attribute('NazwiskoPM', Types.STRING), Attribute('LoginPM', Types.STRING), Attribute('HasłoPM', Types.STRING), Attribute('EmailPM', Types.STRING), Attribute('AktywnyPM', Types.BOOL)])
        e6 = Entity('Poszkodowany', 'Poszkodowani', [Attribute('IdP', Types.INT), Attribute('OpisPoszk', Types.STRING)])
        e7 = Entity('Schorzenie', 'Schorzenia', [Attribute('IdS', Types.STRING), Attribute('NazwaS', Types.STRING)])
        e8 = Entity('Dyspozytor', 'Dyspozytorzy', [Attribute('IdDys', Types.INT), Attribute('LoginDys', Types.STRING), Attribute('HasloDys', Types.STRING), Attribute('EmailDys', Types.STRING), Attribute('AktywnyDys', Types.BOOL), Attribute('JestAdminem', Types.BOOL)])
        e9 = Entity('Pracownik szpitala', 'Pracownicy szpitala', [Attribute('IdPS', Types.INT), Attribute('LoginPS', Types.STRING), Attribute('HasłoPS', Types.STRING), Attribute('EmailPS', Types.BOOL)])

        self.erd.entities = [e1,e2,e3,e4,e5,e6,e7,e8,e9]


