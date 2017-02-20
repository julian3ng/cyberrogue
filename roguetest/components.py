class Component(object):
    """
    Components need to be able to receive messages 
    """
    def __init__(self):
        self.messages = []
        
    def receive(self, message):
        self.messages.append(message)

    def first_message(self):
        return self.messages.pop(0)
        

        
class AI(Component):
    def __init__(self):
        super(AI, self).__init__()

    def next_action(self, input_value=None):
        raise NotImplementedError


class HumanAI(AI):
    def __init__(self):
        super(HumanAI, self).__init__()

    def next_action(self, player_input=None):
        if player_input == ord('h'): return (-1,0)
        if player_input == ord('j'): return (0,1)
        if player_input == ord('k'): return (0,-1)
        if player_input == ord('l'): return (1,0)
        else: return (0,0)

class ComputerAI(AI):
    def __init__(self):
        super(ComputerAI, self).__init__()

    def next_action(self, computer_input=None):
        if computer_input == ord('q'): return (0,0)
        return (0,0)

        
class Position(Component):
    def __init__(self, x = -1, y = -1):
        super(Position, self).__init__()
        self.x = x
        self.y = y
        self.last_x = None
        self.last_y = None

        
class Render(Component):
    def __init__(self, char):
        super(Render, self).__init__()
        self.char = char

        
class ComponentTable(object):
    """
    Holds "has-a" information for a particular component
    """
    def __init__(self, cls, parent=None):
        self.table = {}
        self.cls = cls
        self.parent = parent

    def add(self, entity_number):
        """
        Create component, add to entity
        """
        new_component = self.cls()
        self.table[entity_number] = new_component
        if self.parent is not None:
            self.parent.add_component(entity_number, new_component)

    def add_component(self, entity_number, component):
        """
        Add specific component to entity
        """
        self.table[entity_number] = component
        if self.parent is not None:
            self.parent.add_component(entity_number, component)

    def rm(self, entity_number):
        """
        Remove component from entity
        """
        self.table.pop(entity_number)
        if self.parent is not None:
            self.parent.rm(entity_number)

    def all_entities(self):
        """
        Return an iterator of all entities with this component
        """
        return self.table.keys()

    def all_components(self):
        """
        Return an iterator of all components in this table
        """
        return self.table.values()

    def component_of(self, entity_number):
        """
        Return the component of this entity
        """
        return self.table[entity_number]

    def has_entity(self, entity_number):
        """
        Return whether or not an entity has this component
        """
        return entity_number in self.table
        
if __name__ == "__main__":
    pass
