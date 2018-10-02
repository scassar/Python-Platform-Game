'''
Created on 1 Oct. 2018

@author: Shaun
'''
import pygame
from settings import *
vec = pygame.math.Vector2
import random

#loading and parsing spritesheets
class Spritesheet:
    def __init__(self, filename):
        self.name = filename
        self.spritesheet = pygame.image.load(filename).convert()
        
    def getImage(self, x,y,width, height):
        image= pygame.Surface((width,height))
        image.blit(self.spritesheet, (0,0), (x,y,width,height))
        image = pygame.transform.scale (image,(width//2, height//2))
        return image

class Mob(pygame.sprite.Sprite):
    
    def __init__(self,game):
        self.groups = game.all_sprites, game.all_mobs
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.game = game
        self.image = pygame.image.load('img/doomfist.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (20,HEIGHT*0.1)
                
        self.pos = vec((20,HEIGHT*0.7) )
        self.vel = vec(MOB_ACC_X,MOB_ACC_Y) 
        
        
          
    

        
    def update(self):
        
        self.pos += self.vel
        self.rect.midbottom = self.pos
        
        if self.pos.x >= WIDTH-3:
            self.vel.x *= -1
        
        if self.pos.y < 0+3:
            self.vel.y *= -1
        
        if self.pos.y > HEIGHT:
            self.kill()
            self.game.mob_timer = 0
            
        if self.pos.x > WIDTH:
            self.kill()
            self.game.mob_timer = 0
        


class Powerup(pygame.sprite.Sprite):
    
    def __init__(self,game,platform):
        self.groups = game.all_powerups, game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.game= game
        self.platform = platform
        images = [self.game.spritesheet.getImage(698,1931,84,84),
                 ]
        self.image = random.choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = platform.rect.centerx
        self.rect.bottom = platform.rect.top-5
        
    def update(self):
        self.rect.bottom = self.platform.rect.top-5
        print ('updatePowerup')
        self.die()
        
    def die(self):
        if not self.game.all_platforms.has(self.platform):
           print ('kill')
           self.kill()
        

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game        
        #self.image = self.game.spritesheet.getImage (614,1063,120,191)
        self.image = pygame.image.load ('img/Simon.png')
        self.image.set_colorkey(BLACK)
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH / 2), (HEIGHT/2))
        self.pos = vec((WIDTH / 2), (HEIGHT/ 2) )
        self.vel = vec(0,0)  
        self.accel = vec(0,0) 
        self.jumping = False
        self.jumppower = False
        
    def update(self):
        self.accel = vec(0,PLAYER_GRAV) 

        keys = pygame.key.get_pressed()
        
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
          
    def jumpcut(self):
        
        if self.jumping == True:
            print (self.vel.y)
            if self.vel.y < -3:
                self.vel.y = -3
    
    def jump(self):   
        #jump only if we are standing on something
        
        self.jumping = True
        self.rect.x += 4
        hits = pygame.sprite.spritecollide(self, self.game.all_platforms,False)
        self.rect.x -= 4
        if hits and self.jumping == True:
            self.game.jumpsnd.play()
            self.vel.y = -PLAYER_JUMP
          
              
class Platform(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
                
        pygame.sprite.Sprite.__init__(self)
        self.game= game
        images = [self.game.spritesheet.getImage(0,288,380,94),
                   self.game.spritesheet.getImage(0,288,380,94)]
        self.image = random.choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
      
        if random.randrange(0,100) < POWERPCT:
            Powerup(self.game, self)
            
       