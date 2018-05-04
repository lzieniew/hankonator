from docx.shared import Pt, Inches


from generation import Project


class Stage9:

    def __init__(self, erd):
        self.erd = erd
        self.stage_number = 9

    def build(self, document):

        header = document.add_paragraph()
        header.add_run('9. Diagram ERD').font.size = Pt(Project.HEADER_SIZE)
        document.add_page_break()

        print('Etap 9 wygenerowany')
