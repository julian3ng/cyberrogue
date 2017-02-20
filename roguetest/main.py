from components import *
from systems import *
from entity import *
import tcod

# global tables
ai_table = ComponentTable(AI)
human_ai_table = ComponentTable(HumanAI, parent=ai_table)
computer_ai_table = ComponentTable(ComputerAI, parent=ai_table)
position_table = ComponentTable(Position)
render_table = ComponentTable(Render)

# global systems
ai_system = AISystem(ai_table)
movement_system = MovementSystem(ai_table, position_table)
render_system = RenderSystem(position_table, render_table)

def get_input():
    key = tcod.console_wait_for_keypress(True)
    if key.vk == tcod.KEY_CHAR:
        return key.c
    else:
        return None
    
def initialize():
    """
    Set up constants, systems, etc.
    """
    player = Entity()
    human_ai_table.add(player.entity_id)
    position_table.add_component(player.entity_id, Position(0, 0))
    render_table.add_component(player.entity_id, Render('@'))

def game_loop():
    """
    Do actual game stuff:
    1) Handle input
    2) Update
    3) Render
    """
    player_input = None
    while player_input != ord('q'):
        player_input = get_input()
        ai_system.update(player_input)
        movement_system.update()
        render_system.update()

if __name__ == "__main__":
    initialize()
    game_loop()
