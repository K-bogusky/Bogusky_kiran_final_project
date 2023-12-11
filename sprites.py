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
# global sprites

# creating player class
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        

