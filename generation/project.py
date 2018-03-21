from docx import Document


class Project(object):

    def __init__(self, stages):
        self.stages = stages

    def generate(self):
        document = Document()

        for stage in self.stages:
            stage.build(document)

        document.save('demo.docx')
