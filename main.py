import pygame 
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arial', 32)
        self.player = pygame.draw.rect((250, 0, 0))
        self.running = True

    def new(self):
        self.playing = True
