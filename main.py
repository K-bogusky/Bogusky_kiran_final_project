# This file was created by:Kiran Bogusky
# Title: The mysterious bell
# GameDesign:
    # Goals: for the player:have the ability to save and load using L and O
    # Rules: jump and run without falling
    # Feedback: score counter
    # Freedom: run side to side,.
# IDEAS:
# murder simulator(I wrote this last time but to fully explain:
# murder mystery interactive detective game)
# import libraries and modules
import pygame as pg
from pygame import sprite as spr
from sprites import *
from settings import *
from random import randint
class Game:
    def __init__(self):
        # init pygame and create an instance
        pg.init()
        pg.mixer.init()
        # set the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        # start the clock
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,10):
            # instantiates random mobs
            m = NPC(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)

        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # sets the update function
    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed * PLAYER_FRIC

         # this prevents the player from jumping up through a platform
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                print("ouch")
                self.score -= 1
                if self.player.rect.bottom >= hits[0].rect.top - 1:
                    self.player.rect.top = hits[0].rect.bottom
                    self.player.acc.y = 5
                    self.player.vel.y = 0
        

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    def save(self, x, y, lvl):
        # select save file
        # if file == 1:
        # save to designated file. write from python by w3schools:https://www.w3schools.com/python/python_file_write.asp 
        # open file
        s = open("save_1.txt", "w")
        # write to file with "|" in between values
        s.write(str(x)+"|"+str(y)+"|"+str(lvl)+"|")
        s.close
        # elif file == 2:
        #     s = open("save_2.txt", "w")
        #     s.write(str(x)+"|"+str(y)+"|"+str(lvl)+"|")
        #     s.close
        # elif file == 3:
        #     s = open("save_3.txt", "w")
        #     s.write(str(x)+"|"+str(y)+"|"+str(lvl)+"|")
        #     s.close


    def load(self, file):
        if file == 1:
            s = open("save_1.txt", "r")
            # reading from ciupicri and alfe:https://stackoverflow.com/questions/47927039/reading-a-file-until-a-specific-character-in-python
            # create a variable for all of the file's text
            text = s.read()
            # seperate text into values between "|"
            textlist = text.split("|")
            # reassign values
            x = float(textlist[0])
            y = float(textlist[1])
            lvl = float(textlist[2])
            # return values.
            return x, y, lvl 
        elif file == 2:
            s = open("save_2.txt", "r")
            text = s.read()
            textlist = text.split("|")
            x = float(textlist[0])
            y = float(textlist[1])
            lvl = float(textlist[2])
            return x, y, lvl
        elif file == 3:
            s = open("save_3.txt", "r")
            text = s.read()
            textlist = text.split("|")
            x = float(textlist[0])
            y = float(textlist[1])
            lvl = float(textlist[2])
            return x, y, lvl
    
    def draw_text(self, text, size, color, x, y):
        # draaws text
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()


    
    
