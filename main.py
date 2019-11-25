#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from classlevel import *
from classhero import *
from constants import *

pygame.init()

WINDOW = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))

ICONE = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
pygame.display.set_icon(ICONE)

pygame.display.set_caption(TITLE_WINDOW)

BACKGROUND = pygame.image.load(IMAGE_BACKGROUND).convert()
MAC = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
WALL = pygame.image.load(IMAGE_WALL).convert()
ETHER = pygame.image.load(IMAGE_ETHER).convert_alpha()
NEEDLE = pygame.image.load(IMAGE_NEEDLE).convert_alpha()
TUBE = pygame.image.load(IMAGE_TUBE).convert_alpha()

pygame.display.flip() #raffraichissement

LVL = level(FILE)

CONTINUE = 1
while CONTINUE:
    pygame.time.Clock().tick(30) #limiter la vitesse de la boucle 

    for event in pygame.event.get():


        if event.type == QUIT:
            CONTINUE = 0

        elif event.type == KEYDOWN:

            if event.key == K_RIGHT:
                MAC.move('right')
            elif event.key == K_LEFT:
                MAC.move('left')
            elif event.key == K_UP:
                MAC.move('up')
            elif event.key == K_DOWN:
                MAC.move('down')

        # affihcage nouvelles positions  
        WINDOW.blit(BACKGROUND, (0,0))
        LVL.display(WINDOW)
        WINDOW.blit(MAC.image, (MAC.x, MAC.y))

        pygame.display.flip()

        if (MAC.x, MAC.y) == (ETHER.x, ETHER.y):
            MAC.grab()

        if (MAC.x, MAC.y) == (NEEDLE.x, NEEDLE.y):
            MAC.grab()

        if (MAC.x, MAC.y) == (TUBE.x, TUBE.y):
            MAC.grab()

        if level.structure[MAC.case_y][MAC.case_x] == 'a':
            if MAC.num_objects == 3:
                #afficher message
                CONTINUE = 0
            else:
                #afficher message 
                CONTINUE = 0