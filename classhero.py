import pygame
from pygame.locals import*
from constants import*

class Hero:
    def __init__(self, right, left, down, up):
        self.macgyver = pygame.image.load(macgyver).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.direction = self.droite
        self.level = level

    def moove(self, direction):
        if direction == 'right':
            if self.case_x < (num_sprite_side - 1):
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                   self.case_x += 1
                   self.x = self.case_x * sprite_size
            self.moove = self.right
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
            self.moove = self.left
        if direction == 'down':
            if self.case_y < (num_sprite_side - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
            self.moove = self.down
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
            self.moove = self.up