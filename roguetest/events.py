class Event(object):
    """
    Events are sent by SYSTEMS targeted at ENTITIES by their entity_id
    """
    def __init__(self, entity_id):
        self.entity_id = entity_id


class MovementEvent(Event):
    def __init__(self, entity_id):
        super(MovementEvent, self).__init__(entity_id)


        
