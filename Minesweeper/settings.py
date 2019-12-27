import pygame
import math
import random

tiles = []
pygame.init()
pygame.display.set_caption("Minesweeper")
run = True

x = 20
y = 15
mines = 100

tile_size = 30

FPS = 1001

width = x * tile_size
height = y * tile_size
margin = 15
header = 50

screen = pygame.display.set_mode((width + margin*2, height + margin*2 + header))

mouseX = 0
mouseY = 0
press = False
first_move = False


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light_grey = (220, 220, 220)
grey = (180, 180, 180)
red = (255, 0, 0)