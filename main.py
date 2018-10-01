import pygame
import random
from settings import *
from sprites import *

class Game() :
    
    def __init__(self):
        
        pygame.init()
        pygame.mixer.init()
        
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_platforms = pygame.sprite.Group()
        self.all_sprites.add(self.player)       
        self.running=True
        
        for platform in PLATFORM_LIST:
            
            p = Platform(*platform)
            self.all_sprites.add(p)
            self.all_platforms.add(p)
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
    def run(self):
        
        while(self.running):
        #process input
            self.clock.tick(60)
            self.events()
        #update  
            self.update()
        #draw
            self.draw()

        #render   
    
    #code for the updating of the objects
    def update(self):
        self.all_sprites.update()
        #self.all_platforms.update()
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits: 
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        #render
        #if we hit the top of the screen
        
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.all_platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
            
           

        #self.screen.fill(WHITE)

    def draw(self):
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            
            pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
            
            #print(event)        
    
    def show_start(self):
        pass
    
    def show_end(self):
        pass 
    
    def new(self):
        self.run()
    
 



#start Game

game = Game()
game.new()                                   