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
