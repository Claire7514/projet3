import pygame
from pygame.locals import *

from constants import *

class Hero:
    
    def __init__(self):
        """  self.macgyver = pygame.image.load(IMAGE_MACGYVER).convert_alpha()"""
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.num_objects = 0

    def moove(self, direction, level):
        if direction == 'right':
            if not(self.case_x < (NUM_SPRITE_SIDE - 1)) & level.structure[self.case_y][self.case_x + 1] != 'm':
                self.case_x += 1
                self.x = self.case_x * SPRITE_SIZE
        if direction == 'left':
            if self.case_x > 0 & level.structure[self.case_y][self.case_x - 1] != 'm':
                self.case_x -= 1
                self.x = self.case_x * SPRITE_SIZE
        if direction == 'down':
            if self.case_y < (NUM_SPRITE_SIDE - 1) & level.structure[self.case_y + 1][self.case_x] != 'm':
                self.case_y += 1
                self.y = self.case_y * SPRITE_SIZE
        if direction == 'up':
            if self.case_y > 0 & level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIZE

    def grab(self):
        self.num_objects += 1