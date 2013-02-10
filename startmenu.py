import pygame
import time

from pygame.locals import *
from pygame.sprite import Sprite
from constants import SCREEN_WIDTH,SCREEN_HEIGHT

class Button:
	def __init__(self, left, top, width, height, img):
		self.left = left
		self.top =top
		self.width = width
		self.height = height
		self.img = img
		button = pygame.Surface((width,height), pygame.SRCALPHA, 32)
		button = button.convert_alpha()
		screen.blit(button, (left,top))
		image = pygame.image.load(img)
		screen.blit(image,(left,top))

#creates window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Avengers - Six Guys')

#splash screen
splash = pygame.Surface(screen.get_size())
splash = splash.convert()
splash.fill((0,0,0))
x, y = screen.get_size()
screen.blit(splash, (0, 0))
logo = pygame.image.load("images/splash.png").convert_alpha()
screen.blit(logo, (0,0))
pygame.display.update()

start = Button(369, 363, 122, 22, "images/menusprites/startgame.png")
instructions = Button(367, 393, 115, 22, "images/menusprites/instructions.png")
options = Button(383, 423, 85, 22, "images/menusprites/options.png")
quit = Button(371, 453, 12, 22, "images/menusprites/quit.png")
volume = Button(970, 0, 25, 25, "images/menusprites/volume.png")
pygame.display.update()

playing = False

while(not pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
	pygame.event.wait()

for event in pygame.event.get():
	if event.type == MOUSEBUTTONDOWN:
		if event.button == 1:

			playing = pygame.Rect(start.left, start.top, start.width, start.height).collidepoint(pygame.mouse.get_pos())

			inst = pygame.Rect(instructions.left, instructions.top, instructions.width, instructions.height).collidepoint(pygame.mouse.get_pos())

			ops = pygame.Rect(options.left, options.top, options.width, options.height).collidepoint(pygame.mouse.get_pos())

			quits = pygame.Rect(quit.left, quit.top, quit.width, quit.height).collidepoint(pygame.mouse.get_pos())

			vol = pygame.Rect(volume.left, volume.top, volume.width, volume.height).collidepoint(pygame.mouse.get_pos())