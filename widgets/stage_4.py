from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlList import ControlList

from generation import Stage4
from base import Rule

class CustomEntityCombo(ControlCombo):

    def __init__(self, entities):
        super(CustomEntityCombo, self).__init__()
        self.entities = entities

        filter_lambda = lambda x: not x.is_associative

        for entity in list(filter(filter_lambda, entities)):
            self.add_item(entity.name_singular, value=entity)

    def activated_event(self, index):
        self.parent.populate()



class Stage4Window(BaseWidget):
    def __init__(self, erd, project, rules):
        super(Stage4Window, self).__init__('Etap 4')
        self.set_margin(20)

        self._entities_combo = CustomEntityCombo(erd.entities)
        self._rules_list = ControlList()
        self._fix_button = ControlButton('Popraw regułę')
        self._save_button = ControlButton('Zapisz etap 4')

        self.erd = erd
        self._project = project
        self.rules = rules

        self.rules_dict = {}

        self._save_button.value = self.__save_action
        self._rules_list.readonly = True
        self._entities_combo.parent = self

        self.formset = ['_entities_combo', ('_rules_list', '_fix_button'), '_save_button']

        if not rules:
            self.populate_rules()

        self.populate()


    def populate_rules(self):
        filtered_entities = list(filter(lambda x: not x.is_associative, self.erd.entities))
        for entity in filtered_entities:
            self.rules_dict[entity.name_singular] = []
            relationships = self.erd.get_relationships_connected_wit_entity(entity.name_singular)
            for rel in relationships:
                this_entity_name = entity.name_singular
                other_entity_name = rel.get_other_entity_name(entity.name_singular)
                if rel.get_other_ends_multiplicity(this_entity_name)[0] == '0':
                    rule = Rule(this_entity_name + u' nie musi być powiązany z żadnym ' + other_entity_name + '\n', this_entity_name, other_entity_name)
                    self.rules_dict[this_entity_name].append(rule)
                    self.rules.append(rule)
                elif rel.get_other_ends_multiplicity(entity.name_singular)[0] == '1':
                    rule = Rule(this_entity_name + u' musi być powiązany z przynajmniej jednym ' + other_entity_name + '\n', this_entity_name, other_entity_name)
                    self.rules_dict[this_entity_name].append(rule)
                    self.rules.append(rule)

                if rel.get_other_ends_multiplicity(entity.name_singular)[-1] == '1':
                    rule = Rule(this_entity_name + u' jest powiązany z maksymalnie jednym ' + other_entity_name + '\n', this_entity_name, other_entity_name)
                    self.rules_dict[this_entity_name].append(rule)
                    self.rules.append(rule)
                elif rel.get_other_ends_multiplicity(entity.name_singular)[-1] == 'N':
                    rule = Rule(this_entity_name + u' może być powiązany z wieloma ' + other_entity_name + '\n', this_entity_name, other_entity_name)
                    self.rules_dict[this_entity_name].append(rule)
                    self.rules.append(rule)

    def populate(self):
        self._rules_list.clear()
        curr_entity = self._entities_combo.value.name_singular
        filtered_rules = list(filter(lambda x: curr_entity == x.left_entity_name or curr_entity == x.right_entity_name, self.rules))
        for rule in filtered_rules:
            self._rules_list += [rule.content]


    def __fix_action(self):
        pass

    def __add_rule_action(self):
        pass

    def __remove_rule_action(self):
        pass


    def __save_action(self):
        self._project.stages.append(Stage4(self.erd, self.rules))
