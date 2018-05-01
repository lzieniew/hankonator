from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlList import ControlList

from generation import Stage10
from base import Saver, Attribute, Types, Entity, add_foreign_keys


class Stage10Window(BaseWidget):

    def __init__(self, erd, project):
        super(Stage10Window, self).__init__()
        self.set_margin(20)
        self.erd = erd
        self.project = project

        self._editor = ControlEmptyWidget()
        self._editor.value = ForeignKeysEditor(self.erd)

        self._save_button = ControlButton('Zapisz')
        self._save_button.value = self.__save_action

        self.formset = ['_editor', '_save_button']

        add_foreign_keys(self.erd)


    def __save_action(self):
        self.project.add_stage(Stage10(self.erd))
        Saver.get_saver().save()
        self.parent.populate_buttons()


class EntityCombo(ControlCombo):

    def __init__(self, entities):
        super(EntityCombo, self).__init__()

        self.entities = entities

        self.populate()

    def populate(self):
        for entity in self.entities:
            self.add_item(entity.name_singular, entity)

    def activated_event(self, index):
        super().activated_event(index)
        self.parent.entity = self.parent.erd.entities[index]
        self.parent.populate()


class ForeignKeysEditor(BaseWidget):

    def __init__(self, erd):
        super(ForeignKeysEditor, self).__init__()

        self.erd = erd

        if self.erd.entities:
            self.entity = self.erd.entities[0]
        else:
            self.entity = Entity('', '', [])

        self._keys_list = ControlList()
        self._entity_combo = EntityCombo(self.erd.entities)
        self._entity_combo.parent = self
        self._add_fk_button = ControlButton('Dodaj klucz obcy')
        self._edit_fk_button = ControlButton('Edytuj klucz obcy')
        self._remove_fk_button = ControlButton('Usuń klucz obcy')

        self._add_fk_button.value = self.__add_fk_action
        self._edit_fk_button.value = self.__edit_fk_action
        self._remove_fk_button.value = self.__remove_fk_action

        self._keys_list.readonly = True

        self.formset = ['Etap 10 - sprawdz automatycznie wygenerowane klucz obce i w razie potrzeby je popraw', ('Wyświetlam klucz obec dla encji: ', '_entity_combo'), '_keys_list', ('_add_fk_button', '_edit_fk_button', '_remove_fk_button')]

        self.populate()

    def populate(self):
        self._keys_list.clear()
        for attribute in self.entity.foreign_keys:
            self._keys_list += [attribute.name]

    def __add_fk_action(self):
        win = ForeignKeyEditor(self.erd)
        win.parent = self
        win.show()

    def __edit_fk_action(self):
        if self._entity_combo.current_index is not None and self._keys_list.selected_row_index is not None:
            win = ForeignKeyEditor(self.erd, self.erd.entities[self._entity_combo.current_index], self.entity.foreign_keys[self._keys_list.selected_row_index])
            win.parent = self
            win.show()

    def __remove_fk_action(self):
        if self._keys_list.selected_row_index is not None:
            del self.entity.foreign_keys[self._keys_list.selected_row_index]
            self.populate()


class ForeignKeyEditor(BaseWidget):

    def __init__(self, erd, entity=None, attribute=None):
        super(ForeignKeyEditor, self).__init__()

        self.erd = erd
        self.entity = entity
        self.attribute = attribute

        self._fk_entity_combo = EntityCombo(self.erd.entities)
        self._fk_entity_combo.parent = self
        self._save_button = ControlButton('Zapisz')
        self._save_button.value = self.__save_action

        self.populate()

        self.formset = ['_fk_entity_combo', '_save_button']

    def populate(self):
        if self.entity is not None:
            self._fk_entity_combo.value = self.entity

    def __save_action(self):
        key = self._fk_entity_combo.value.get_key()
        self.attribute.name = self._fk_entity_combo.value.get_key().name
        Saver.get_saver().save()
        self.parent.populate()
        self.close()

