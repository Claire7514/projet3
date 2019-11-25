import pygame
from pygame.locals import *

from constants import *

class Level:
    def __init__(self, f):
        self.file = f
        self.structure = 0

    def generate(self):
        with open(self.file, "r") as file: #ouverture du fichier
            level_structure = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line.level.append(sprite) # ajout du sprite à la liste de la ligne
                level_structure.append(line_level) # ajout de la ligne à la liste du niveau
            self.structure = level_structure # on sauvegarde cette structure 

    def show(self, window):
        wall = pygame.image.load(IMAGE_WALL).convert()
        start = pygame.image.load(IMAGE_START).convert()
        arrival = pygame.image.load(IMAGE_KEEPER).convert_alpha()

        num_line = 0
        for line in self.structure: # parcours des listes de lignes 
            num_case = 0
            for sprite in line:
                x = num_case * SPRITE_SIZE # calcul position réelle en pixels (pas en cases) de chaque sprite
                y = num_line * SPRITE_SIZE
                if sprite == 'm':
                    window.blit(wall(x,y))
                elif sprite == 'd':
                    window.blit(start(x,y))
                elif sprite == 'a':
                    window.blit(arrival(x,y))
                num_case += 1
            num_line += 1