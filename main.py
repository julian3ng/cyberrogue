#!/usr/bin/env python3
import tdl
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
 
PLAYER_X = SCREEN_WIDTH//2
PLAYER_Y = SCREEN_HEIGHT//2

tdl.set_font('fonts/consolas12x12_gs_tc.png', greyscale=True, altLayout=True)

console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="CyberRogue", fullscreen=False)

def handle_input():
    

while not tdl.event.is_window_closed():
#    for i in range(32,127):
#        console.draw_char(i%8, i//8, chr(i), bg=None, fg=(255, 255, 255))

    console.draw_char(PLAYER_X, PLAYER_Y, '@', bg=None, fg=(255, 255, 255))
    tdl.flush()

    
