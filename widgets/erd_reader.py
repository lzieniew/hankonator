import pyforms
import pickle

from pyforms.gui.controls.ControlCheckBox import ControlCheckBox
from pyforms.gui.controls.ControlList import ControlList

from base import Erd
from pyforms.gui.controls.ControlText import ControlText
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlCheckBoxList import ControlCheckBoxList
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlCombo import ControlCombo

from base import Entity, Attribute, Relationship, Types


# TODO add a new window that contains this erd reader, and also readers for things, like users, transactions etc.
# this window will be run from button, that now shows this ErdReader
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


class AttributeEditor(pyforms.BaseWidget):
    def __init__(self, attributes):
        super(AttributeEditor, self).__init__()
        self.set_margin(10)

        self.attributes = attributes

        self._name_edit_text = ControlText()
        self._type_combo = ControlCombo()
        self._description_edit_text = ControlText('Opis')
        self._is_key_checkbox = ControlCheckBox('Czy kluczowy')
        self._save_attribute_button = ControlButton('Zapisz')

        self._is_key_checkbox.value = False

        self._save_attribute_button.value = self.__add_attribute_action

        self.formset = [('Nazwa: ', '_name_edit_text'), ('Typ: ', '_type_combo'), '_description_edit_text', '_is_key_checkbox', '_save_attribute_button']

        self._type_combo.add_item(Types.INT.name, 'INT')
        self._type_combo.add_item(Types.INT_POSITIVE.name, 'INT_POSITIVE')
        self._type_combo.add_item(Types.INT_NEGATIVE.name, 'INT_NEGATIVE')
        self._type_combo.add_item(Types.DATE.name, 'DATE')
        self._type_combo.add_item(Types.STRING.name, 'STRING')


    def __add_attribute_action(self):
        self.attributes.append(Attribute(self._name_edit_text.value, self._type_combo.value))
        self.parent.populate()
        self.close()


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
        self._remove_attribute_button = ControlButton(u'Usuń atrybut')
        self._attributes_list = ControlList()
        self._save_entity_button = ControlButton(u'Zapisz')

        self._add_attribute_button.value = self.__add_attribute_button_action
        self._remove_attribute_button.value = self.__remove_attribute_action
        self._save_entity_button.value = self.__save_entity_button_action

        self._attributes_list.readonly = True

        self.formset = [(u'Nazwa encji (liczba pojedyńcza): ', '_entity_name_singular'),
                        (u'Nazwa encji (liczba mnoga):', '_entity_name_plural'),
                        ('Atrybuty: ', '_attributes_list' ,'_add_attribute_button', '_remove_attribute_button'),
                        '_save_entity_button']

        self.populate()

    def populate(self):
        self._attributes_list.clear()
        self._entity_name_singular.value = self.entity.name_singular
        self._entity_name_plural.value = self.entity.name_plural
        for attribute in self.entity.attributes:
            self._attributes_list += [attribute.name]

    def __add_attribute_button_action(self):
        self.entity.name_singular = self._entity_name_singular.value
        self.entity.name_plural = self._entity_name_plural.value
        editor = AttributeEditor(self.entity.attributes)
        editor.parent = self
        editor.show()

    def __remove_attribute_action(self):
        index = self._attributes_list.selected_row_index
        if index is not None:
            del self.entity.attributes[index]
            self.populate()

    def __save_entity_button_action(self):
        # TODO fix program crash when attributes_list is empty
        self.entity.name_singular = self._entity_name_singular.value
        self.entity.name_plural = self._entity_name_plural.value
        self.parent._populate()
        self.close()

        if self.erd.get_entity_by_name(self.entity.name_singular) is None:
            self.erd.entities.append(self.entity)
        self.parent._populate()
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
        self.relationship.name = self._relationship_name_edit_text.value
        self.relationship.left_entity = self._left_entity_combo.value
        self.relationship.left_quantity = self._left_multiplicity_combo.value
        self.relationship.right_entity = self._right_entity_combo.value
        self.relationship.right_quantity = self._right_multiplicity_combo.value

        if self.relationship not in self.erd.relationships:
            self.erd.relationships.append(self.relationship)
        self.parent._populate()
        self.close()