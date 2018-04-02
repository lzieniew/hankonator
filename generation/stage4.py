from docx.shared import Pt


from generation import Project
from base.rule import Rule


class Stage4:

    def __init__(self, erd, rules):
        self.erd = erd
        self.rules = rules

        self.rules_dict = {}

        self.populate_rules()

    def populate_rules(self):
        for entity in self.erd.entities:
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

    def build(self, document):

        header = document.add_paragraph()
        header.add_run('4. Reguły funkcjonowania').font.size = Pt(Project.HEADER_SIZE)
        header.add_run().add_break()

        counter = 1
        rules_counter = 1

        for entity in self.rules_dict.keys():
            rules_paragraph = document.add_paragraph()
            rules_paragraph.keep_together = True

            if self.rules_dict[entity]:
                rules_paragraph.add_run(str(counter) + '. Reguły dla KAT/' + '{0:03}'.format(self.erd.get_entity_by_name(entity).id) + ' ' + entity).font.size = Pt(16)
            rules_paragraph.add_run().add_break()
            for rule in self.rules_dict[entity]:
                rules_paragraph.add_run('REG/' + '{0:03}'.format(rules_counter)).font.bold=True
                rules_paragraph.add_run('\t\t')
                rules_paragraph.add_run(repr(rule))

                rules_counter += 1

            counter += 1
        document.add_page_break()

        print('Etap 4 wygenerowany')
