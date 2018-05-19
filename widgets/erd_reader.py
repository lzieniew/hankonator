import pyforms
import pickle

from pyforms.gui.controls.ControlCheckBox import ControlCheckBox
from pyforms.gui.controls.ControlList import ControlList

from base import Erd, Saver
from pyforms.gui.controls.ControlText import ControlText
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlCheckBoxList import ControlCheckBoxList
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlCombo import ControlCombo

from base import Entity, Attribute, Relationship, Types

from .popup import Popup


class ErdReader(pyforms.BaseWidget):

    def __init__(self, erd):
        super(ErdReader, self,).__init__('ERD reader')
        self.set_margin(20)

        self.erd = erd

        self._entity_list = ControlList('Encje', "1")

        self._relationship_list = ControlList('Związki', '1')

        self._entity_editor = ControlEmptyWidget()
        self._relationship_editor = ControlEmptyWidget()

        self._add_entity_button = ControlButton(u'Dodaj encję')
        self._edit_entity_button = ControlButton(u'Edytuj encję')
        self._remove_entity_button = ControlButton(u'Usuń encję')
        self._add_relationship_button = ControlButton(u'Dodaj związek')
        self._edit_relationship_button = ControlButton(u'Edytuj związek')
        self._remove_relationship_button = ControlButton(u'Usuń związek')

        self._add_entity_button.value = self.__add_entity_action
        self._add_relationship_button.value = self.__add_relationship_action
        self._edit_entity_button.value = self.__edit_entity_action
        self._edit_relationship_button.value = self.__edit_relationship_action
        self._remove_entity_button.value = self.__remove_entity_action
        self._remove_relationship_button.value = self.__remove_relationship_action

        self.formset = ['_entity_list',
                        ('_add_entity_button', '_edit_entity_button', '_remove_entity_button'),
                        '_entity_editor',
                        '_relationship_list',
                        ('_add_relationship_button', '_edit_relationship_button', '_remove_relationship_button'),
                        '_relationship_editor',]

        self._entity_list.readonly = True
        self._entity_list.select_entire_row = True
        self._relationship_list.readonly = True
        self._relationship_list.select_entire_row = True

        self._populate()

    def _populate(self):
        self._entity_list.clear()
        self._relationship_list.clear()
        for entity in self.erd.entities:
            self._entity_list += [entity.name_singular, repr(entity)]
        for relationship in self.erd.relationships:
            self._relationship_list += [relationship.name, repr(relationship)]

    def __add_entity_action(self):
        entity_editor_win = EntityEditor(self.erd)
        entity_editor_win.parent = self
        entity_editor_win.show()

    def __edit_entity_action(self):
        if self._entity_list.selected_row_index is not None:
            index = self._entity_list.selected_row_index
            entity = self._entity_list.get_value(row=index, column=0)
            entity_editor_win = EntityEditor(self.erd, entity)
            entity_editor_win.parent = self
            entity_editor_win.show()

    def __remove_entity_action(self):
        indexes = self._entity_list.selected_rows_indexes
        indexes.sort(reverse=True)
        for index in indexes:
            self.erd.remove_entity(index)
        self._populate()
        Saver.get_saver().save()

    def __add_relationship_action(self):
        relationship_editor_win = RelationshipEditor(self.erd)
        relationship_editor_win.parent = self
        relationship_editor_win.show()

    def __edit_relationship_action(self):
        if self._relationship_list.selected_row_index is not None:
            index = self._relationship_list.selected_row_index
            relationship = self.erd.get_relationship_by_name(self._relationship_list.get_value(row=index, column=0))
            win = RelationshipEditor(self.erd, relationship)
            win.parent = self
            win.show()

    def __remove_relationship_action(self):
        indexes = self._relationship_list.selected_rows_indexes
        indexes.sort(reverse=True)
        for index in indexes:
            self.erd.remove_relationship(index)
        self._populate()
        Saver.get_saver().save()


