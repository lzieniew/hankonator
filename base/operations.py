
def add_foreign_keys(erd):
    for entity in erd.entities:
        relationships = erd.get_relationships_connected_with_entity(entity.name_singular)
        for relationship in relationships:
            if relationship.get_this_ends_multiplicity(entity.name_singular)[-1] == 'N':
                other_entity = erd.get_entity_by_name(relationship.get_other_entity_name(entity.name_singular))
                if other_entity.get_key() not in entity.foreign_keys:
                    entity.foreign_keys.append(other_entity.get_key())