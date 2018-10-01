'''
Created on 1 Oct. 2018

@author: Shaun
'''

#player settings
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_SIZE = ((50,50))
PLAYER_GRAV = 0.8

#initalise    
WIDTH = 600
HEIGHT = 800
FPS = 60
TITLE = "Jumpy"
#colours
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)

#Game settings
PLATFORM_LIST = [(0, HEIGHT-40, WIDTH, 40), 
                 (0, HEIGHT*3/4, WIDTH/4, 20),
                 (100, HEIGHT*2/4, WIDTH/4, 20),
                 (150, HEIGHT*1/4, WIDTH/4, 20)]