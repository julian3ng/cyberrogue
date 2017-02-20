"""
An entity is just an id, associated with a component in the given component table.
"""
class Entity(object):
    last_id = 0
    def __init__(self):
        self.entity_id = Entity.last_id
        Entity.last_id += 1
        
