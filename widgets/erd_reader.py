import pyforms
import pickle
from base import Erd
from pyforms.gui.controls.ControlText import ControlText
from pyforms.gui.controls.ControlToolBox import ControlToolBox
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlCheckBoxList import ControlCheckBoxList

from base import Entity, Attribute, Relationship


class ErdReader(pyforms.BaseWidget):

    def __init__(self, menu):
        super(ErdReader, self).__init__('ERD reader')

        self.erd = Erd()
        self.menu = menu

        self._entity_list = ControlList()
        self._relationship_list = ControlList()

        self._entity_editor = ControlEmptyWidget()
        self._relationship_editor = ControlEmptyWidget()

        self._add_entity_button = ControlButton(u'Dodaj encję')
        self._remove_entity_button = ControlButton(u'Usuń encję')
        self._add_relationship_button = ControlButton(u'Dodaj związek')
        self._save_erd_button = ControlButton('Zapisz diagram ERD')

        self._add_entity_button.value = self.__add_entity_action
        self._add_relationship_button.value = self.__add_relationship_action
        self._remove_entity_button.value = self.__remove_entity_action
        self._save_erd_button.value = self.__save_erd_action

        self.formset = ['_entity_list',
                        ('_add_entity_button', '_remove_entity_button'),
                        '_entity_editor',
                        '_relationship_list',
                        '_add_relationship_button',
                        '_relationship_editor',
                        '_save_erd_button']

        self._entity_list.readonly = True
        self._relationship_editor.readonly = True

    def __add_entity_action(self):
        entity_editor_win = EntityEditor(self.erd.entities, self._entity_list)
        entity_editor_win.parent = self
        self._entity_editor.value = entity_editor_win

    def __add_relationship_action(self):
        relationship_editor_win = EntityEditor(self.erd.entities)
        relationship_editor_win.parent = self
        self._relationship_editor.value = relationship_editor_win

    def __save_erd_action(self):
        self.menu._erd = self.erd

    def __remove_entity_action(self):
        win = RemoveEntityWindow(self.erd.entities, self._entity_list)
        win.show()




class AttributeEditor(pyforms.BaseWidget):

    def __init__(self, attributes, label_list):
        super(AttributeEditor, self).__init__()

        self.attributes = attributes
        self.label_list = label_list

        self._name_edit_text = ControlText()
        self._type_edit_text = ControlText()
        self._save_attribute_button = ControlButton('Zapisz')

        self._save_attribute_button.value = self.__add_attribute_action

        self.formset = [('Nazwa: ', '_name_edit_text'), ('Typ: ', '_type_edit_text'), '_save_attribute_button']


    def __add_attribute_action(self):
        self.attributes.append(Attribute(self._name_edit_text.value, self._type_edit_text.value))
        self.label_list.value = str(self.attributes)
        self.close()


class EntityEditor(pyforms.BaseWidget):

    def __init__(self, entities, entities_list):
        super(EntityEditor, self).__init__()

        self.entities = entities
        self.entities_list = entities_list

        self._entity_name_singular = ControlText()
        self._entity_name_plural = ControlText()
        self._add_attribute_button = ControlButton(u'Dodaj atrybut')
        self._attributes_list = ControlLabel()
        self._save_entity_button = ControlButton(u'Zapisz encję')

        self._add_attribute_button.value = self.__add_attribute_button_action
        self._save_entity_button.value = self.__save_entity_button_action

        self.formset = [(u'Nazwa encji (liczba pojedyńcza): ', '_entity_name_singular'),
                        (u'Nazwa encji (liczba mnoga):', '_entity_name_plural'),
                        ('Atrybuty: ', '_attributes_list' ,'_add_attribute_button'),
                        '_save_entity_button']

        self.attributes = []


    def __add_attribute_button_action(self):
        editor = AttributeEditor(self.attributes, self._attributes_list)
        editor.show()

    def __save_entity_button_action(self):
        # TODO fix program crash when attributes_list is empty
        attr_list = self._attributes_list.value[1:-1].split(',')
        self.entities.append(Entity(self._entity_name_singular.value, self._entity_name_plural, attr_list))
        self.entities_list += [self._entity_name_singular.value]
        self._entity_name_singular.value = ''
        self._entity_name_plural.value = ''
        self._attributes_list.value = ''

class RemoveEntityWindow(pyforms.BaseWidget):

    def __init__(self, entities, entity_list):
        super(RemoveEntityWindow, self).__init__(u'Encje do usunięcia:')

        self._entities_to_remove_checkbox = ControlCheckBoxList()
        self._remove_button = ControlButton(u'Usuń zaznaczone')

        for entity in entities:
            self._entities_to_remove_checkbox.__add__((repr(entity), False))

