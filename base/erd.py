import pickle

class Erd(object):

    def __init__(self):
        self.entities = []
        self.relationships = []

    def remove_entity(self, index):
        del self.entities[index]

    def remove_relationship(self, index):
        del self.relationships[index]

    def save(self):
        output = open('erd.P', 'w')
        pickle.dump(self, output)

    @staticmethod
    def load():
        pkl_file = open('erd.P')
        return pickle.load(pkl_file)


class Entity(object):

    ID = 1

    def __init__(self, name_singular, name_plural, attributes):
        self.name_singular = name_singular
        self.name_plural = name_plural
        self.attributes = attributes
        self.id = Entity.ID
        Entity.ID += 1

    def __repr__(self):
        return self.name_singular + repr(self.attributes)


class Relationship(object):
    def __init__(self, name, left_entity, right_entity, left_quantity, right_quantity):
        self.name = name
        self.left_entity = left_entity
        self.right_entity = right_entity
        self.left_quantity = left_quantity
        self.right_quantity = right_quantity

    def __repr__(self):
        return self.name


class Attribute(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return self.name + ':' + self.type