# This file was created by: Kiran Bogusky
# This is a file to store all settings, pre-set and manual.
WIDTH = 1080
HEIGHT = 720
FPS = 30
# PLAYER SETTINGS
PLAYER_FRIC = 1
PLAYER_JUMP = 75
PLAYER_GRAV = 5.5
# DEFINE COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# sets a list of all the platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"moving"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "moving")]