# This file was created by:Kiran Bogusky
# File to hold all sprites classes
# blocks, libraries, and modules
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *
# finding directories
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
sound_folder = os.path.join(game_folder, 'sounds')
# global variables
global locked
# creating player class
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, "player")).convert()
        self.rect = self.image.get_rect
        self.rect.center = (0,0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def controls(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            print("temp")
        if key[pg.K_w]:
            print("temp")
        if key[pg.K_s]:
            print("temp")
        if key[pg.K_d]:
            print("temp")
        if key[pg.K_l]:
            self.game.save(self.rect.x,self.rect.y,self.score, 1)
        if key[pg.K_SCROLLOCK] or key[pg.K_r]:
            locked = 1
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # CHECKING FOR COLLISION WITH MOBS
        mhits = pg.sprite.spritecollide(self, self.game.all_mobs, False)
        if mhits:
            self.score += 10
            
                

        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        
class Platform(Sprite):
    # create platform class
    def __init__( self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        # if Player.vel.x > 0:
        #     self.rect.x -= Player.vel.x
        self.rect.y = y
        self.category = category
        if self.category == "moving":
            self.speed = 5
    # uodate function to try to work as moving
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed


class NPC(Sprite):
    # create Npc class
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)

    def update(self):
        pass
