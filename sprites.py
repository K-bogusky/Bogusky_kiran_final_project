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
    # from Chris Bradfield at kidscancode
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
        if key[pg.K_SCROLLOCK] or key[pg.K_r]:
            locked = 1
        
        

