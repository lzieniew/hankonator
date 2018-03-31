import pyforms
import pickle

from pyforms.gui.controls.ControlList import ControlList

from base import Erd
from pyforms.gui.controls.ControlText import ControlText
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlCheckBoxList import ControlCheckBoxList
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlCombo import ControlCombo

from base import Entity, Attribute, Relationship, Domains


class ErdReader(pyforms.BaseWidget):

    def __init__(self, menu):
        super(ErdReader, self,).__init__('ERD reader')
        self.set_margin(20)

        self.erd = menu.erd
        self.menu = menu

        self._entity_list = ControlList('Encje',
                                        plusFunction = self.__add_entity_action,
                                        minusFunction = self.__remove_entity_action)

        self._relationship_list = ControlList('Związki',
                                              plusFunction = self.__add_relationship_action,
                                              minusFunction = self.__remove_relationship_action)

        self._entity_editor = ControlEmptyWidget()
        self._relationship_editor = ControlEmptyWidget()

        self._add_entity_button = ControlButton(u'Dodaj encję')
        self._remove_entity_button = ControlButton(u'Usuń encję')
        self._add_relationship_button = ControlButton(u'Dodaj związek')
        self._remove_relationship_button = ControlButton(u'Usuń związek')

        self._add_entity_button.value = self.__add_entity_action
        self._add_relationship_button.value = self.__add_relationship_action
        self._remove_entity_button.value = self.__remove_entity_action
        self._remove_relationship_button.value = self.__remove_relationship_action

        self.formset = ['_entity_list',
                        ('_add_entity_button', '_remove_entity_button'),
                        '_entity_editor',
                        '_relationship_list',
                        ('_add_relationship_button', '_remove_relationship_button'),
                        '_relationship_editor',]

        self._entity_list.readonly = True
        self._relationship_list.readonly = True

        self._populate()

    def _populate(self):
        self._entity_list.clear()
        self._relationship_list.clear()
        for entity in self.erd.entities:
            self._entity_list += [repr(entity)]
        for relationship in self.erd.relationships:
            self._relationship_list += [repr(relationship)]

    def __add_entity_action(self):
        entity_editor_win = EntityEditor(self.erd)
        entity_editor_win.parent = self
        entity_editor_win.show()

    def __remove_entity_action(self):
        indexes = self._entity_list.selected_rows_indexes
        indexes.sort(reverse=True)
        for index in indexes:
            self.erd.remove_entity(index)
        self._populate()

    def __add_relationship_action(self):
        relationship_editor_win = RelationshipEditor(self.erd)
        relationship_editor_win.parent = self
        relationship_editor_win.show()

    def __remove_relationship_action(self):
        indexes = self._relationship_list.selected_rows_indexes
        indexes.sort(reverse=True)
        for index in indexes:
            self.erd.remove_relationship(index)
        self._populate()


class AttributeEditor(pyforms.BaseWidget):
    def __init__(self, attributes, label_list):
        super(AttributeEditor, self).__init__()
        self.set_margin(10)

        self.attributes = attributes
        self.label_list = label_list

        self._name_edit_text = ControlText()
        self._type_combo = ControlCombo()
        self._save_attribute_button = ControlButton('Zapisz')

        self._save_attribute_button.value = self.__add_attribute_action

        self.formset = [('Nazwa: ', '_name_edit_text'), ('Typ: ', '_type_combo'), '_save_attribute_button']


        self._type_combo.add_item(Domains.INT.name, 'INT')
        self._type_combo.add_item(Domains.INT_POSITIVE.name, 'INT_POSITIVE')
        self._type_combo.add_item(Domains.INT_NEGATIVE.name, 'INT_NEGATIVE')
        self._type_combo.add_item(Domains.DATE.name, 'DATE')
        self._type_combo.add_item(Domains.STRING.name, 'STRING')


    def __add_attribute_action(self):
        self.attributes.append(Attribute(self._name_edit_text.value, self._type_combo.value))
        self.label_list.value = str(self.attributes)
        self.close()


class EntityEditor(pyforms.BaseWidget):

    def __init__(self, erd):
        super(EntityEditor, self).__init__()
        self.set_margin(10)

        self.erd = erd

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
        self.erd.entities.append(Entity(self._entity_name_singular.value, self._entity_name_plural, attr_list))
        self.erd.save()
        # self._entity_name_singular.value = ''
        # self._entity_name_plural.value = ''
        # self._attributes_list.value = ''
        self.parent._populate()
        self.close()

class RelationshipEditor(pyforms.BaseWidget):

    def __init__(self, erd):
        super(RelationshipEditor, self).__init__()
        self.set_margin(10)
        self.erd = erd

        self._left_entity_combo = ControlCombo()
        self._left_multiplicity_combo = ControlCombo()
        self._relationship_name_edit_text = ControlText()
        self._right_multiplicity_combo = ControlCombo()
        self._right_entity_combo = ControlCombo()
        self._save_button = ControlButton(u'Zapisz związek')

        self._save_button.value = self.__save_relationship_action

        for entity in erd.entities:
            self._left_entity_combo.add_item(entity.name_singular)
            self._right_entity_combo.add_item(entity.name_singular)
        multiplicities = ['0..1', '1..1', '0..N', '1..N']
        for mul in multiplicities:
            self._left_multiplicity_combo.add_item(mul)
            self._right_multiplicity_combo.add_item(mul)

        self.formset = [('_left_entity_combo', '_left_multiplicity_combo', '_relationship_name_edit_text', '_right_multiplicity_combo', '_right_entity_combo'),
                        '_save_button']


    def __save_relationship_action(self):
        relationship = Relationship(name=self._relationship_name_edit_text.value, left_entity=self._left_entity_combo.value,
                                           left_quantity=self._left_multiplicity_combo.value, right_quantity=self._left_multiplicity_combo.value,
                                           right_entity=self._right_entity_combo.value)
        self.erd.relationships.append(relationship)
        self.erd.save()
        self.parent._populate()
        self.close()