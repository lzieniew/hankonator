from docx import Document


class Project(object):

    HEADER_SIZE = 22
    SECONDAR_HEADER_SIZE = 16

    def __init__(self):
        self.stages = list(None for x in range(14))

    def add_stage(self, stage):
        self.stages[stage.stage_number]

    def generate(self):
        document = Document()

        for stage in list(filter(lambda stage: stage is not None, self.stages)):
            stage.build(document)

        document.save('demo.docx')
        print('Dokument wygenerowany')
