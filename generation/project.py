from docx import Document


class Project(object):

    HEADER_SIZE = 22
    SECONDAR_HEADER_SIZE = 16

    def __init__(self, stages):
        self.stages = stages

    def generate(self):
        document = Document()

        for stage in self.stages:
            stage.build(document)

        document.save('demo.docx')
        print('Dokument wygenerowany')
