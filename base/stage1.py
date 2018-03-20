import docx


class Stage1:

    def __init__(self, topic, objective, range, users):
        self.topic = topic
        self.objective = objective
        self.range = objective
        self.users = []

    def build(self, document):
        document.add_run('dupa 1')
