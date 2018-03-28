

class Stage2:
    def __init__(self, reality_description, dictionary, users, functional_requirements, nonfunctional_requirements,
                 existing_database, cost):
        self.reality_description = reality_description
        self.dictionary = dictionary
        self.users = users
        self.functional_requirements = functional_requirements
        self.nonfunctional_requirements = nonfunctional_requirements
        self.existing_database = existing_database
        self.cost = cost

    def build(self, document):
        document.add_paragraph('Etap2')
        document.add_page_break()

        print('Etap 2 wygenerowany')
