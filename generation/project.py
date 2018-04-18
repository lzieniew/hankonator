from docx import Document



class Project(object):

    HEADER_SIZE = 22
    SECONDAR_HEADER_SIZE = 16

    def __init__(self, progress_bar):
        self.stages = list(None for x in range(14))
        self.progress_bar = progress_bar

    def add_stage(self, stage):
        self.stages[stage.stage_number] = stage
        self.progress_bar.value = self.get_stage_count() / 13 * 100

    def get_stage(self, stage_number):
        return self.stages[stage_number]

    def get_stage_count(self):
        counter = 0
        for stage in self.stages:
            if stage is not None:
                counter += 1
        return counter

    def generate(self):
        document = Document()

        for stage in list(filter(lambda stage: stage is not None, self.stages)):
            stage.build(document)

        document.save('demo.docx')
        print('Dokument wygenerowany')
