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
mac = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
wall = pygame.image.load(IMAGE_WALL).convert()
ether = pygame.image.load(IMAGE_ETHER).convert_alpha()
needle = pygame.image.load(IMAGE_NEEDLE).convert_alpha()
tube = pygame.image.load(IMAGE_TUBE).convert_alpha()

pygame.display.flip() #raffraichissement

CONTINUE = 1
while CONTINUE:
    pygame.time.Clock().tick(30) #limiter la vitesse de la boucle 
    
    for event in pygame.event.get():
        
        
        if event.type == QUIT:
            CONTINUE = 0
        
        elif event.type == KEYDOWN:
            
            if event.key == K_RIGHT:
                    mac.moove('right')
                elif event.key == K_LEFT:
                    mac.moove('left')
                elif event.key == K_UP:
                    mac.moove('up')
                elif event.key == K_DOWN:
                    mac.moove('down')
      
        # affihcage nouvelles positions  
        window.blit(BACKGROUND, (0,0))
        level.display(WINDOW)
        window.blit(mac.image, (mac.x, mac.y))

        pygame.display.flip()
        
        if (mac.x, mac.y) == (ether.x, ether.y):
            mac.grab()
            
        if (mac.x, mac.y) == (needle.x, needle.y):
            mac.grab()
            
        if (mac.x, mac.y) == (tube.x, tube.y):
            mac.grab()
            
        if level.structure[mac.case_y][mac.case_x] == 'a':
            if mac.num_objects == 3:
                #afficher message
                CONTINUE = 0
            else:
                #afficher message 
                CONTINUE = 0