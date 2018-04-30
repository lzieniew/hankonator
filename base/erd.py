import pickle

class Erd(object):

    def __init__(self):
        self.entities = []
        self.relationships = []

    def remove_entity(self, index):
        del self.entities[index]

    def remove_relationship(self, index):
        del self.relationships[index]

    def get_entities_connected_wtih_relationship(self, relationship_name):
        entities = set()
        for relationship in self.relationships:
            if relationship.name == relationship_name:
                entities.add(relationship)
        return list(entities)

    def get_relationships_connected_with_entity(self, entity_name, relationships_alt=None):
        relationships = relationships_alt if relationships_alt is not None else self.relationships
        relationships_set = set()
        for relationship in relationships:
            if relationship.left_entity == entity_name or relationship.right_entity == entity_name:
                relationships_set.add(relationship)
        return list(relationships_set)

    def get_relationship_between(self, entity_1_name, entity_2_name):
        out = None
        for relationship in self.relationships:
            if (relationship.left_entity == entity_1_name and relationship.right_entity == entity_2_name)\
                    or (relationship.left_entity == entity_2_name and relationship.right_entity == entity_1_name):
                out = relationship
        return out

    def get_entity_by_name(self, name):
        entities_with_name = list(filter(lambda entity: entity.name_singular == name, self.entities))
        if not entities_with_name:
            return None
        else:
            return entities_with_name[0]

    def get_relationship_by_name(self, name):
        relationships_with_name = list(filter(lambda rel: rel.name == name, self.relationships))
        if not relationships_with_name:
            return None
        else:
            return relationships_with_name[0]

    def get_entity_by_pk(self, pk_name):
        result_entity = None
        for entity in self.entities:
            if entity.get_key().name == pk_name:
                result_entity = entity
        return result_entity

    def get_relationships_without_associative_entities(self):
        result = []
        for entity in self.entities:
            relationships = self.get_relationships_connected_with_entity(entity_name=entity.name_singular)
            if entity.is_associative:
                left_entity = self.get_entity_by_name(relationships[0].get_entity_with_N_quantity())
                right_entity = self.get_entity_by_name(relationships[1].get_entity_with_N_quantity())
                if not left_entity.is_associative and not right_entity.is_associative:
                    result.append(Relationship(left_entity=relationships[0].get_entity_with_N_quantity(),
                                  left_quantity=relationships[0].get_N_quantity(),
                                  right_entity=relationships[1].get_entity_with_N_quantity(),
                                  right_quantity=relationships[1].get_N_quantity(),
                                  name='temp'))
            else:
                for relationship in relationships:
                    left_entity = self.get_entity_by_name(relationship.left_entity)
                    right_entity = self.get_entity_by_name(relationship.right_entity)
                    if relationship not in result and not left_entity.is_associative and not right_entity.is_associative:
                        result.append(relationship)
        return result


class Entity(object):

    def __init__(self, name_singular, name_plural, attributes, is_strong=False, description=''):
        self.name_singular = name_singular
        self.name_plural = name_plural
        self.attributes = attributes
        self.id = None
        self.foreign_keys = []
        self.is_strong = is_strong
        self.description = description

    def get_key(self):
        out = None
        for attribute in self.attributes:
            if attribute.is_key:
                out = attribute
        return out

    def repr_attributes(self):
        result = '('
        for attribute in self.attributes:
            result += attribute.name
            result += ', '
        result = result[:-2]
        result += ')'
        return result

    # TODO fix bug: sometimes there is a comma at the end of argument list
    def build_argument_list(self, paragraph):
        paragraph.add_run('(')
        counter = 0
        for attribute in self.attributes:
            name_run = paragraph.add_run(attribute.name)
            name_run.italic = True
            if attribute.is_key:
                name_run.underline = True
            if counter < len(self.attributes) + len(self.foreign_keys) - 1:
                paragraph.add_run(', ')
            counter += 1
        for key in self.foreign_keys:
            paragraph.add_run('#' + key.name).italic = True
            if counter < len(self.attributes) + len(self.foreign_keys) - 1:
                paragraph.add_run(', ')

        paragraph.add_run(')')


    def __repr__(self):
        return self.name_singular + repr(self.attributes)


class Relationship(object):

    ID = 1

    def __init__(self, name, left_entity, right_entity, left_quantity, right_quantity):
        self.name = name
        self.left_entity = left_entity
        self.right_entity = right_entity
        self.left_quantity = left_quantity
        self.right_quantity = right_quantity
        self.id = Relationship.ID
        Relationship.ID += 1

    def get_this_ends_multiplicity(self, this_end_entity_name):
        if this_end_entity_name == self.right_entity:
            return self.right_quantity
        elif this_end_entity_name == self.left_entity:
            return self.left_quantity
        else:
            return None

    def get_other_ends_multiplicity(self, this_end_entity_name):
        if this_end_entity_name == self.right_entity:
            return self.left_quantity
        elif this_end_entity_name == self.left_entity:
            return self.right_quantity
        else:
            return None

    def get_other_entity_name(self, this_name):
        if self.left_entity == this_name:
            return self.right_entity
        elif self.right_entity == this_name:
            return self.left_entity

    def get_entity_with_N_quantity(self):
        if 'N' in self.left_quantity and 'N' in self.right_quantity:
            return (self.left_entity, self.right_entity)
        elif 'N' in self.left_quantity:
            return (self.right_entity)
        elif 'N' in self.right_quantity:
            return (self.left_entity)
        else:
            return None

    def get_N_quantity(self):
        if 'N' in self.left_quantity and 'N' in self.right_quantity:
            return (self.left_quantity, self.right_quantity)
        elif 'N' in self.left_quantity:
            return (self.left_quantity)
        elif 'N' in self.right_quantity:
            return (self.right_quantity)
        else:
            return None

    def __repr__(self):
        return self.left_entity + ' -- ' + self.left_quantity + ' --- ' + self.name + ' --- ' + self.right_quantity + ' -- ' + self.right_entity


class Attribute(object):
    def __init__(self, name, type, is_key=False, description=''):
        self.name = name
        self.type = type
        self.is_key = is_key
        self.description = description

    def __repr__(self):
        return self.name + ':' + repr(self.type)
