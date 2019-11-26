#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from classlevel import *
from classhero import *
from constants import *
from classobjects import *

class Engine:

	def __init__(self):
		pygame.init()
		self.set_attributes()
		self.init_pygame()
		# lancement du programme
		self.main()

	def init_pygame(self):
		pygame.display.set_icon(self.icone_image)
		pygame.display.set_caption(TITLE_WINDOW)

	def set_attributes(self):
		self.window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
		self.set_custom_objects()
		self.set_images()

	def set_images(self):
		# différencier les convert() et les convert_alpha()
		self.icone_image = pygame.image.load(IMAGE_MACGYVER).convert_()
		self.background_image = pygame.image.load(IMAGE_BACKGROUND).convert()
		self.mac_image = pygame.image.load(IMAGE_MACGYVER).convert()
		self.wall_image = pygame.image.load(IMAGE_WALL).convert()
		self.ether_image = pygame.image.load(IMAGE_ETHER).convert_alpha() # gestion de la transparence
		self.needle_image = pygame.image.load(IMAGE_NEEDLE).convert_alpha()
		self.tube_image = pygame.image.load(IMAGE_TUBE).convert_alpha()

	def set_custom_objects(self):
		# instanciation des objets
		self.lvl = Level(FILE)
		self.hero = Hero()
		self.ether = Object()
		self.tube = Object()
		self.needle = Object()

	def should_we_grab(self):
		for obj in [self.needle, self.ether, self.tube]:
			if (self.hero.x, self.hero.y) == (obj.x, obj.y):
				self.hero.grab()

	def main(self):
		pygame.display.flip()

		continu = 1
		while continu:
		    pygame.time.Clock().tick(30) #limiter la vitesse de la boucle 

		    for event in pygame.event.get():

		        if event.type == QUIT:
		            continu = 0

		        elif event.type == KEYDOWN:

		            if event.key == K_RIGHT:
		                self.hero.move('right', self.lvl)
		            elif event.key == K_LEFT:
		                self.hero.move('left', self.lvl)
		            elif event.key == K_UP:
		                self.hero.move('up', self.lvl)
		            elif event.key == K_DOWN:
		                self.hero.move('down', self.lvl)

		        # affichage nouvelles positions  
		        self.window.blit(self.background_image, (0,0))
		        self.lvl.show(self.window)
		        self.window.blit(self.mac_image, (self.hero.x, self.hero.y))

		        pygame.display.flip()

		        self.should_we_grab()

		        if self.lvl.structure[self.hero.case_y][self.hero.case_x] == 'a':
		            if self.hero.num_objects == 3:
		                #afficher message
		                continu = 0
		            else:
		                #afficher message 
		                continu = 0

if "__main__" == __name__:
	e = Engine()