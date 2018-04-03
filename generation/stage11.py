from docx.shared import Pt

from generation import Project


class Stage11(object):

    def __init__(self, erd):
        self.erd = erd

    def build(self, document):
        header = document.add_paragraph()
        header.add_run('11. Definicje schematów relacji i przykładowe dane w poszczególnych tabelach').font.size = Pt(Project.HEADER_SIZE)
        header.add_run().add_break()

        for entity in self.erd.entities:
            relation_paragraph = document.add_paragraph()
            relation_paragraph.add_run('REL/' + '{0:03}'.format(entity.id) + entity.name_plural + '/' + entity.name_singular.upper()).bold = True
            relation_paragraph.add_run().add_break()
            relation_paragraph.add_run('Opis schematu relacji:')
            relation_paragraph.add_run().add_break()

            table = document.add_table(rows = len(entity.attributes) + len(entity.foreign_keys) + 1, cols = 10)
            hdr_cells = table.rows[0].cells
            runs = []
            runs.append(hdr_cells[0].paragraphs[0].add_run('Nazwa atrybutu'))
            runs.append(hdr_cells[1].paragraphs[0].add_run('Dziedzina'))
            runs.append(hdr_cells[2].paragraphs[0].add_run('Maska'))
            runs.append(hdr_cells[3].paragraphs[0].add_run('OBL'))
            runs.append(hdr_cells[4].paragraphs[0].add_run('Wart. Dom.'))
            runs.append(hdr_cells[5].paragraphs[0].add_run('Ograniczenia'))
            runs.append(hdr_cells[6].paragraphs[0].add_run('Unikalność'))
            runs.append(hdr_cells[7].paragraphs[0].add_run('Klucz'))
            runs.append(hdr_cells[8].paragraphs[0].add_run('Referencje'))
            runs.append(hdr_cells[9].paragraphs[0].add_run('Źródło danych'))
            for run in runs:
                run.font.size = Pt(10)
                run.bold = True
            row_counter = 1
            for attribute in entity.attributes:
                row = table.rows[row_counter].cells
                row[0].text = attribute.name
                row[1].text = repr(attribute.type)
                if attribute.is_key:
                    row[7].text = 'PK'
                row_counter += 1
            for foreign_key in entity.foreign_keys:
                if row[7].text == '':
                    row[7].text = 'FK'
                else:
                    row[7].text += ', FK'

                reference = self.erd.get_entity_by_pk(foreign_key.name).name_plural
                if row[8].text == '':
                    row[8].text = reference
                else:
                    row[8].text += ', ' + reference





