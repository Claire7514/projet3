#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *

from classlevel import *
from classhero import *
from constants import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))

icone = pygame.image.load(image_macgyver).convert_alpha()
pygame.display.set_icon(icone)

pygame.display.set_caption(title_window)

background = pygame.image.load(image_background).convert()
mac = pygame.image.load(image_macgyver).convert_alpha()
wall = pygame.image.load(image_wall).convert()
ether = pygame.image.load(image_ether).convert_alpha()
needle = pygame.image.load(image_needle).convert_alpha()
tube = pygame.image.load(image_tube).convert_alpha()

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
        window.blit(background, (0,0))
        level.display(window)
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