class AttributeEditor(pyforms.BaseWidget):
    def __init__(self, attributes, attribute=None):
        super(AttributeEditor, self).__init__()
        self.set_margin(10)

        self.attributes = attributes
        self.attribute = attribute

        self._name_edit_text = ControlText()
        self._type_combo = ControlCombo()
        self._description_edit_text = ControlText('Opis')
        self._is_key_checkbox = ControlCheckBox('Czy kluczowy')
        self._is_obligatory_checkbox = ControlCheckBox(u'Atrybut obligatoryjny (brak zaznaczenia - opcjonalny)')
        self._is_unique_checkbox = IsUniqueCheckBox(self._is_key_checkbox)
        self._save_attribute_button = ControlButton('Zapisz')

        self._save_attribute_button.value = self.__save_attribute_action

        self.formset = [('Nazwa: ', '_name_edit_text'), ('Typ: ', '_type_combo'), '_description_edit_text', '_is_key_checkbox', '_is_obligatory_checkbox', '_is_unique_checkbox', '_save_attribute_button']

        self._type_combo.add_item(Types.INT_POSITIVE.name, Types.INT_POSITIVE)
        self._type_combo.add_item(Types.INT.name, Types.INT)
        self._type_combo.add_item(Types.INT_NEGATIVE.name, Types.INT_NEGATIVE)
        self._type_combo.add_item(Types.DATE.name, Types.DATE)
        self._type_combo.add_item(Types.STRING.name, Types.STRING)
        self._type_combo.add_item(Types.REAL.name, Types.REAL)
        self._type_combo.add_item(Types.REAL_POSITIVE.name, Types.REAL_POSITIVE)
        self._type_combo.add_item(Types.REAL_NEGATIVE.name, Types.REAL_NEGATIVE)
        self._type_combo.add_item(Types.REAL_0_1.name, Types.REAL_0_1)

        self.populate()

    def populate(self):
        if self.attribute is not None:
            self._name_edit_text.value = self.attribute.name
            self._type_combo.value = self.attribute.type
            self._description_edit_text.value = self.attribute.description
            self._is_key_checkbox.value = self.attribute.is_key
            self._is_obligatory_checkbox.value = self.attribute.is_obligatory
            self._is_unique_checkbox.value = self.attribute.unique
        else:
            self.attribute = Attribute('', '')

    def __save_attribute_action(self):
        if self._name_edit_text.value == '':
            popup = Popup('Nazwa atrybutu nie może być pusta')
            popup.show()
        else:
            self.attribute.name = self._name_edit_text.value
            self.attribute.type = self._type_combo.value
            self.attribute.description = self._description_edit_text.value
            self.attribute.is_key = self._is_key_checkbox.value
            self.attribute.is_obligatory = self._is_obligatory_checkbox.value
            self.attribute.unique = self._is_unique_checkbox.value or self._is_key_checkbox.value

            if self.attribute not in self.attributes:
                self.attributes.append(self.attribute)
            self.parent.populate()
            Saver.get_saver().save()
            self.close()


class IsUniqueCheckBox(ControlCheckBox):

    def __init__(self, is_key_checkbox):
        super(IsUniqueCheckBox, self).__init__('Unikalny')
        self.is_key_checkbox = is_key_checkbox

    def changed_event(self):
        if self.value:
            self.is_key_checkbox.value = True
        return super().changed_event()


