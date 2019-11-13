import pygame
from pygame.locals import *
from constants import *

class Level:
    def __init__(self, file):
        self.file = "N1.txt"
        self.structure = 0

    def generer(self):
        with open(self.file, "r") as file:
            level_structure = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line.level.append(sprite)
                level_structure.append(line_level)
            self.structure = level_structure

    def show(self, window):
        wall = pygame.image.load(image_wall).convert()
        start = pygame.image.load(image_start).convert()
        arrival = pygame.image.load(image_keeper).convert_alpha()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * sprite_size # calcul position réelle en pixels (pas en cases) de chaque sprite
                y = num_line * sprite_size
                if sprite == 'm':
                    window.blit(wall(x,y))
                elif sprite == 'd':
                    window.blit(start(x,y))
                elif sprite == 'a':
                    window.blit(arrival(x,y))
                num_case += 1
            num_line += 1