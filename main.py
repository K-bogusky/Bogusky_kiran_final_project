# This file was created by:Kiran Bogusky
# Title: The mysterious bell
# GameDesign:
    # Goals: for the player:find out who killed the bellarmine bell
    # Rules: jump and run without falling
    # Feedback: minimap, interactive menu, timer/day count, sound effects.
    # Freedom: run side to side, walk through doors in bellarmine's campus.
# IDEAS:
# murder simulator(I wrote this last time but to fully explain:
# murder mystery interactive detective game)
# import libraries and modules
import pygame as pg
from pygame import sprite as spr
from sprites import *
from settings import *

def save(x, y, lvl, file):
    # select save file
    if file == 1:
        # save to designated file. write from python by w3schools:https://www.w3schools.com/python/python_file_write.asp 
        # open file
        s = open("save_1.txt", "w")
        # write to file with "|" in between values
        s.write(str(x)+"|"+str(y)+"|"+str(lvl)+"|")
        s.close
    if file == 2:
        s = open("save_2.txt", "w")
        s.write(str(x)+"|"+str(y)+"|"+str(lvl)+"|")
        s.close
    if file == 3:
        s = open("save_3.txt", "w")
        s.write(str(x)+"|"+str(y)+"|"+str(lvl)+"|")
        s.close


def load(file):
    if file == 1:
        s = open("save_1.txt", "r")
        # reading from ciupicri and alfe:https://stackoverflow.com/questions/47927039/reading-a-file-until-a-specific-character-in-python
        # create a variable for all of the file's text
        text = s.read()
        # seperate text into values between "|"
        textlist = text.split("|")
        # reassign values
        x = textlist[0]
        y = textlist[1]
        lvl =textlist[1]
        # return values.
        return x, y, lvl 
    elif file == 2:
        s = open("save_2.txt", "r")
        text = s.read()
        textlist = text.split("|")
        x = textlist[0]
        y = textlist[1]
        lvl =textlist[1]
        return x, y, lvl
    elif file == 3:
        s = open("save_3.txt", "r")
        text = s.read()
        textlist = text.split("|")
        x = textlist[0]
        y = textlist[1]
        lvl =textlist[1]
        return x, y, lvl

    
    
