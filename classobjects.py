import pygame
import random
from pygame.locals import *

from constants import *

class Objects:
    def __init__(self):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def randomize_position(self):
        while self.level[self.case_y][self.case_x] == '0':
            self.case_x = random.randint(0,14)
            self.case_y = random.randint(0,14)
            self.x = self.case_x * sprite_size
            self.y = self.case_y * sprite_size