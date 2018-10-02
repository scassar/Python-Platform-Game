'''
Created on 1 Oct. 2018

@author: Shaun
'''

#player settings
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_SIZE = ((120,85))
PLAYER_GRAV = 0.8
SPRITESHEETNAME="spritesheet_jumper.png"
PLAYER_JUMP = 20
#initalise    
WIDTH = 600
HEIGHT = 800
FPS = 60
TITLE = "Jumpy"
POWERPCT = 12
#colours
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
LIGHTBLUE=(0,222,255)
#MOB Settings
MOB_ACC_X = 3.5
MOB_ACC_Y = -3.5
MOB_SPAWNPCT = 0.15

#Game settings
PLATFORM_LIST = [(0, HEIGHT*2/4), 
                 (0, HEIGHT*1/4),
                 (WIDTH/2-50, HEIGHT*3/4),
                 (WIDTH/3, HEIGHT*1/4)]