class EntityEditor(pyforms.BaseWidget):

    def __init__(self, erd, entity=None):
        super(EntityEditor, self).__init__()
        self.set_margin(10)

        self.erd = erd
        if entity is not None:
            self.entity = self.erd.get_entity_by_name(entity)
        else:
            self.entity = Entity('', '', [])

        self._entity_name_singular = ControlText()
        self._entity_name_plural = ControlText()
        self._add_attribute_button = ControlButton(u'Dodaj atrybut')
        self._edit_attribute_button = ControlButton(u'Edytuj atrybut')
        self._remove_attribute_button = ControlButton(u'Usuń atrybut')
        self._attributes_list = ControlList()
        self._description_edit_text = ControlText()
        self._is_strong_checkbox = ControlCheckBox(u'Jest silna (brak zaznaczenia - słaba)')
        self._save_entity_button = ControlButton(u'Zapisz')

        self._add_attribute_button.value = self.__add_attribute_button_action
        self._edit_attribute_button.value = self.__edit_attribute_button_action
        self._remove_attribute_button.value = self.__remove_attribute_action
        self._save_entity_button.value = self.__save_entity_button_action

        self._attributes_list.readonly = True

        self.formset = [(u'Nazwa encji (liczba pojedyńcza): ', '_entity_name_singular'),
                        (u'Nazwa encji (liczba mnoga):', '_entity_name_plural'),
                        ('Opis encji: ', '_description_edit_text'),
                        ('Atrybuty: ', '_attributes_list', '_add_attribute_button', '_edit_attribute_button', '_remove_attribute_button'),
                        '_is_strong_checkbox',
                        '_save_entity_button']

        self.populate()

    def populate(self):
        self._attributes_list.clear()
        self._entity_name_singular.value = self.entity.name_singular
        self._entity_name_plural.value = self.entity.name_plural
        self._description_edit_text.value = self.entity.description
        self._is_strong_checkbox.value = self.entity.is_strong
        for attribute in self.entity.attributes:
            self._attributes_list += [attribute.name]

    def __add_attribute_button_action(self):
        self.entity.name_singular = self._entity_name_singular.value
        self.entity.name_plural = self._entity_name_plural.value
        self.entity.description = self._description_edit_text.value
        self.entity.is_strong = self._is_strong_checkbox.value
        editor = AttributeEditor(self.entity.attributes)
        editor.parent = self
        editor.show()

    def __edit_attribute_button_action(self):
        self.entity.name_singular = self._entity_name_singular.value
        self.entity.name_plural = self._entity_name_plural.value
        self.entity.description = self._description_edit_text.value
        self.entity.is_strong = self._is_strong_checkbox.value
        if self._attributes_list.selected_row_index is not None:
            win = AttributeEditor(self.entity.attributes, self.entity.attributes[self._attributes_list.selected_row_index])
            win.parent = self
            win.show()

    def __remove_attribute_action(self):
        index = self._attributes_list.selected_row_index
        if index is not None:
            del self.entity.attributes[index]
            self.populate()

    def __save_entity_button_action(self):
        # TODO fix program crash when attributes_list is empty
        if self._entity_name_plural.value == '' or self._entity_name_plural.value == '':
            popup = Popup('Nazwy encji nie mogą być puste')
            popup.show()
        else:
            self.entity.name_singular = self._entity_name_singular.value
            self.entity.name_plural = self._entity_name_plural.value
            self.entity.description = self._description_edit_text.value
            self.entity.is_strong = self._is_strong_checkbox.value

            if self.erd.get_entity_by_name(self.entity.name_singular) is None:
                self.erd.entities.append(self.entity)
            self.parent._populate()
            Saver.get_saver().save()
            self.close()


class RelationshipEditor(pyforms.BaseWidget):

    def __init__(self, erd, relationship=None):
        super(RelationshipEditor, self).__init__()
        self.set_margin(10)
        self.erd = erd

        self._left_entity_combo = ControlCombo()
        self._left_multiplicity_combo = ControlCombo()
        self._relationship_name_edit_text = ControlText()
        self._right_multiplicity_combo = ControlCombo()
        self._right_entity_combo = ControlCombo()
        self._save_button = ControlButton(u'Zapisz')

        self._save_button.value = self.__save_relationship_action

        for entity in erd.entities:
            self._left_entity_combo.add_item(entity.name_singular)
            self._right_entity_combo.add_item(entity.name_singular)
        multiplicities = ['0,1', '1,1', '0,N', '1,N']
        for mul in multiplicities:
            self._left_multiplicity_combo.add_item(mul)
            self._right_multiplicity_combo.add_item(mul)

        self.formset = [('_left_entity_combo', '_left_multiplicity_combo', '_relationship_name_edit_text', '_right_multiplicity_combo', '_right_entity_combo'),
                        '_save_button']

        if relationship is not None:
            self.relationship = relationship
        else:
            self.relationship = Relationship('', '', '', '', '')

        self.populate()

    def populate(self):
        self._left_entity_combo.value = self.relationship.left_entity
        self._left_multiplicity_combo.value = self.relationship.left_quantity
        self._relationship_name_edit_text.value = self.relationship.name
        self._right_entity_combo.value = self.relationship.right_entity
        self._right_multiplicity_combo.value = self.relationship.right_quantity

    def __save_relationship_action(self):
        if self._relationship_name_edit_text.value == '':
            popup = Popup('Nazwa związku nie może być pusta')
            popup.show()
        else:
            self.relationship.name = self._relationship_name_edit_text.value
            self.relationship.left_entity = self._left_entity_combo.value
            self.relationship.left_quantity = self._left_multiplicity_combo.value
            self.relationship.right_entity = self._right_entity_combo.value
            self.relationship.right_quantity = self._right_multiplicity_combo.value

            if self.relationship not in self.erd.relationships:
                self.erd.relationships.append(self.relationship)
            self.parent._populate()
            Saver.get_saver().save()
            self.close()