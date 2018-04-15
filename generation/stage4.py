from docx.shared import Pt


from generation import Project
from base.rule import Rule


class Stage4:

    def __init__(self, erd, rules):
        self.erd = erd
        self.rules = rules

        self.rules_dict = {}


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
