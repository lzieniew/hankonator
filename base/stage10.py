from docx.shared import Pt

from generation import Project

class Stage10(object):

    def __init__(self, erd):
        self.erd = erd

    def build(self, document):
        header = document.add_paragraph()
        header.add_run('10. Transformacja modelu konceptualnego do modelu logicznego').font.size = Pt(Project.HEADER_SIZE)
        header.add_run().add_break()

        for relationship in self.erd.relationships:
            relationship_paragraph = document.add_paragraph()
            relationship_paragraph.add_run('ZWI' + '{0:03}'.format(relationship.id)).bold = True
            relationship_paragraph.add_run(' ' + relationship.name + '(' + relationship.left_entity.upper() + '(' + relationship.left_quantity + '):' + relationship.right_entity.upper() + '(' + relationship.right_quantity + ')')
            relationship_paragraph.add_run().add_break()

            left_entity = self.erd.get_entity_by_name(relationship.left_entity)
            right_entity = self.erd.get_entity_by_name(relationship.right_entity)
            relationship_paragraph.add_run('ENC/' + '{0:03}'.format(left_entity.id) + ' ' + left_entity.name_singular.upper() + ' ')


        print('Etap 10 wygenerowany!')