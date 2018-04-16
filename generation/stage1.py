from docx import Document


class Stage1:

    def __init__(self, topic='', objective='', range='', users=''):
        self.topic = topic
        self.objective = objective
        self.range = range
        self.users = users
        self.stage_number = 1

    def build(self, document):
        document.add_paragraph('Etap 1')
        document.add_page_break()

        print('Etap 1 wygenerowany')
