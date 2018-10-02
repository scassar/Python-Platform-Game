import pygame
import random
from settings import *
from sprites import *
import time
import os

class Game() :
    
    def __init__(self):
        
        pygame.init()
        pygame.mixer.init()
              
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.mob_timer = 0
        
        
    def run(self):
        
        pygame.mixer.music.load('snd/happy.OGG')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.2)
        self.running = True
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
                self.jumppower = False
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom < lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0
                    self.jumping = False
           
            hitsp = pygame.sprite.spritecollide(self.player, self.all_powerups, False)
            
            if hitsp:
                self.player.vel.y = -50
                
            hitsm = pygame.sprite.spritecollide(self.player, self.all_mobs, False)
            
            if hitsm:
                print ('gameover') 
                self.gameover()
                
        #render
        #if we hit the top of the screen
        #create mob
        if self.mob_timer == 0:
            
            if random.randrange(0, 100) < MOB_SPAWNPCT:
                                      
                self.uppercutsnd.play()
                Mob(self)
                self.mob_timer = 1
                print ('spawn MOB')
             
        
        
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.all_platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    
            for mob in self.all_mobs:
                if mob.rect.y < 0:
                    mob.rect.y -= abs(self.player.vel.y)
                else:
                    mob.rect.y += abs(self.player.vel.y)
      
            
            
        while len(self.all_platforms) <= 4:
            width = random.randrange(50,100)
            p = Platform(self, random.randrange(0,500),self.player.pos.y - random.randrange(70,75))          
            
            self.all_sprites.add(p)
            self.all_platforms.add(p)
            self.score += 1
            
            
             
        #check if game over   
        
        if self.player.rect.top > HEIGHT:
            
            print ('gameover') 
            self.gameover()
         
    

        #self.screen.fill(WHITE)

    def draw(self):
            self.screen.fill(LIGHTBLUE)
            self.all_sprites.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect)
            self.display_text('freesansbold.ttf', 'SCORE: ' + str(self.score), 5, BLACK, 80, 30,False)
            pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print ('cut the jump')
                    self.player.jumpcut()
            
            #print(event)        
    
    def show_start(self):
        #this is the code for the start of the game
        
        self.screen.fill(WHITE)
        self.display_text('freesansbold.ttf', 'Welcome to the klasseman game', 20, BLACK, (WIDTH / 2), (HEIGHT / 2),True)
        self.display_text('freesansbold.ttf', 'Dont be a pussy', 20, BLACK, (WIDTH / 2), (HEIGHT / 1.5),False)
        self.display_button('freesansbold.ttf','start',5,GREEN,WIDTH/2-25,HEIGHT/1.2,50,50)
        pygame.display.flip()
        self.waiting()
    
    def waiting(self):
        waiting = True
        
        while(waiting):
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                    quit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                   #now we check for collision
                    locationx = event.pos[0]
                    locationy = event.pos[1]

                    if locationy > HEIGHT/1.2 and locationy < HEIGHT/1.2 + 50:
                        if locationx > WIDTH/2-25 and locationx < WIDTH/2-25 + 50:
                            print ('no longer waiting')
                            waiting = False
                   
                    
                    #waiting = False        
                    
    def display_button(self, font, text, size, color, x, y, w ,h):
        
        pygame.draw.rect(self.screen, color,(x,y,w,h))
        self.display_text(font, text, size, BLACK, x+(0.5*w)  ,y+(0.5*h)  ,  False   )
        pygame.display.update()
        
    
    def display_text(self,font, text, size, color, x, y, whiteout):
        font = pygame.font.Font(font,20)
        surface = font.render(text, True,color)
        surfRect = surface.get_rect()
        surfRect.center = (x, y)
        
        if whiteout:
            self.screen.fill(WHITE)
        
        self.screen.blit(surface, surfRect)
    
    def show_end(self):
        
        self.display_text('freesansbold.ttf', 'GAME OVER', 20, BLACK, (WIDTH / 2), (HEIGHT / 2),True)
        self.display_text('freesansbold.ttf', 'Score: ' + str(self.score), 20, BLACK, (WIDTH / 2), (HEIGHT / 1.5),False)
        self.destroy_sprite()
        pygame.display.flip()
        time.sleep(2)
        
    
    def destroy_sprite(self):
        for sprite in self.all_sprites:
            sprite.kill()
        
            
    
    def gameover(self):
        pygame.mixer.music.fadeout(500)
        self.running = False
        self.show_end()
        print ('start a new game')
        self.new()
    
    def load_data(self):
        imgpath = os.path.join("img", str(SPRITESHEETNAME))
        self.spritesheet = Spritesheet(imgpath)
        
        sndpath = os.path.join("snd", 'doinit.wav')
        sndupperpath = os.path.join("snd", 'uppercut.wav')
        self.jumpsnd = pygame.mixer.Sound(sndpath)
        self.uppercutsnd = pygame.mixer.Sound(sndupperpath)          
        #load the sound
        
        
    
    def new(self):
        self.show_start()
        print ('out of start')
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_platforms = pygame.sprite.Group()
        self.all_powerups = pygame.sprite.Group()
        self.all_mobs = pygame.sprite.Group()
        self.all_sprites.add(self.player)       
        self.running=True
        
        for platform in PLATFORM_LIST:
            
            p = Platform(self, *platform)
            self.all_sprites.add(p)
            self.all_platforms.add(p)
        
        self.run()
    



#start Game

game = Game()
game.new()                                   