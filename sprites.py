'''
Created on 1 Oct. 2018

@author: Shaun
'''
import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game        
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2), (HEIGHT/2))
        self.pos = vec((WIDTH / 2), (HEIGHT/ 2) )
        self.vel = vec(0,0)  
        self.accel = vec(0,0) 
        
    def update(self):
        self.accel = vec(0,PLAYER_GRAV) 

        keys = pygame.key.get_pressed()
        print(keys)
        if(keys[pygame.K_LEFT]):
            self.accel.x = -PLAYER_ACC
        if(keys[pygame.K_RIGHT]):
            self.accel.x = PLAYER_ACC
        
        
        self.accel.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.accel 
        self.pos += self.vel + 0.5 * self.accel
                
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        
        self.rect.midbottom = self.pos
          
    def jump(self):   
        #jump only if we are standing on something
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.all_platforms,False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20 
          
              
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        