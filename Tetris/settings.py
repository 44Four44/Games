import pygame
import math
import random
import time
import copy

pygame.init()
pygame.display.set_caption("Tetris")

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 32)

run = True

FPS = 1000

sWidth = 600
sHeight = 600

tileSize = 28
columns = 10
rows = 20

bWidth = tileSize*columns
bHeight = tileSize*rows

# Entire game screen
screen = pygame.display.set_mode((sWidth, sHeight), pygame.SRCALPHA)

# Board for the blocks
board = pygame.Surface((bWidth, bHeight), pygame.SRCALPHA)

# Mouse events
mouseX = 0
mouseY = 0
mousePress = False

# Key events
downPress = False
leftPress = False
rightPress = False

# List of all blocks on the screen
blocks = []

# Coordinates of walls
walls = []

# Scoring
score = 0

# File paths
modesPath = '/Users/EthanWang/Games/Tetris/modes.txt'

# Colors
black = [0, 0, 0]
white = [255, 255, 255]
lightGrey = [220, 220, 220]
darkGrey = [150, 150, 150]
grey = [180, 180, 180]
red = [255, 0, 0]
orange = [245, 155, 66]
green = [66, 245, 87]
darkBlue = [66, 90, 245]
lightBlue = [66, 233, 245]
purple = [182, 66, 245]
yellow = [245, 236, 66]