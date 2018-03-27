from docx.shared import Pt


class Stage3:

    def __init__(self, erd):
        self.erd = erd

    def build(self, document):

        run = document.add_paragraph('3. Kategorie').add_run()
        font = run.font
        font.size = Pt(18)




        for entity in self.erd.entities:
            document.add_paragraph('KAT/' + '{0:03}'.format(entity.id) + ' ' + entity.name_singular)
            description = document.add_paragraph()
            description.add_run('Opis:').bold = True
            description.add_run().add_break()
            description.add_run('   Tutaj krótki opis encji')
            description.add_run().add_break()
            description.add_run('Atrybuty:').bold = True
            description.add_run().add_break()
