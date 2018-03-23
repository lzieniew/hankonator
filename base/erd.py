class Entity(object):
    def __init__(self, name_singular, name_plural, attributes):
        self.name_singular = name_singular
        self.name_plural = name_plural
        self.attributes = attributes


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